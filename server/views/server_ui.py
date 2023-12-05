# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_ServerForm(object):
    def setupUi(self, ServerForm):
        if not ServerForm.objectName():
            ServerForm.setObjectName(u"ServerForm")
        ServerForm.resize(600, 400)
        ServerForm.setMinimumSize(QSize(600, 400))
        ServerForm.setMaximumSize(QSize(600, 400))
        ServerForm.setStyleSheet(u"background-color: #fbf1c7")
        self.server_console = QTextEdit(ServerForm)
        self.server_console.setObjectName(u"server_console")
        self.server_console.setGeometry(QRect(10, 60, 581, 331))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.server_console.setFont(font)
        self.server_console.setStyleSheet(u"background-color: #ffffff; color: #282828;")
        self.server_console.setReadOnly(True)
        self.server_button = QPushButton(ServerForm)
        self.server_button.setObjectName(u"server_button")
        self.server_button.setGeometry(QRect(10, 10, 101, 41))
        self.server_button.setStyleSheet(u"background-color: #282828; color: #fbf1c7;")
        self.horizontalLayoutWidget = QWidget(ServerForm)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(116, 13, 461, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.horizontalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setStyleSheet(u"color: #282828")

        self.horizontalLayout.addWidget(self.status_label)

        self.connected_label = QLabel(self.horizontalLayoutWidget)
        self.connected_label.setObjectName(u"connected_label")
        self.connected_label.setStyleSheet(u"color: #282828")

        self.horizontalLayout.addWidget(self.connected_label)


        self.retranslateUi(ServerForm)

        QMetaObject.connectSlotsByName(ServerForm)
    # setupUi

    def retranslateUi(self, ServerForm):
        ServerForm.setWindowTitle(QCoreApplication.translate("ServerForm", u"Form", None))
        self.server_button.setText(QCoreApplication.translate("ServerForm", u"ENCENDER", None))
        self.status_label.setText("")
        self.connected_label.setText("")
    # retranslateUi

