import os
import sys

# Set Qt plugin path relative to the executable
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    qt_plugins = os.path.join(base_path, "PySide6", "plugins")
    os.environ["QT_PLUGIN_PATH"] = qt_plugins

from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                               QHBoxLayout, QWidget, QPushButton, QLabel, 
                               QLineEdit, QFileDialog, QMessageBox, QTextEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from ui_mainwindow import Ui_MainWindow
from About_ArborescenceASCII import AboutDialog
from filedetails import FileDetailsDialog
from tree_generator import TreeGenerator
from maxLengthDialog import maxLengthDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize input_folder attribute and tree generator
        self.input_folder = ""
        self.tree_generator = TreeGenerator()

        # Configure preview text widget for proper formatting
        self.setup_preview_text()

        self.ui.browse_btn.clicked.connect(self.browse_input_folder)
        self.ui.generateTree_btn.clicked.connect(self.generate_tree_structure)
        self.ui.generateTree_btn.setEnabled(False)

        self.ui.input_path_display.setPlaceholderText("No folder selected")
        self.ui.input_path_display.editingFinished.connect(self.check_manual_folder_input)

        self.update_generate_button_state()

        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionDetails.triggered.connect(self.show_details)
        self.ui.actionFilenameMaxLength.triggered.connect(self.configure_filename_length)
        
        self.ui.copy_btn.clicked.connect(self.copy_preview_text)

        self.ui.preview_text.setEnabled(True)

    def setup_preview_text(self):
        """Configure preview text widget with monospaced font for proper alignment"""
        # Set monospaced font for proper tabular formatting
        font = QFont("Consolas", 9)  # Windows
        if not font.exactMatch():
            font = QFont("Monaco", 9)  # macOS
        if not font.exactMatch():
            font = QFont("Liberation Mono", 9)  # Linux
        if not font.exactMatch():
            font = QFont("Courier New", 9)  # Fallback
        
        font.setFixedPitch(True)
        self.ui.preview_text.setFont(font)
        
        # Set some styling for better readability
        self.ui.preview_text.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                font-family: 'Consolas', 'Monaco', 'Liberation Mono', 'Courier New', monospace;
            }
        """)
        
        # Disable word wrapping to preserve formatting
        self.ui.preview_text.setLineWrapMode(QTextEdit.NoWrap)

    def default_connect_action(self):
        print("default action")
    
    def browse_input_folder(self):
        """Open dialog to select input folder"""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder to Scan",
            self.input_folder if self.input_folder else os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if folder:
            self.input_folder = folder
            self.ui.input_path_display.setText(folder)
            self.ui.input_path_display.setStyleSheet("color: black;")
            self.update_generate_button_state()    

    def update_generate_button_state(self):
        """Enable generate button when folder is selected"""
        if self.input_folder:
            self.ui.generateTree_btn.setEnabled(True)
            self.ui.status_label.setText("Ready to generate tree structure")
            self.ui.status_label.setStyleSheet("color: green; font-style: italic;")
        else:
            self.ui.generateTree_btn.setEnabled(False)
            self.ui.status_label.setText("Please select a folder to scan")
            self.ui.status_label.setStyleSheet("color: gray; font-style: italic;")

    def check_manual_folder_input(self):
        """Check if manually entered folder path is valid"""
        entered_path = self.ui.input_path_display.text().strip()
        
        if entered_path and os.path.exists(entered_path) and os.path.isdir(entered_path):
            # Valid folder path
            self.input_folder = entered_path
            self.ui.input_path_display.setStyleSheet("color: black;")
        else:
            # Invalid or empty path
            self.input_folder = ""
            if entered_path:
                self.ui.input_path_display.setStyleSheet("color: red;")
            else:
                self.ui.input_path_display.setStyleSheet("color: black;")
        
        self.update_generate_button_state()

    def generate_tree_structure(self):
        """Generate tree structure and update preview"""
        try:
            # Update status
            self.ui.status_label.setText("Generating tree structure...")
            self.ui.status_label.setStyleSheet("color: blue; font-style: italic;")
            
            # Process the application events to update the UI
            QApplication.processEvents()
            
            # Generate tree using the separate module
            tree_content = self.tree_generator.generate_tree(self.input_folder)
            
            # Update preview with generated content
            self.ui.preview_text.setPlainText(tree_content)
            
            # Update status
            self.ui.status_label.setText("Tree structure generated successfully!")
            self.ui.status_label.setStyleSheet("color: green; font-style: italic;")
            
        except Exception as e:
            self.ui.status_label.setText("Error generating tree structure")
            self.ui.status_label.setStyleSheet("color: red; font-style: italic;")
            
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred while generating the tree structure:\n{str(e)}"
            )

    def copy_preview_text(self):
        text = self.ui.preview_text.toPlainText()
        QApplication.clipboard().setText(text)

    def show_about(self):
        dlg = AboutDialog(self)
        dlg.exec()

    def show_details(self):
        dlg = FileDetailsDialog("utils/file_details.toml")
        # dlg.show()
        dlg.exec()

    def configure_filename_length(self):
        """Allow user to configure maximum filename length"""
        current_length = self.tree_generator.get_max_filename_length()
        
        # Use custom dialog
        dlg = maxLengthDialog(self, current_length)
        result = dlg.exec()
        print(result)
        if result == True:
            new_length = dlg.get_max_length()
            
            if new_length != current_length:
                self.tree_generator.set_max_filename_length(new_length)
                self.ui.status_label.setText(f"Filename length set to {new_length} characters")
                self.ui.status_label.setStyleSheet("color: blue; font-style: italic;")
                
                # If there's already a tree generated, suggest regenerating
                if self.ui.preview_text.toPlainText().strip():
                    reply = QMessageBox.question(
                        self, 
                        "Regenerate Tree?", 
                        "Settings changed. Regenerate tree with new filename length?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        self.generate_tree_structure()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())