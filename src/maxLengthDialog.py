# pyside6-uic maxLength.ui -o ui_maxlength.py
import sys

from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator

from ui_maxlength import Ui_maxLengthDialog


class maxLengthDialog(QDialog, Ui_maxLengthDialog):
	def __init__(self, parent=None, current_value=64):
		super().__init__(parent)
		self.setupUi(self)
		
		# Set window title
		self.setWindowTitle("Configure Maximum Filename Length")
		
		# Initialize the max_length field with current value
		self.max_length.setText(str(current_value))
		
		# Set input validation (only integers between 20 and 500)
		validator = QIntValidator(20, 500)
		self.max_length.setValidator(validator)
		
		# Set placeholder text
		self.max_length.setPlaceholderText("Enter length (20-500)")
		
		# Select all text when dialog opens
		self.max_length.selectAll()
		self.max_length.setFocus()
	
	def get_max_length(self):
		"""Get the entered maximum length value"""
		try:
			return int(self.max_length.text())
		except ValueError:
			return 64  # Default fallback
	
	def set_max_length(self, value):
		"""Set the maximum length value"""
		self.max_length.setText(str(value))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	dlg = maxLengthDialog(current_value=64)
	result = dlg.exec()   # modal (blocks until closed)
	
	if result == QDialog.Accepted:
		print(f"New max length: {dlg.get_max_length()}")
	else:
		print("Cancelled")
	
	sys.exit(0)  # since exec() already blocks, exit cleanly after closing