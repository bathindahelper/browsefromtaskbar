from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class PanelCascadeMenuApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PanelCascadeMenu")

        self.setWindowFlags(Qt.Window)

        self.setFixedSize(40, 40)
        self.move(300, 200)

        main_layout = QVBoxLayout(self)

        icon_label = QLabel("📁")
        icon_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(icon_label)