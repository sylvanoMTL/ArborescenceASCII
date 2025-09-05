import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QSplitter, QWidget, QVBoxLayout
from PySide6.QtCore import QDir

class ExplorerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Explorer Left Panel Example")
        self.resize(800, 600)

        # Main container
        container = QWidget()
        layout = QVBoxLayout(container)
        self.setCentralWidget(container)

        # Splitter: left and right panels
        splitter = QSplitter()
        layout.addWidget(splitter)

        # --------------------
        # Left panel: folder tree
        # --------------------
        self.model = QFileSystemModel()
        self.model.setRootPath("")           # Start from filesystem root
        # self.model.setFilter(self.model.Dirs)  # Show only directories
        self.model.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(""))  # Could use home directory
        self.tree.setHeaderHidden(True)  # Hide column headers

        splitter.addWidget(self.tree)

        # --------------------
        # Right panel: placeholder
        # --------------------
        from PySide6.QtWidgets import QLabel
        self.right_panel = QLabel("Right panel: file details here")
        self.right_panel.setStyleSheet("background-color: #eee;")
        self.right_panel.setMinimumWidth(300)
        splitter.addWidget(self.right_panel)

        splitter.setSizes([250, 550])  # initial widths

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExplorerWindow()
    window.show()
    sys.exit(app.exec())
