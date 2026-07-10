from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class PanelCascadeMenuApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PanelCascadeMenu")

        self.setWindowFlags(Qt.Window)

        self.setFixedSize(40, 40)
        self.move(300, 200)
        layout = QVBoxLayout(self)

        label = QLabel("📁")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
