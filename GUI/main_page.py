import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Network.Commands as cmds
from start_client import client
import Constants.Vulnerabilities as vuln
import time
from Constants import General as constants
import Constants.Errors as errors


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1035, 668)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 600))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.groupBox)
        self.logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("imgs/logos/xploit-hub-logo-nobg.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.menu_btns = QtWidgets.QVBoxLayout()
        self.menu_btns.setSpacing(6)
        self.menu_btns.setObjectName("menu_btns")
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setEnabled(True)
        self.line_7.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.menu_btns.addWidget(self.line_7)
        self.scan_page_btn = QtWidgets.QPushButton(self.groupBox)
        self.scan_page_btn.setEnabled(True)
        self.scan_page_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(13)
        self.scan_page_btn.setFont(font)
        self.scan_page_btn.setMouseTracking(False)
        self.scan_page_btn.setTabletTracking(False)
        self.scan_page_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scan_page_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scan_page_btn.setAcceptDrops(False)
        self.scan_page_btn.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.scan_page_btn.setCheckable(False)
        self.scan_page_btn.setAutoExclusive(False)
        self.scan_page_btn.setAutoDefault(False)
        self.scan_page_btn.setDefault(False)
        self.scan_page_btn.setFlat(True)
        self.scan_page_btn.setObjectName("scan_page_btn")
        self.menu_btns.addWidget(self.scan_page_btn)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setEnabled(True)
        self.line_5.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.menu_btns.addWidget(self.line_5)
        self.history_page_btn = QtWidgets.QPushButton(self.groupBox)
        self.history_page_btn.setEnabled(True)
        self.history_page_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(13)
        self.history_page_btn.setFont(font)
        self.history_page_btn.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.history_page_btn.setFlat(True)
        self.history_page_btn.setObjectName("history_page_btn")
        self.menu_btns.addWidget(self.history_page_btn)
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setEnabled(True)
        self.line_6.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.menu_btns.addWidget(self.line_6)
        self.learn_more_page_btn = QtWidgets.QPushButton(self.groupBox)
        self.learn_more_page_btn.setEnabled(True)
        self.learn_more_page_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(13)
        self.learn_more_page_btn.setFont(font)
        self.learn_more_page_btn.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.learn_more_page_btn.setFlat(True)
        self.learn_more_page_btn.setObjectName("learn_more_page_btn")
        self.menu_btns.addWidget(self.learn_more_page_btn)
        self.line_11 = QtWidgets.QFrame(self.groupBox)
        self.line_11.setEnabled(True)
        self.line_11.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.menu_btns.addWidget(self.line_11)
        self.verticalLayout.addLayout(self.menu_btns)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settings_btn = QtWidgets.QToolButton(self.groupBox)
        self.settings_btn.setEnabled(True)
        self.settings_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/imgs/resources/settings_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("imgs/resources/settings_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QtCore.QSize(30, 30))
        self.settings_btn.setAutoRaise(True)
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout_2.addWidget(self.settings_btn)
        self.account_username = QtWidgets.QLabel(self.groupBox)
        self.account_username.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(11)
        self.account_username.setFont(font)
        self.account_username.setObjectName("account_username")
        self.horizontalLayout_2.addWidget(self.account_username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_12 = QtWidgets.QFrame(self.groupBox)
        self.line_12.setEnabled(True)
        self.line_12.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.horizontalLayout.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(255, 163, 26);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(850, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setObjectName("welcome_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.welcome_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.welcome_txt = QtWidgets.QTextBrowser(self.welcome_page)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        self.welcome_txt.setFont(font)
        self.welcome_txt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.welcome_txt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.welcome_txt.setLineWidth(0)
        self.welcome_txt.setObjectName("welcome_txt")
        self.verticalLayout_2.addWidget(self.welcome_txt)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.welcome_page)
        self.new_scan_page = QtWidgets.QWidget()
        self.new_scan_page.setObjectName("new_scan_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.new_scan_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scan_title = QtWidgets.QLabel(self.new_scan_page)
        self.scan_title.setEnabled(True)
        self.scan_title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(30)
        self.scan_title.setFont(font)
        self.scan_title.setStyleSheet("")
        self.scan_title.setAlignment(QtCore.Qt.AlignCenter)
        self.scan_title.setObjectName("scan_title")
        self.verticalLayout_8.addWidget(self.scan_title)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.url_txt = QtWidgets.QLabel(self.new_scan_page)
        self.url_txt.setEnabled(True)
        self.url_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(17)
        self.url_txt.setFont(font)
        self.url_txt.setObjectName("url_txt")
        self.verticalLayout_9.addWidget(self.url_txt)
        self.url_input = QtWidgets.QLineEdit(self.new_scan_page)
        self.url_input.setEnabled(True)
        self.url_input.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.url_input.setFont(font)
        self.url_input.setText("")
        self.url_input.setObjectName("url_input")
        self.verticalLayout_9.addWidget(self.url_input)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cookies_text = QtWidgets.QLabel(self.new_scan_page)
        self.cookies_text.setEnabled(True)
        self.cookies_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(17)
        self.cookies_text.setFont(font)
        self.cookies_text.setObjectName("cookies_text")
        self.horizontalLayout_3.addWidget(self.cookies_text)
        self.cookies_help_btn = QtWidgets.QPushButton(self.new_scan_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookies_help_btn.sizePolicy().hasHeightForWidth())
        self.cookies_help_btn.setSizePolicy(sizePolicy)
        self.cookies_help_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cookies_help_btn.setFont(font)
        self.cookies_help_btn.setAutoFillBackground(False)
        self.cookies_help_btn.setStyleSheet("QPushButton{\n"
"    border-width: 2px;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.cookies_help_btn.setAutoDefault(False)
        self.cookies_help_btn.setObjectName("cookies_help_btn")
        self.horizontalLayout_3.addWidget(self.cookies_help_btn)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.cookies_input = QtWidgets.QTextEdit(self.new_scan_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookies_input.sizePolicy().hasHeightForWidth())
        self.cookies_input.setSizePolicy(sizePolicy)
        self.cookies_input.setMaximumSize(QtCore.QSize(16777215, 210))
        self.cookies_input.setObjectName("cookies_input")
        self.verticalLayout_9.addWidget(self.cookies_input)
        self.result_line = QtWidgets.QFrame(self.new_scan_page)
        self.result_line.setEnabled(True)
        self.result_line.setStyleSheet("color: rgb(255, 163, 26);")
        self.result_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result_line.setLineWidth(2)
        self.result_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.result_line.setObjectName("result_line")
        self.verticalLayout_9.addWidget(self.result_line)
        self.result_text = QtWidgets.QLabel(self.new_scan_page)
        self.result_text.setEnabled(True)
        self.result_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(17)
        self.result_text.setFont(font)
        self.result_text.setObjectName("result_text")
        self.verticalLayout_9.addWidget(self.result_text)
        self.scan_result = QtWidgets.QTextBrowser(self.new_scan_page)
        self.scan_result.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_result.sizePolicy().hasHeightForWidth())
        self.scan_result.setSizePolicy(sizePolicy)
        self.scan_result.setMinimumSize(QtCore.QSize(0, 0))
        self.scan_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scan_result.setObjectName("scan_result")
        self.verticalLayout_9.addWidget(self.scan_result)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_scan_btn = QtWidgets.QPushButton(self.new_scan_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_scan_btn.sizePolicy().hasHeightForWidth())
        self.save_scan_btn.setSizePolicy(sizePolicy)
        self.save_scan_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.save_scan_btn.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_scan_btn.setFont(font)
        self.save_scan_btn.setAutoFillBackground(False)
        self.save_scan_btn.setStyleSheet("QPushButton{\n"
"    border-width: 3px;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.save_scan_btn.setAutoDefault(False)
        self.save_scan_btn.setObjectName("save_scan_btn")
        self.horizontalLayout_4.addWidget(self.save_scan_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.read_scan_btn = QtWidgets.QPushButton(self.new_scan_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_scan_btn.sizePolicy().hasHeightForWidth())
        self.read_scan_btn.setSizePolicy(sizePolicy)
        self.read_scan_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.read_scan_btn.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.read_scan_btn.setFont(font)
        self.read_scan_btn.setAutoFillBackground(False)
        self.read_scan_btn.setStyleSheet("QPushButton{\n"
"    border-width: 3px;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.read_scan_btn.setAutoDefault(False)
        self.read_scan_btn.setObjectName("read_scan_btn")
        self.horizontalLayout_4.addWidget(self.read_scan_btn)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.line_14 = QtWidgets.QFrame(self.new_scan_page)
        self.line_14.setEnabled(True)
        self.line_14.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(2)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_9.addWidget(self.line_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.scan_progress_bar = QtWidgets.QProgressBar(self.new_scan_page)
        self.scan_progress_bar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_progress_bar.sizePolicy().hasHeightForWidth())
        self.scan_progress_bar.setSizePolicy(sizePolicy)
        self.scan_progress_bar.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        self.scan_progress_bar.setFont(font)
        self.scan_progress_bar.setProperty("value", 3)
        self.scan_progress_bar.setTextVisible(False)
        self.scan_progress_bar.setObjectName("scan_progress_bar")
        self.horizontalLayout_7.addWidget(self.scan_progress_bar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.line_2 = QtWidgets.QFrame(self.new_scan_page)
        self.line_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vuln_txt = QtWidgets.QLabel(self.new_scan_page)
        self.vuln_txt.setEnabled(True)
        self.vuln_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(17)
        self.vuln_txt.setFont(font)
        self.vuln_txt.setObjectName("vuln_txt")
        self.verticalLayout_10.addWidget(self.vuln_txt)
        self.scrollArea = QtWidgets.QScrollArea(self.new_scan_page)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 404, 506))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.xss_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.xss_box.setEnabled(True)
        self.xss_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.xss_box.setFont(font)
        self.xss_box.setStyleSheet("")
        self.xss_box.setIconSize(QtCore.QSize(16, 16))
        self.xss_box.setCheckable(True)
        self.xss_box.setChecked(True)
        self.xss_box.setAutoRepeat(False)
        self.xss_box.setAutoExclusive(False)
        self.xss_box.setTristate(False)
        self.xss_box.setObjectName("xss_box")
        self.verticalLayout_11.addWidget(self.xss_box)
        self.sql_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.sql_box.setEnabled(True)
        self.sql_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.sql_box.setFont(font)
        self.sql_box.setStyleSheet("")
        self.sql_box.setIconSize(QtCore.QSize(16, 16))
        self.sql_box.setCheckable(True)
        self.sql_box.setChecked(True)
        self.sql_box.setAutoRepeat(False)
        self.sql_box.setAutoExclusive(False)
        self.sql_box.setTristate(False)
        self.sql_box.setObjectName("sql_box")
        self.verticalLayout_11.addWidget(self.sql_box)
        self.cmd_injection_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.cmd_injection_box.setEnabled(True)
        self.cmd_injection_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.cmd_injection_box.setFont(font)
        self.cmd_injection_box.setStyleSheet("")
        self.cmd_injection_box.setIconSize(QtCore.QSize(16, 16))
        self.cmd_injection_box.setCheckable(True)
        self.cmd_injection_box.setChecked(True)
        self.cmd_injection_box.setAutoRepeat(False)
        self.cmd_injection_box.setAutoExclusive(False)
        self.cmd_injection_box.setTristate(False)
        self.cmd_injection_box.setObjectName("cmd_injection_box")
        self.verticalLayout_11.addWidget(self.cmd_injection_box)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_13.setEnabled(True)
        self.line_13.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_11.addWidget(self.line_13)
        self.select_all_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.select_all_box.setEnabled(True)
        self.select_all_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.select_all_box.setFont(font)
        self.select_all_box.setStyleSheet("")
        self.select_all_box.setIconSize(QtCore.QSize(16, 16))
        self.select_all_box.setCheckable(True)
        self.select_all_box.setChecked(True)
        self.select_all_box.setAutoRepeat(False)
        self.select_all_box.setAutoExclusive(False)
        self.select_all_box.setTristate(False)
        self.select_all_box.setObjectName("select_all_box")
        self.verticalLayout_11.addWidget(self.select_all_box)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scan_help_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_help_btn.sizePolicy().hasHeightForWidth())
        self.scan_help_btn.setSizePolicy(sizePolicy)
        self.scan_help_btn.setMinimumSize(QtCore.QSize(35, 0))
        self.scan_help_btn.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.scan_help_btn.setFont(font)
        self.scan_help_btn.setAutoFillBackground(False)
        self.scan_help_btn.setStyleSheet("QPushButton{\n"
"    border-width: 2px;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.scan_help_btn.setAutoDefault(False)
        self.scan_help_btn.setObjectName("scan_help_btn")
        self.horizontalLayout_6.addWidget(self.scan_help_btn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.start_scan_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.start_scan_btn.setEnabled(True)
        self.start_scan_btn.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        self.start_scan_btn.setFont(font)
        self.start_scan_btn.setStyleSheet("background-color: rgb(255, 163, 26);")
        self.start_scan_btn.setFlat(False)
        self.start_scan_btn.setObjectName("start_scan_btn")
        self.horizontalLayout_6.addWidget(self.start_scan_btn)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.new_scan_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setObjectName("history_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.history_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.history_title = QtWidgets.QLabel(self.history_page)
        self.history_title.setEnabled(True)
        self.history_title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(30)
        self.history_title.setFont(font)
        self.history_title.setStyleSheet("")
        self.history_title.setAlignment(QtCore.Qt.AlignCenter)
        self.history_title.setObjectName("history_title")
        self.verticalLayout_3.addWidget(self.history_title)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.date_title = QtWidgets.QLabel(self.history_page)
        self.date_title.setEnabled(True)
        self.date_title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(30)
        self.date_title.setFont(font)
        self.date_title.setStyleSheet("")
        self.date_title.setAlignment(QtCore.Qt.AlignCenter)
        self.date_title.setObjectName("date_title")
        self.verticalLayout_4.addWidget(self.date_title)
        self.date_combo = QtWidgets.QComboBox(self.history_page)
        self.date_combo.setObjectName("date_combo")
        self.date_combo.addItem("")
        self.verticalLayout_4.addWidget(self.date_combo)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.get_scan_history_btn = QtWidgets.QPushButton(self.history_page)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(22)
        self.get_scan_history_btn.setFont(font)
        self.get_scan_history_btn.setStyleSheet("QPushButton{\n"
"    border-width: 3px;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 163, 26);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"        background-color: rgb(255, 255, 255);\n"
"}")
        self.get_scan_history_btn.setObjectName("get_scan_history_btn")
        self.verticalLayout_4.addWidget(self.get_scan_history_btn)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.history_page)
        self.line_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("color: rgb(255, 163, 26);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_9.addWidget(self.line_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.saved_scan_result_title = QtWidgets.QLabel(self.history_page)
        self.saved_scan_result_title.setEnabled(True)
        self.saved_scan_result_title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(30)
        self.saved_scan_result_title.setFont(font)
        self.saved_scan_result_title.setStyleSheet("")
        self.saved_scan_result_title.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_scan_result_title.setObjectName("saved_scan_result_title")
        self.verticalLayout_5.addWidget(self.saved_scan_result_title)
        self.history_scan_result = QtWidgets.QTextBrowser(self.history_page)
        self.history_scan_result.setObjectName("history_scan_result")
        self.verticalLayout_5.addWidget(self.history_scan_result)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.history_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ===ADDED CODE===
        # Setting the username at the bottom to the signed-in username
        self.account_username.setText(client.get_username())

        # Hiding all the scan result related elements
        self.hide_reset_scan_elements()

        # =Buttons=
        # Page passing
        self.scan_page_btn.clicked.connect(self.load_new_scan_page)

        # Start scan
        self.result = ""
        self.saved_scan_id = ""
        self.scan_id = ""
        self.scanning = False
        if not self.scanning:
                self.start_scan_btn.clicked.connect(self.send_scan_request)

        # Select all Check box
        self.boxes = {self.xss_box: vuln.XSS, self.sql_box: vuln.SQL_INJECTION,
                      self.cmd_injection_box: vuln.CMD_INJECTION}
        self.select_all_box.clicked.connect(self.select_all)

        # Cookies help
        self.cookies_help_btn.clicked.connect(self.cookies_help_popup)

        # Scan help
        self.scan_help_btn.clicked.connect(self.scan_help_popup)

        # Read scan results
        self.read_scan_btn.clicked.connect(self.read_more_scan_popup)

        # Save scan results
        self.save_scan_btn.clicked.connect(self.send_save_scan_results)

        # Fetch all saved dates
        self.history_page_btn.clicked.connect(self.fetch_all_saved_dates)

        # Get scan history
        self.get_scan_history_btn.clicked.connect(self.send_scan_history_request)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scan_page_btn.setText(_translate("MainWindow", "New Scan"))
        self.history_page_btn.setText(_translate("MainWindow", "History"))
        self.learn_more_page_btn.setText(_translate("MainWindow", "Lean More"))
        self.settings_btn.setText(_translate("MainWindow", "..."))
        self.account_username.setText(_translate("MainWindow", "-"))
        self.welcome_txt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Copperplate Gothic Bold\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Welcome</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">To</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Xploit Hub</span></p></body></html>"))
        self.scan_title.setText(_translate("MainWindow", "New Scan"))
        self.url_txt.setText(_translate("MainWindow", "URL:"))
        self.cookies_text.setText(_translate("MainWindow", "Cookies:"))
        self.cookies_help_btn.setText(_translate("MainWindow", "?"))
        self.result_text.setText(_translate("MainWindow", "Result:"))
        self.scan_result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.save_scan_btn.setText(_translate("MainWindow", "Save"))
        self.read_scan_btn.setText(_translate("MainWindow", "Read More"))
        self.vuln_txt.setText(_translate("MainWindow", "vulnerabilities:"))
        self.xss_box.setText(_translate("MainWindow", "xss"))
        self.sql_box.setText(_translate("MainWindow", "SQL Injection"))
        self.cmd_injection_box.setText(_translate("MainWindow", "Command Injection"))
        self.select_all_box.setText(_translate("MainWindow", "Select All"))
        self.scan_help_btn.setText(_translate("MainWindow", "?"))
        self.start_scan_btn.setText(_translate("MainWindow", "Scan"))
        self.history_title.setText(_translate("MainWindow", "History"))
        self.date_title.setText(_translate("MainWindow", "Pick date"))
        self.date_combo.setItemText(0, _translate("MainWindow", "-pick a date to show-"))
        self.get_scan_history_btn.setText(_translate("MainWindow", "Get Result"))
        self.saved_scan_result_title.setText(_translate("MainWindow", "Scan result"))



# ===ADDED CODE===
    def load_new_scan_page(self):
        self.stackedWidget.setCurrentWidget(self.new_scan_page)


    # Set all the checkboxes to that of the select all
    def select_all(self):
        state = self.select_all_box.checkState()
        for box in self.boxes.keys():
            box.setCheckState(state)

    # Hide all scan result elements
    def hide_reset_scan_elements(self):
        self.scan_result.clear()
        self.result_line.hide()
        self.result_text.hide()
        self.save_scan_btn.hide()
        self.read_scan_btn.hide()
        self.scan_progress_bar.hide()

    def scan_help_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Scan Help")
        msg.setText("Welcome to the scan page.\n"
                    "To start a scan enter the URL for the website page to scan\n"
                    "and pick the vulnerabilities to scan on the website.\n"
                    "After the scan has finished you can choose to read more about\n"
                    "the scan results, save the scan results, or start a new scan.")
        msg.setInformativeText("Additionally you can choose to add your cookies to\n"
                               "the scan for pages that require that.\n"
                               "(more on that on the cookies ? button)")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def cookies_help_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Cookies Help")
        msg.setText("You can insert your cookies for the scanned website (not required).\n"
                    "using cookies will let the scanner use the website as you have it.")
        msg.setInformativeText('You can only get valid cookies using the "EditThisCookie" Chrome extension')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


    def read_more_scan_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Scan Results")
        msg.setText(self.result)
        msg.exec_()

    def general_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()


    # Send the scan results back to server for saving it
    def send_save_scan_results(self):
        if self.scan_id != self.saved_scan_id:
            client.send_data_list(cmds.SAVE_SCAN_CMD, [self.scan_id, self.result])
            self.saved_scan_id = self.scan_id


            start = time.time()
            while time.time() - start < constants.RESPONSE_WAIT_TIMEOUT:
                data = client.receive_data()
                if data is not None:
                    if data.pop(0) == cmds.SAVE_SCAN_CMD:
                        _, msg = data

                        self.general_popup('Scan Results', msg)
                        break


    # Fetch all saved scan dates and time, and update the history page
    def fetch_all_saved_dates(self):
        # Load the history page first
        self.stackedWidget.setCurrentWidget(self.history_page)

        # Clear the date combobox options and add the default one
        self.date_combo.clear()
        self.date_combo.addItem(constants.DATE_COMBOBOX_MSG)

        client.send_data_list(cmds.GET_ALL_SAVED_DATES_CMD, [])

        start = time.time()
        while time.time() - start < constants.RESPONSE_WAIT_TIMEOUT:
            data = client.receive_data()
            if data is not None:
                if data.pop(0) == cmds.GET_ALL_SAVED_DATES_CMD:
                    fetched = data.pop(0)

                    if fetched:
                        # what's only left in the data are the fetched dates
                        for date in data:
                            self.date_combo.addItem(date)
                    else:
                        self.general_popup("history", data[0])

                    break


    def send_scan_history_request(self):
        date_time = self.date_combo.currentText()

        if date_time == constants.DATE_COMBOBOX_MSG:
            self.general_popup("Date-Time", errors.NO_DATE_PICKED)
            return

        client.send_data_list(cmds.GET_SAVED_SCAN_CMD, [date_time])

        start = time.time()
        while time.time() - start < constants.RESPONSE_WAIT_TIMEOUT:
            data = client.receive_data()
            if data is not None:
                if data.pop(0) == cmds.GET_SAVED_SCAN_CMD:
                    fetched = data.pop(0)

                    if fetched:
                        # what's only left in the data is the saved scan result
                        result = data[0]
                        self.history_scan_result.setText(result)
                    else:
                        self.general_popup("history", data[0])

                    break

    def send_scan_request(self):
        # Generate a random and long scan id
        self.scan_id = str(random.randint(10000000, 99999999))
        self.start_scan_btn.hide()

        self.result = ""
        self.hide_reset_scan_elements()

        self.scan_progress_bar.show()
        self.result_line.show()
        self.result_text.show()

        self.scan_progress_bar.setValue(3)
        url = self.url_input.text()
        cookies = self.cookies_input.toPlainText()
        msg = [url, cookies]
        vuln_list = []

        page_vulnerable = False

        for box in self.boxes.keys():
            if box.isChecked():
                vuln_list.append(self.boxes[box])

        msg = msg + vuln_list
        num_of_vuln = len(vuln_list)

        if url != "" and num_of_vuln > 0:
            client.send_data_list(cmds.NEW_SCAN_CMD, msg)

            # scan_wait = threading.Thread(target=self.wait_for_scan_result, args=(vuln_list,))
            # scan_wait.start()

            start = time.time()
            while time.time() - start < constants.RESPONSE_WAIT_TIMEOUT and len(vuln_list) > 0:
                data = client.receive_data()
                if data is not None:
                    # Check if
                    print(data)
                    if data.pop(0) == cmds.NEW_SCAN_CMD and data.pop(0):
                        vuln_type = data.pop(0)
                        vuln_found = data.pop(0)

                        vuln_list.remove(vuln_type)
                        self.scan_progress_bar.setValue(int(round(100 - (100 / num_of_vuln) * len(vuln_list))))

                        if vuln_found:
                            msg = "Vulnerable"
                            page_vulnerable = True

                            self.result += msg +"\n"
                            self.result += "URL: " + url + "\n"
                            self.result += "-" + vuln_type + "-\n"

                            for form_details in data:
                                self.result += form_details + "\n"
                            self.result += "\n"

                        else:
                            msg = "Secure"

                        self.scan_result.append(vuln_type + ": " + msg)
                    else:
                        error = data[-1]
                        self.scan_progress_bar.setValue(100)
                        self.scan_result.setText(error)
                        break

            if page_vulnerable:
                self.scan_result.append("Website not secured!")
                self.save_scan_btn.show()
                self.read_scan_btn.show()
                print(self.result)
            else:
                self.scan_result.append("Website secured.")

        self.start_scan_btn.show()




    # def wait_for_scan_result(self, vuln_list):
    #     num_of_vuln = len(vuln_list)
    #     start = time.time()
    #     while time.time() - start < constants.RESPONSE_WAIT_TIMEOUT and len(vuln_list) > 0:
    #         data = client.receive_data()
    #         if data is not None:
    #             # Check if
    #             print(data)
    #             if data.pop(0) == cmds.NEW_SCAN_CMD and data.pop(0):
    #                 vuln_type, vuln_found, details = data
    #                 vuln_list.remove(vuln_type)
    #                 self.scan_progress_bar.setValue(int(round(100 - (100 / num_of_vuln) * len(vuln_list))))
    #
    #                 if vuln_found:
    #                     msg = "Vulnerable"
    #                 else:
    #                     msg = "Secure"
    #
    #                 print("=set bar=")
    #                 self.scan_result.setText(vuln_type + ": " + msg)
    #                 print("=set text=")
    #             else:
    #                 error = data
    #                 self.scan_progress_bar.setValue(100)
    #                 self.scan_result.setText(error)
    #                 break



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
