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
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 50, 351, 21))
        self.label_5.setStyleSheet(u"color: #282828;")
        self.verticalLayoutWidget = QWidget(LoginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 4, 201, 192))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: #d65d0e;")

        self.verticalLayout.addWidget(self.label_4)

        self.address_input = QLineEdit(self.verticalLayoutWidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setStyleSheet(u"color: #282828;")

        self.verticalLayout.addWidget(self.address_input)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: #d65d0e;")

        self.verticalLayout.addWidget(self.label_3)

        self.port_input = QLineEdit(self.verticalLayoutWidget)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setStyleSheet(u"color: #282828;")

        self.verticalLayout.addWidget(self.port_input)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"color: #d65d0e;")

        self.verticalLayout.addWidget(self.label_2)

        self.username_input = QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setStyleSheet(u"color: #282828;")

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
        self.label_5.setText(QCoreApplication.translate("LoginForm", u"GERARDO ENRIQUE RAMOS ESPINOZA - 21130599", None))
        self.label_4.setText(QCoreApplication.translate("LoginForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">DIRECCION:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("LoginForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">PUERTO:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">USERNAME:</span></p></body></html>", None))
        self.login_button.setText(QCoreApplication.translate("LoginForm", u"ENTRAR", None))
    # retranslateUi

