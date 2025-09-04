# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setCheckable(True)
        self.actionDetails = QAction(MainWindow)
        self.actionDetails.setObjectName(u"actionDetails")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.path_layout = QHBoxLayout()
        self.path_layout.setSpacing(6)
        self.path_layout.setObjectName(u"path_layout")
        self.path_layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.path_layout.setContentsMargins(-1, 0, -1, -1)
        self.input_path_display = QLineEdit(self.centralwidget)
        self.input_path_display.setObjectName(u"input_path_display")
        self.input_path_display.setMinimumSize(QSize(0, 30))

        self.path_layout.addWidget(self.input_path_display)

        self.browse_btn = QPushButton(self.centralwidget)
        self.browse_btn.setObjectName(u"browse_btn")
        self.browse_btn.setMinimumSize(QSize(0, 30))

        self.path_layout.addWidget(self.browse_btn)

        self.generateTree_btn = QPushButton(self.centralwidget)
        self.generateTree_btn.setObjectName(u"generateTree_btn")
        self.generateTree_btn.setMinimumSize(QSize(0, 30))

        self.path_layout.addWidget(self.generateTree_btn)


        self.verticalLayout.addLayout(self.path_layout)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout.addWidget(self.status_label)

        self.preview_text = QTextEdit(self.centralwidget)
        self.preview_text.setObjectName(u"preview_text")
        self.preview_text.setEnabled(False)

        self.verticalLayout.addWidget(self.preview_text)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copy_btn = QPushButton(self.frame)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setMinimumSize(QSize(0, 30))
        self.copy_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.copy_btn)

        self.save_btn = QPushButton(self.frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 30))
        self.save_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 33))
        self.menuPrefe = QMenu(self.menuBar)
        self.menuPrefe.setObjectName(u"menuPrefe")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuPrefe.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuPrefe.addAction(self.actionDetails)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ArborescenceASCII", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDetails.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.browse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.generateTree_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Tree", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuPrefe.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

