# main.py
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from gui import Ui_MainWindow
from logic import detect_faces, convert_cv_qt

class FaceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.uploadButton.clicked.connect(self.load_image)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            result = detect_faces(file_name)
            pixmap = convert_cv_qt(result)
            self.ui.imageLabel.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceApp()
    window.show()
    sys.exit(app.exec_())
