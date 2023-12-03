# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 300)
        LoginForm.setMinimumSize(QSize(400, 300))
        LoginForm.setMaximumSize(QSize(400, 300))
        LoginForm.setStyleSheet(u"background-color: #fbf1c7")
        self.frame = QFrame(LoginForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 200, 401, 101))
        self.frame.setStyleSheet(u"background-color: #ebdbb2")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 31))
        self.label.setStyleSheet(u"color: #3c3836;")
        self.verticalLayoutWidget = QWidget(LoginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 70, 201, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"color: #d65d0e;")

        self.verticalLayout.addWidget(self.label_2)

        self.username_input = QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        font = QFont()
        font.setBold(True)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet(u"background-color: #3c3836;\n"
"color: #fbf1c7;\n"
"")

        self.verticalLayout.addWidget(self.login_button)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">TCP CHAT - TEC LAGUNA</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">USERNAME:</span></p></body></html>", None))
        self.login_button.setText(QCoreApplication.translate("LoginForm", u"ENTRAR", None))
    # retranslateUi

