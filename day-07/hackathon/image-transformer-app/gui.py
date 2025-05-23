# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from logic import ImageProcessor

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Transformer Tool")
        self.processor = ImageProcessor()
        self.image_path = None

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Upload Image", command=self.upload_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Save Image", command=self.save_image).pack(side=tk.LEFT, padx=5)

        self.image_label = tk.Label(frame)
        self.image_label.grid(row=1, column=0, columnspan=2)

        self.transform_list = [
            "Grayscale", "Gaussian Blur", "Median Blur", "Sobel", "Canny",
            "Threshold", "Rotate", "Resize", "Erode", "Dilate",
            "Flip Horizontal", "Flip Vertical"
        ]
        self.transformation = tk.StringVar()
        self.transformation.set(self.transform_list[0])

        transform_menu = ttk.Combobox(frame, textvariable=self.transformation, values=self.transform_list)
        transform_menu.grid(row=2, column=0, pady=10)

        tk.Button(frame, text="Apply", command=self.apply_transformation).grid(row=2, column=1, pady=10)

        # Brightness slider
        self.brightness_slider = tk.Scale(frame, from_=-100, to=100, orient=tk.HORIZONTAL,
                                          label="Brightness", command=self.update_brightness_contrast)
        self.brightness_slider.set(0)
        self.brightness_slider.grid(row=3, column=0, padx=10)

        # Contrast slider
        self.contrast_slider = tk.Scale(frame, from_=50, to=300, orient=tk.HORIZONTAL,
                                        label="Contrast (x0.01)", command=self.update_brightness_contrast)
        self.contrast_slider.set(100)
        self.contrast_slider.grid(row=3, column=1, padx=10)

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.image_path = path
            self.processor.load_image(path)
            self.update_brightness_contrast(None)

    def reset_image(self):
        if self.processor.original is not None:
            self.processor.reset_image()
            self.brightness_slider.set(0)
            self.contrast_slider.set(100)
            self.show_image(self.processor.image)

    def apply_transformation(self):
        if self.processor.image is None:
            messagebox.showerror("Error", "Upload an image first")
            return

        transform_name = self.transformation.get()
        self.processor.apply(transform_name)
        self.show_image(self.processor.image)

    def update_brightness_contrast(self, _):
        if self.processor.original is None:
            return
        alpha = self.contrast_slider.get() / 100.0  # scale 50–300 to 0.5–3.0
        beta = self.brightness_slider.get()
        self.processor.adjust_brightness_contrast(alpha, beta)
        self.show_image(self.processor.image)

    def show_image(self, img):
        bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(bgr_img)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk

    def save_image(self):
        if self.processor.image is not None:
            path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if path:
                cv2.imwrite(path, self.processor.image)
                messagebox.showinfo("Success", f"Image saved to {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
