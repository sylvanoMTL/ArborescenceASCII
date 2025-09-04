import os
import sys
import tempfile


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



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_mainwindow.py, or

from ui_mainwindow import Ui_MainWindow
# from ui_about import Ui_AboutDialog
from About_ArborescenceASCII import AboutDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize input_folder attribute
        self.input_folder = ""

        self.ui.browse_btn.clicked.connect(self.browse_input_folder)
        self.ui.generateTree_btn.clicked.connect(self.generate_tree_structure)
        self.ui.generateTree_btn.setEnabled(False)

        self.ui.input_path_display.setPlaceholderText("No folder selected")
        self.ui.input_path_display.editingFinished.connect(self.check_manual_folder_input)

        self.update_generate_button_state()

        self.ui.actionAbout.triggered.connect(self.show_about)

        self.ui.copy_btn.clicked.connect(self.copy_preview_text)


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
            self.ui.input_path_display.setStyleSheet("color: black;")  # Normal text color
        else:
            # Invalid or empty path
            self.input_folder = ""
            if entered_path:  # Only show red if something was entered
                self.ui.input_path_display.setStyleSheet("color: red;")
            else:
                self.ui.input_path_display.setStyleSheet("color: black;")
        
        # Update the generate button state
        self.update_generate_button_state()

    
    def generate_tree_structure_string(self, folder_path, prefix="", is_last=True):
        """Generate tree structure as string"""
        items = []
        try:
            # Get all items in the folder
            all_items = sorted(os.listdir(folder_path))
            
            for i, item in enumerate(all_items):
                item_path = os.path.join(folder_path, item)
                is_last_item = i == len(all_items) - 1
                
                # Choose the appropriate tree symbols
                if is_last_item:
                    current_prefix = "└── "
                    next_prefix = prefix + "    "
                else:
                    current_prefix = "├── "
                    next_prefix = prefix + "│   "
                
                items.append(f"{prefix}{current_prefix}{item}")
                
                # If it's a directory, recursively add its contents
                if os.path.isdir(item_path):
                    try:
                        sub_items = self.generate_tree_structure_string(item_path, next_prefix, is_last_item)
                        items.extend(sub_items)
                    except PermissionError:
                        items.append(f"{next_prefix}[Permission Denied]")
                        
        except PermissionError:
            items.append(f"{prefix}[Permission Denied]")
            
        return items



    def generate_tree_structure(self):
        """Generate tree structure and update preview"""
        try:
            # Update status
            self.ui.status_label.setText("Generating tree structure...")
            self.ui.status_label.setStyleSheet("color: blue; font-style: italic;")
            
            # Process the application events to update the UI
            QApplication.processEvents()
            
            tree_content = ""
            
            # Try using the imported function first
            try:
                # # Use temporary file for the imported function
                # with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
                #     temp_path = temp_file.name
                
                # creer_arborescence(self.input_folder, temp_path)
                # with open(temp_path, 'r', encoding='utf-8') as f:
                #     tree_content = f.read()
                
                # # Clean up temporary file
                # os.unlink(temp_path)
                # Fallback to built-in tree generator
                folder_name = os.path.basename(self.input_folder) or self.input_folder
                tree_lines = [folder_name]
                tree_lines.extend(self.generate_tree_structure_string(self.input_folder))
                tree_content = "\n".join(tree_lines)    
            except (NameError, ImportError, Exception) as e:
                pass
            
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
        text = self.ui.preview_text.toPlainText()   # QTextEdit
        # or .text() if it's a QLineEdit / QLabel
        QApplication.clipboard().setText(text)

    def show_about(self):
        dlg = AboutDialog(self)
        dlg.exec()   # blocks until closed (modal dialog)
        # alternatively: dlg.show()  # non-blocking (modeless)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
