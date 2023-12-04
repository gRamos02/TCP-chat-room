# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_ChatForm(object):
    def setupUi(self, ChatForm):
        if not ChatForm.objectName():
            ChatForm.setObjectName(u"ChatForm")
        ChatForm.resize(549, 535)
        ChatForm.setStyleSheet(u"background-color: #fbf1c7;")
        self.verticalLayoutWidget = QWidget(ChatForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 551, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(529, 10))
        self.frame.setMaximumSize(QSize(600, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: #3c3836; color: #fbf1c7;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_label = QLabel(self.frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 10, 201, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.username_label.setFont(font1)

        self.verticalLayout.addWidget(self.frame)

        self.msg_output = QTextEdit(self.verticalLayoutWidget)
        self.msg_output.setObjectName(u"msg_output")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.msg_output.setFont(font2)
        self.msg_output.setStyleSheet(u"background-color: #f9f5d7; color: #282828;")
        self.msg_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.msg_output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_2 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.msg_input = QLineEdit(self.verticalLayoutWidget)
        self.msg_input.setObjectName(u"msg_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.msg_input.sizePolicy().hasHeightForWidth())
        self.msg_input.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.msg_input.setFont(font3)
        self.msg_input.setStyleSheet(u"background-color: #ffffff; color: #3c3836;")

        self.horizontalLayout.addWidget(self.msg_input)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.send_button = QPushButton(self.verticalLayoutWidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy2)
        self.send_button.setFont(font3)
        self.send_button.setStyleSheet(u"background-color: #3c3836; color: #fbf1c7")

        self.horizontalLayout.addWidget(self.send_button)

        self.horizontalSpacer_3 = QSpacerItem(17, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ChatForm)

        QMetaObject.connectSlotsByName(ChatForm)
    # setupUi

    def retranslateUi(self, ChatForm):
        ChatForm.setWindowTitle(QCoreApplication.translate("ChatForm", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("ChatForm", u"Bienvenido, {username}", None))
        self.send_button.setText(QCoreApplication.translate("ChatForm", u"ENVIAR", None))
    # retranslateUi

