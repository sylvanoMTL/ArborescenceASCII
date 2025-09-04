import os
import sys

from PySide6.QtWidgets import QDialog,QApplication

#     pyside6-uic about.ui -o ui_about.py

from ui_about import Ui_AboutDialog



class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        # with open("about.txt", "r", encoding="utf-8") as f:
        #     content = f.read()
        # self.about_text.setPlainText(content)

        with open("utils/about.html", "r", encoding="utf-8") as f:
            self.about_text.setHtml(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = AboutDialog()
    dlg.exec()   # modal (blocks until closed)
    # dlg.show() # alternative: non-modal, but then you need app.exec()
    sys.exit(0)  # since exec() already blocks, exit cleanly after closing