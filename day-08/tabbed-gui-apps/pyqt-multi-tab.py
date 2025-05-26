import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QTabWidget, QTextEdit, QStyleFactory
)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor

class TabOne(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Welcome to Tab 1")
        label.setFont(QFont("Arial", 14))
        layout.addWidget(label)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter something...")
        layout.addWidget(self.input)

        button = QPushButton("Click Me")
        button.clicked.connect(self.on_click)
        layout.addWidget(button)

        self.setLayout(layout)

    def on_click(self):
        text = self.input.text()
        self.input.setText(f"You said: {text}")

class TabTwo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is Tab 2")
        label.setFont(QFont("Arial", 14))
        layout.addWidget(label)

        text_area = QTextEdit()
        text_area.setPlaceholderText("Type notes here...")
        layout.addWidget(text_area)

        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Tabbed Dark Themed App")
        self.resize(600, 400)

        layout = QVBoxLayout()
        tabs = QTabWidget()

        tabs.addTab(TabOne(), "Tab 1")
        tabs.addTab(TabTwo(), "Tab 2")

        layout.addWidget(tabs)
        self.setLayout(layout)



def apply_dark_theme(app):
    app.setStyle(QStyleFactory.create("Fusion"))
    dark_palette = app.palette()

    dark_palette.setColor(dark_palette.Window, QColor("#2b2b2b"))
    dark_palette.setColor(dark_palette.WindowText, QColor("#ffffff"))
    dark_palette.setColor(dark_palette.Base, QColor("#3c3f41"))
    dark_palette.setColor(dark_palette.AlternateBase, QColor("#2b2b2b"))
    dark_palette.setColor(dark_palette.ToolTipBase, QColor("#ffffff"))
    dark_palette.setColor(dark_palette.ToolTipText, QColor("#ffffff"))
    dark_palette.setColor(dark_palette.Text, QColor("#ffffff"))
    dark_palette.setColor(dark_palette.Button, QColor("#3c3f41"))
    dark_palette.setColor(dark_palette.ButtonText, QColor("#ffffff"))
    dark_palette.setColor(dark_palette.BrightText, QColor("#ff0000"))
    dark_palette.setColor(dark_palette.Highlight, QColor("#007acc"))
    dark_palette.setColor(dark_palette.HighlightedText, QColor("#ffffff"))

    app.setPalette(dark_palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
