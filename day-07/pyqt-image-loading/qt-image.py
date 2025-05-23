# In PyQt5, you can display images using a QLabel and loading the image with QPixmap.

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QFileDialog
)
from PyQt5.QtGui import QPixmap


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 640, 480)

        # Create widgets
        self.image_label = QLabel("No Image Loaded")
        self.image_label.setStyleSheet("border: 2px dashed #aaa;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)  # scale image to label size

        self.button = QPushButton("Upload Image")
        self.button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.button.clicked.connect(self.upload_image)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)


if __name__ == "__main__":
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
