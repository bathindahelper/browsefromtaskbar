#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication

from app import PanelCascadeMenuApp


def main():
    app = QApplication(sys.argv)

    window = PanelCascadeMenuApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
