# ArborescenceASCII

**Version 0.1**  
© 2025 Sylvain Boyer

## Overview

ArborescenceASCII is a desktop application that generates ASCII tree representations of folder structures. It provides a clean, text-based visualization of directory hierarchies that can be easily shared, documented, or included in reports.

## What it does

The application scans any selected folder on your computer and creates a visual tree structure using ASCII characters, similar to the classic `tree` command but with a modern graphical interface and additional customization options.

**Example output:**
```
MyProject/
├── src/
│   ├── main.py
│   └── utils.py
├── docs/
│   └── readme.txt
└── tests/
    └── test_main.py
```

## Key Features

- **Easy folder selection** - Browse and select any folder using a simple file dialog
- **Customizable file information** - Choose what details to display (file size, modification date, file type, etc.)
- **Filename length control** - Set maximum filename length to keep output clean and readable
- **Copy to clipboard** - Instantly copy the generated tree structure for use in documentation or reports
- **Clean, monospaced output** - Properly formatted text that maintains alignment when pasted elsewhere

## Use Cases

- **Documentation** - Include folder structures in project documentation
- **Code reviews** - Share project organization with team members
- **File organization** - Visualize and understand complex directory structures
- **System administration** - Document server or system folder layouts
- **Academic projects** - Show project structure in reports or assignments

## Configuration

The application allows you to customize which file details are displayed through an intuitive preferences dialog. You can choose to show or hide:

- File sizes
- File types
- Creation dates
- Modification dates
- Access dates

## Requirements

- Windows operating system
- No additional software required (standalone application)

---

**Website:** [www.the-frog.fr](https://www.the-frog.fr)

This software is provided "as-is" without any warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.