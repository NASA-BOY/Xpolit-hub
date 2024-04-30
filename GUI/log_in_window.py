from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_page import Ui_MainWindow
import Network.Commands as cmds
from start_client import client

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(950, 615)
        StackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.start)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.logo_main = QtWidgets.QLabel(self.start)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_main.sizePolicy().hasHeightForWidth())
        self.logo_main.setSizePolicy(sizePolicy)
        self.logo_main.setText("")
        self.logo_main.setPixmap(QtGui.QPixmap("imgs/logos/xploit-hub-logo-nobg.png"))
        self.logo_main.setScaledContents(True)
        self.logo_main.setObjectName("logo_main")
        self.horizontalLayout_10.addWidget(self.logo_main)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sign_in_btn = QtWidgets.QPushButton(self.start)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_in_btn.sizePolicy().hasHeightForWidth())
        self.sign_in_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setStyleSheet("background-color: rgb(255, 163, 26);")
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.verticalLayout.addWidget(self.sign_in_btn)
        self.sign_up_btn = QtWidgets.QPushButton(self.start)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_up_btn.sizePolicy().hasHeightForWidth())
        self.sign_up_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(22)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.verticalLayout.addWidget(self.sign_up_btn)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        StackedWidget.addWidget(self.start)
        self.sign_in_page = QtWidgets.QWidget()
        self.sign_in_page.setObjectName("sign_in_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sign_in_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.logo_sign_in = QtWidgets.QLabel(self.sign_in_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_sign_in.sizePolicy().hasHeightForWidth())
        self.logo_sign_in.setSizePolicy(sizePolicy)
        self.logo_sign_in.setText("")
        self.logo_sign_in.setPixmap(QtGui.QPixmap("imgs/logos/xploit-hub-logo-nobg.png"))
        self.logo_sign_in.setScaledContents(True)
        self.logo_sign_in.setObjectName("logo_sign_in")
        self.horizontalLayout_4.addWidget(self.logo_sign_in)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.label_sign_in = QtWidgets.QLabel(self.sign_in_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_sign_in.setFont(font)
        self.label_sign_in.setObjectName("label_sign_in")
        self.verticalLayout_5.addWidget(self.label_sign_in)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Email = QtWidgets.QLabel(self.sign_in_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Email.sizePolicy().hasHeightForWidth())
        self.Email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.verticalLayout_3.addWidget(self.Email)
        self.email_input = QtWidgets.QLineEdit(self.sign_in_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_input.sizePolicy().hasHeightForWidth())
        self.email_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email_input.setFont(font)
        self.email_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.email_input.setStyleSheet("\\")
        self.email_input.setObjectName("email_input")
        self.verticalLayout_3.addWidget(self.email_input)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Pass = QtWidgets.QLabel(self.sign_in_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Pass.setFont(font)
        self.Pass.setObjectName("Pass")
        self.verticalLayout_6.addWidget(self.Pass)
        self.pass_input = QtWidgets.QLineEdit(self.sign_in_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_input.sizePolicy().hasHeightForWidth())
        self.pass_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.pass_input.setFont(font)
        self.pass_input.setInputMask("")
        self.pass_input.setText("")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.verticalLayout_6.addWidget(self.pass_input)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.msg_sign_in = QtWidgets.QLabel(self.sign_in_page)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        self.msg_sign_in.setFont(font)
        self.msg_sign_in.setObjectName("msg_sign_in")
        self.verticalLayout_5.addWidget(self.msg_sign_in)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.signing_in_btn = QtWidgets.QPushButton(self.sign_in_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signing_in_btn.sizePolicy().hasHeightForWidth())
        self.signing_in_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(16)
        self.signing_in_btn.setFont(font)
        self.signing_in_btn.setStyleSheet("background-color: rgb(255, 163, 26);")
        self.signing_in_btn.setObjectName("signing_in_btn")
        self.horizontalLayout_5.addWidget(self.signing_in_btn)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 3)
        self.verticalLayout_5.setStretch(5, 3)
        self.verticalLayout_5.setStretch(6, 1)
        StackedWidget.addWidget(self.sign_in_page)
        self.sign_up_page = QtWidgets.QWidget()
        self.sign_up_page.setObjectName("sign_up_page")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.sign_up_page)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.logo_sign_up = QtWidgets.QLabel(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_sign_up.sizePolicy().hasHeightForWidth())
        self.logo_sign_up.setSizePolicy(sizePolicy)
        self.logo_sign_up.setText("")
        self.logo_sign_up.setPixmap(QtGui.QPixmap("imgs/logos/xploit-hub-logo-nobg.png"))
        self.logo_sign_up.setScaledContents(True)
        self.logo_sign_up.setObjectName("logo_sign_up")
        self.horizontalLayout_11.addWidget(self.logo_sign_up)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 2)
        self.horizontalLayout_11.setStretch(2, 3)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.label_sign_up = QtWidgets.QLabel(self.sign_up_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_sign_up.setFont(font)
        self.label_sign_up.setObjectName("label_sign_up")
        self.verticalLayout_14.addWidget(self.label_sign_up)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.new_email = QtWidgets.QLabel(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_email.sizePolicy().hasHeightForWidth())
        self.new_email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_email.setFont(font)
        self.new_email.setObjectName("new_email")
        self.verticalLayout_8.addWidget(self.new_email)
        self.new_email_input = QtWidgets.QLineEdit(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_email_input.sizePolicy().hasHeightForWidth())
        self.new_email_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_email_input.setFont(font)
        self.new_email_input.setObjectName("new_email_input")
        self.verticalLayout_8.addWidget(self.new_email_input)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.new_username = QtWidgets.QLabel(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_username.sizePolicy().hasHeightForWidth())
        self.new_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_username.setFont(font)
        self.new_username.setObjectName("new_username")
        self.verticalLayout_9.addWidget(self.new_username)
        self.new_username_input = QtWidgets.QLineEdit(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_username_input.sizePolicy().hasHeightForWidth())
        self.new_username_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_username_input.setFont(font)
        self.new_username_input.setObjectName("new_username_input")
        self.verticalLayout_9.addWidget(self.new_username_input)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.new_pass = QtWidgets.QLabel(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_pass.sizePolicy().hasHeightForWidth())
        self.new_pass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_pass.setFont(font)
        self.new_pass.setObjectName("new_pass")
        self.verticalLayout_12.addWidget(self.new_pass)
        self.new_pass_input = QtWidgets.QLineEdit(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_pass_input.sizePolicy().hasHeightForWidth())
        self.new_pass_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_pass_input.setFont(font)
        self.new_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass_input.setObjectName("new_pass_input")
        self.verticalLayout_12.addWidget(self.new_pass_input)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.confirm_pass = QtWidgets.QLabel(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_pass.sizePolicy().hasHeightForWidth())
        self.confirm_pass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_pass.setFont(font)
        self.confirm_pass.setObjectName("confirm_pass")
        self.verticalLayout_13.addWidget(self.confirm_pass)
        self.confirm_pass_input = QtWidgets.QLineEdit(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_pass_input.sizePolicy().hasHeightForWidth())
        self.confirm_pass_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_pass_input.setFont(font)
        self.confirm_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pass_input.setObjectName("confirm_pass_input")
        self.verticalLayout_13.addWidget(self.confirm_pass_input)
        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.verticalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem13)
        self.msg_sign_up = QtWidgets.QLabel(self.sign_up_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msg_sign_up.setFont(font)
        self.msg_sign_up.setObjectName("msg_sign_up")
        self.verticalLayout_14.addWidget(self.msg_sign_up)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem15)
        self.signing_up_btn = QtWidgets.QPushButton(self.sign_up_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signing_up_btn.sizePolicy().hasHeightForWidth())
        self.signing_up_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(16)
        self.signing_up_btn.setFont(font)
        self.signing_up_btn.setStyleSheet("background-color: rgb(255, 163, 26);")
        self.signing_up_btn.setObjectName("signing_up")
        self.horizontalLayout_12.addWidget(self.signing_up_btn)
        self.horizontalLayout_12.setStretch(0, 5)
        self.horizontalLayout_12.setStretch(1, 1)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.verticalLayout_14.setStretch(0, 12)
        self.verticalLayout_14.setStretch(1, 1)
        self.verticalLayout_14.setStretch(2, 12)
        self.verticalLayout_14.setStretch(6, 2)
        StackedWidget.addWidget(self.sign_up_page)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

        # ===ADDED CODE===
        # BUTTONS
        self.sign_in_btn.clicked.connect(self.load_sign_in_page)
        self.sign_up_btn.clicked.connect(self.load_sign_up_page)
        self.signing_in_btn.clicked.connect(lambda: self.sign_in_check(email=self.email_input.text(),
                                                                       passw=self.pass_input.text()))

        self.signing_up_btn.clicked.connect(lambda: self.sign_up_check(email=self.new_email_input.text(),
                                                                       username=self.new_username_input.text(),
                                                                       passw=self.new_pass_input.text(),
                                                                       confirm_passw=self.confirm_pass_input.text()))


    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.sign_in_btn.setText(_translate("StackedWidget", "Sign In"))
        self.sign_up_btn.setText(_translate("StackedWidget", "Sign Up"))
        self.label_sign_in.setText(_translate("StackedWidget", "Sign In"))
        self.Email.setText(_translate("StackedWidget", "Email/username:"))
        self.Pass.setText(_translate("StackedWidget", "Password"))
        self.msg_sign_in.setText(_translate("StackedWidget", "*"))
        self.signing_in_btn.setText(_translate("StackedWidget", "Sign In"))
        self.label_sign_up.setText(_translate("StackedWidget", "Sign Up"))
        self.new_email.setText(_translate("StackedWidget", "Email:"))
        self.new_username.setText(_translate("StackedWidget", "Username"))
        self.new_pass.setText(_translate("StackedWidget", "Password"))
        self.confirm_pass.setText(_translate("StackedWidget", "Confirm Password"))
        self.msg_sign_up.setText(_translate("StackedWidget", "*"))
        self.signing_up_btn.setText(_translate("StackedWidget", "Sign Up"))

    def load_sign_in_page(self):
        StackedWidget.setCurrentWidget(self.sign_in_page)

    def load_sign_up_page(self):
        StackedWidget.setCurrentWidget(self.sign_up_page)

    def sign_in_check(self, email, passw):
        client.send_data_list(cmds.SIGN_IN_CMD, [email, passw])

        while True:
            data = client.receive_data()
            if data is not None:
                print(data)
                _, status, msg = data
                if status:
                    client.set_username(msg)  # If the sign in is successful the msg from server is the user's username
                    client.set_email(email)
                    self.open_main_window()
                else:
                    self.msg_sign_in.setText("* " + msg)
                break

    def sign_up_check(self, email, username, passw, confirm_passw):
        client.send_data_list(cmds.SIGN_UP_CMD, [email, username, passw, confirm_passw])

        while True:
            data = client.receive_data()
            if data is not None:
                print(data)
                _, status, msg = data
                if status:
                    client.set_username(username)
                    client.set_email(email)
                    self.open_main_window()
                else:
                    self.msg_sign_up.setText("* " + msg)
                break

    def open_main_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


app = QtWidgets.QApplication(sys.argv)
StackedWidget = QtWidgets.QStackedWidget()
ui = Ui_StackedWidget()
ui.setupUi(StackedWidget)

def start():
    StackedWidget.show()
    sys.exit(app.exec_())


