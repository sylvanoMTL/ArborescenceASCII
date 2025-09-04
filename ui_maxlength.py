# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maxLength.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_maxLengthDialog(object):
    def setupUi(self, maxLengthDialog):
        if not maxLengthDialog.objectName():
            maxLengthDialog.setObjectName(u"maxLengthDialog")
        maxLengthDialog.resize(277, 105)
        self.verticalLayout = QVBoxLayout(maxLengthDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(maxLengthDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filename_maxLength_label = QLabel(self.frame)
        self.filename_maxLength_label.setObjectName(u"filename_maxLength_label")

        self.horizontalLayout.addWidget(self.filename_maxLength_label)

        self.max_length = QLineEdit(self.frame)
        self.max_length.setObjectName(u"max_length")

        self.horizontalLayout.addWidget(self.max_length)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(maxLengthDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(maxLengthDialog)
        self.buttonBox.accepted.connect(maxLengthDialog.accept)
        self.buttonBox.rejected.connect(maxLengthDialog.reject)

        QMetaObject.connectSlotsByName(maxLengthDialog)
    # setupUi

    def retranslateUi(self, maxLengthDialog):
        maxLengthDialog.setWindowTitle(QCoreApplication.translate("maxLengthDialog", u"Dialog", None))
        self.filename_maxLength_label.setText(QCoreApplication.translate("maxLengthDialog", u"Maximum File Length", None))
    # retranslateUi

