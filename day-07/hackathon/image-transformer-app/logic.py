# logic.py
import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        self.original = None
        self.image = None
        self.alpha = 1.0  # Contrast
        self.beta = 0     # Brightness

    def load_image(self, path):
        self.original = cv2.imread(path)
        self.image = self.original.copy()

    def reset_image(self):
        self.image = self.original.copy()
        self.alpha = 1.0
        self.beta = 0

    def apply(self, transform_name):
        if transform_name == "Grayscale":
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)

        elif transform_name == "Gaussian Blur":
            self.image = cv2.GaussianBlur(self.image, (7, 7), 0)

        elif transform_name == "Median Blur":
            self.image = cv2.medianBlur(self.image, 5)

        elif transform_name == "Sobel":
            sobelx = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=5)
            sobel = cv2.magnitude(sobelx, sobely)
            self.image = cv2.convertScaleAbs(sobel)

        elif transform_name == "Canny":
            self.image = cv2.Canny(self.image, 100, 200)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)

        elif transform_name == "Threshold":
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            _, self.image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)

        elif transform_name == "Rotate":
            h, w = self.image.shape[:2]
            M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 1)
            self.image = cv2.warpAffine(self.image, M, (w, h))

        elif transform_name == "Resize":
            self.image = cv2.resize(self.image, None, fx=0.5, fy=0.5)

        elif transform_name == "Erode":
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.erode(self.image, kernel, iterations=1)

        elif transform_name == "Dilate":
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv2.dilate(self.image, kernel, iterations=1)

        elif transform_name == "Flip Horizontal":
            self.image = cv2.flip(self.image, 1)

        elif transform_name == "Flip Vertical":
            self.image = cv2.flip(self.image, 0)

    def adjust_brightness_contrast(self, alpha, beta):
        """Apply contrast (alpha) and brightness (beta)"""
        self.alpha = alpha
        self.beta = beta
        self.image = cv2.convertScaleAbs(self.original, alpha=self.alpha, beta=self.beta)
