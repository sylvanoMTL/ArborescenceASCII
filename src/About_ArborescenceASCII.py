import os
import sys

from PySide6.QtWidgets import QDialog, QApplication

from ui_about import Ui_AboutDialog
from getResourcePath import get_resource_path

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Robust path handling for about.html
        try:           
            about_file = get_resource_path("utils", "about.html")
            with open(about_file, "r", encoding="utf-8") as f:
                self.about_text.setHtml(f.read())

        except FileNotFoundError:
            # Fallback content if file not found
            self.about_text.setHtml("""
                <h2>ArborescenceASCII v0.1</h2>
                <p><b>© 2025 Sylvain Boyer</b></p>
                <p>This software is provided "as-is" without any warranty.</p>
                <p>Visit: <a href="https://www.the-frog.fr">www.the-frog.fr</a></p>
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = AboutDialog()
    dlg.exec()
    sys.exit(0)