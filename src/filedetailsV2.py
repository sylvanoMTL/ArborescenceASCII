import sys
import toml
from PySide6.QtWidgets import (
    QApplication, QDialog, QWidget, QVBoxLayout, QGroupBox,
    QCheckBox, QScrollArea, QPushButton, QHBoxLayout
)
from PySide6.QtGui import QIcon
from getResourcePath import get_resource_path
from user_config import get_user_toml

class FileDetailsDialog(QDialog):
    def __init__(self, toml_file):
        super().__init__()
        self.setWindowTitle("File Details Selection")
        self.resize(450, 550)

        icon = get_resource_path("graphics", "icon.ico")
        self.setWindowIcon(QIcon(icon))

        self.toml_file = toml_file
        self.data = toml.load(self.toml_file)

        import copy
        self.initial_data = copy.deepcopy(self.data)
        self.checkboxes = {}

        main_layout = QVBoxLayout(self)

        # Buttons
        button_layout = QHBoxLayout()
        select_all_btn = QPushButton("Select All")
        unselect_all_btn = QPushButton("Unselect All")
        reset_btn = QPushButton("Reset")
        button_layout.addWidget(select_all_btn)
        button_layout.addWidget(unselect_all_btn)
        button_layout.addWidget(reset_btn)
        main_layout.addLayout(button_layout)

        select_all_btn.clicked.connect(self.select_all)
        unselect_all_btn.clicked.connect(self.unselect_all)
        reset_btn.clicked.connect(self.reset_all)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        main_layout.addWidget(scroll)

        container = QWidget()
        container_layout = QVBoxLayout(container)

        # Checkboxes grouped by category
        for category, items in self.data.items():
            group_box = QGroupBox(category.capitalize())
            group_layout = QVBoxLayout()
            self.checkboxes[category] = {}

            for item, value in items.items():
                checkbox = QCheckBox(item)
                checkbox.setChecked(value)
                checkbox.stateChanged.connect(self.make_update_fn(category, item))
                group_layout.addWidget(checkbox)
                self.checkboxes[category][item] = checkbox

            group_box.setLayout(group_layout)
            container_layout.addWidget(group_box)

        container.setLayout(container_layout)
        scroll.setWidget(container)

    def make_update_fn(self, category, item):
        """Return a function to update TOML when checkbox changes"""
        def update(value):
            self.data[category][item] = bool(value)
            self.save_toml()
        return update

    def save_toml(self):
        with open(self.toml_file, "w", encoding="utf-8") as f:
            toml.dump(self.data, f)

    def select_all(self):
        for items in self.checkboxes.values():
            for checkbox in items.values():
                checkbox.setChecked(True)

    def unselect_all(self):
        for items in self.checkboxes.values():
            for checkbox in items.values():
                checkbox.setChecked(False)

    def reset_all(self):
        for category, items in self.checkboxes.items():
            for item, checkbox in items.items():
                checkbox.setChecked(self.initial_data[category][item])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    toml_file = get_user_toml()
    dialog = FileDetailsDialog(toml_file)
    dialog.setModal(True)
    dialog.exec()
