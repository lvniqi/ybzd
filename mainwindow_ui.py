# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun May 03 00:17:57 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(723, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("joypad.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName(_fromUtf8(""))
        MainWindow.setStyleSheet(_fromUtf8("*{   \n"
"  font-size:10.5pt;   \n"
"  color:white;   \n"
"  font-family:\"Microsoft YaHei UI\";   \n"
"}\n"
"QMenuBar\n"
"{\n"
"    background: transparent;\n"
"    color: silver;\n"
"    \n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"    \n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
";\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"    margin-bottom:1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    background-color: #010101;\n"
"    \n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"    \n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"}\n"
"   \n"
"CallWidget QLineEdit#telEdt  \n"
"{   \n"
"  font-size:24px;   \n"
"}   \n"
"QMainWindow,QDialog{   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #1B2534, stop: 0.4 #010101,   \n"
"                                 stop: 0.5 #000101, stop: 1.0 #1F2B3C);   \n"
"}   \n"
"QWidget{   \n"
"    background:#121922;   \n"
"}   \n"
"QLabel{   \n"
"   background:transparent;   \n"
"}   \n"
"DailForm QLineEdit#phoneLineEdt{   \n"
"  font-size:36px;   \n"
"  font-weight: bold;   \n"
"}   \n"
"QPushButton,QToolButton{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);  \n"
"    border-style: outset;  \n"
"    border-width: 1px;   \n"
"    border-radius: 5px;   \n"
"    border-color: #11223F;   \n"
"    padding: 1px;   \n"
"    min-width: 2em;\n"
"}   \n"
"QPushButton::hover,QToolButton::hover{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #313C4F); \n"
"    border-color: #5D8B9E;  \n"
"    \n"
"}   \n"
"QPushButton::pressed,QToolButton::pressed{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    color: white;\n"
"    border-color: #5D8B9E;   \n"
"}   \n"
"QPushButton::disabled,QToolButton::disabled{   \n"
"    background: rgb(10, 10,10);\n"
"    border-color: #0A1320;   \n"
"    color:#6A6864;   \n"
"}   \n"
"QDialog QPushButton,QDialog QToolButton{   \n"
"  min-width:30px;   \n"
"  min-height:23px;   \n"
"}   \n"
"QToolButton[objectName=\"minimizeToolBtn\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/minimize.png)*/\n"
"}   \n"
"QToolButton[objectName=\"minimizeToolBtn\"]:hover,QToolButton[objectName=\"minimizeToolBtn\"]:pressed {   \n"
"    /*image:url(qss/minimize_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"maximizeToolBtn\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/maximize.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"maximizeToolBtn\"]:hover,QToolButton[objectName=\"maximizeToolBtn\"]:pressed {   \n"
"    /*image:url(qss/maximize_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"closeToolBtn\"],QToolButton[objectName=\"customCloseWindow\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/close.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"closeToolBtn\"]:hover,QToolButton[objectName=\"closeToolBtn\"]:pressed{   \n"
"    /*image:url(qss/close_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"customCloseWindow\"]:hover,QToolButton[objectName=\"customCloseWindow\"]:pressed{   \n"
"    /*image:url(qss/close_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"titleSetUpToolBtn\"]{   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/setup.png)*/   \n"
"}   \n"
"DailForm QToolButton#oneToolBtn,QToolButton#OneToolBtn,QToolButton#twoToolBtn,QToolButton#threeToolBtn,   \n"
"         QToolButton#fourToolBtn,QToolButton#fiveToolBtn,QToolButton#sixToolBtn,   \n"
"         QToolButton#sevenToolBtn,QToolButton#eightToolBtn,QToolButton#nineToolBtn,   \n"
"         QToolButton#starToolBtn,QToolButton#zeroToolBtn,QToolButton#sharpToolBtn {   \n"
"    font-size:36px;   \n"
"    border-radius: 10px;   \n"
"}   \n"
"DailForm QToolButton#delToolBtn{   \n"
"    border-radius: 10px;   \n"
"}   \n"
"QFrame{   \n"
"    border-color:#32435E;   \n"
"    border-width:1px;   \n"
"    border-radius: 3px;   \n"
"}   \n"
"QLineEdit,QTextEdit {   \n"
"    border: 1px solid #32435E;   \n"
"    border-radius: 3px;   \n"
"    /* padding: 0 8px; */  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"    selection-background-color: #0A246A;   \n"
"}   \n"
"QLineEdit::hover{   \n"
"  border-color:#5D8B9E;   \n"
"}   \n"
"QLineEdit[echoMode=\"3\"] {   \n"
"     lineedit-password-character: 9679;   \n"
"}   \n"
"#QLineEdit:read-only {   \n"
"     background: #543F7C;   \n"
"}   \n"
"QTabWidget::pane { /* The tab widget frame */  \n"
"     border: 1px solid #ffffff;   \n"
"     position: absolute;    \n"
"}   \n"
"QTabWidget#MainTabWidget::tab-bar {   \n"
"     left: -3px; /* move to the right by 5px */  \n"
"}   \n"
"QTabWidget#MainTabWidget QTabBar::tab {   \n"
"     height: 14ex;   \n"
"     width: 14ex;   \n"
"}   \n"
"QTabBar::tab {   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);  \n"
"}   \n"
"QTabBar::tab:selected{   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    \n"
"}   \n"
"QTabBar::tab:hover {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #313C4F); \n"
"    \n"
"}\n"
"QTabBar::tab:pressed{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    color: white;\n"
"    border-color: #5D8B9E;   \n"
"}     \n"
"#QTabBar::tab:selected {   \n"
"     border-color: #32435E;   \n"
"     border-right-color: #32435E; /* same as pane color */  \n"
"}   \n"
"#QTabBar::tab:!selected {   \n"
"     margin-left: 2px; /* make non-selected tabs look smaller */  \n"
"}   \n"
"#QTabBar:tab:first:selected {   \n"
"    margin-top: 0;   \n"
"}   \n"
"QTabBar:tab:last:selected {   \n"
"    margin-right: 0;   \n"
"}   \n"
"QTabBar:tab:only-one {   \n"
"     margin: 0;   \n"
"}   \n"
"QListWidget{   \n"
"    border: 1px solid #32435E;   \n"
"    background:#050609;   \n"
"}   \n"
"QListWidget::item:selected {   \n"
"     /*border: 0px solid #33CCFF;*/  \n"
"     border:none;   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #6A848C,  stop: 1.0 #0F9EAF);   \n"
"     padding:0px;   \n"
"     margin:0px;   \n"
"}   \n"
"#QListWidget::item:selected:!active {   \n"
"     border-width: 0px ;   \n"
"}   \n"
"#QListWidget::item:selected:active {   \n"
"     border-width: 1px;   \n"
"}   \n"
"  \n"
"QComboBox {   \n"
"     border: 1px solid #32435E;   \n"
"     border-radius: 3px;   \n"
"     padding: 1px 18px 1px 3px;   \n"
"     min-width: 6em;   \n"
"}   \n"
"QComboBox::hover{   \n"
"  border-color:#5D8B9E;   \n"
"}   \n"
"QComboBox:editable {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"}   \n"
"QComboBox:!editable, QComboBox::drop-down:editable {   \n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"}   \n"
"/* QComboBox gets the \"on\" state when the popup is open */  \n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);;   \n"
"}   \n"
"QComboBox:on { /* shift the text when the popup opens */  \n"
"     padding-top: 3px;   \n"
"     padding-left: 4px;   \n"
"}   \n"
"QComboBox::drop-down {   \n"
"     subcontrol-origin: padding;   \n"
"     subcontrol-position: top right;   \n"
"     width: 15px;   \n"
"     border-left-width: 1px;   \n"
"     border-left-color: 32435E;   \n"
"     border-left-style: solid; /* just a single line */  \n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */  \n"
"     border-bottom-right-radius: 3px;   \n"
"}   \n"
"QComboBox::down-arrow {   \n"
"     /*image: url(qss/downarrow.png);*/ \n"
"     \n"
"}   \n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */  \n"
"     top: 1px;   \n"
"     left: 1px;   \n"
"}   \n"
"QComboBox QAbstractItemView {   \n"
"     border: 2px solid #32435E;   \n"
"     selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #506B79,   \n"
"                                 stop: 1.0 #0D95A6);   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #1B2534, stop: 0.4 #010101,   \n"
"                                 stop: 0.5 #000101, stop: 1.0 #1F2B3C);   \n"
"} "))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 0, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.box_7 = QtGui.QPushButton(self.centralwidget)
        self.box_7.setMinimumSize(QtCore.QSize(44, 100))
        self.box_7.setObjectName(_fromUtf8("box_7"))
        self.gridLayout.addWidget(self.box_7, 2, 0, 1, 3)
        self.box_8 = QtGui.QPushButton(self.centralwidget)
        self.box_8.setMinimumSize(QtCore.QSize(44, 100))
        self.box_8.setObjectName(_fromUtf8("box_8"))
        self.gridLayout.addWidget(self.box_8, 2, 3, 1, 3)
        self.box_3 = QtGui.QPushButton(self.centralwidget)
        self.box_3.setMinimumSize(QtCore.QSize(44, 100))
        self.box_3.setBaseSize(QtCore.QSize(0, 0))
        self.box_3.setObjectName(_fromUtf8("box_3"))
        self.gridLayout.addWidget(self.box_3, 0, 4, 1, 2)
        self.box_2 = QtGui.QPushButton(self.centralwidget)
        self.box_2.setMinimumSize(QtCore.QSize(44, 100))
        self.box_2.setObjectName(_fromUtf8("box_2"))
        self.gridLayout.addWidget(self.box_2, 0, 2, 1, 2)
        self.box_6 = QtGui.QPushButton(self.centralwidget)
        self.box_6.setMinimumSize(QtCore.QSize(44, 100))
        self.box_6.setObjectName(_fromUtf8("box_6"))
        self.gridLayout.addWidget(self.box_6, 1, 4, 1, 2)
        self.box_5 = QtGui.QPushButton(self.centralwidget)
        self.box_5.setMinimumSize(QtCore.QSize(44, 100))
        self.box_5.setObjectName(_fromUtf8("box_5"))
        self.gridLayout.addWidget(self.box_5, 1, 2, 1, 2)
        self.box_1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_1.sizePolicy().hasHeightForWidth())
        self.box_1.setSizePolicy(sizePolicy)
        self.box_1.setMinimumSize(QtCore.QSize(44, 100))
        self.box_1.setObjectName(_fromUtf8("box_1"))
        self.gridLayout.addWidget(self.box_1, 0, 0, 1, 2)
        self.box_4 = QtGui.QPushButton(self.centralwidget)
        self.box_4.setMinimumSize(QtCore.QSize(44, 100))
        self.box_4.setObjectName(_fromUtf8("box_4"))
        self.gridLayout.addWidget(self.box_4, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_close = QtGui.QAction(MainWindow)
        self.action_close.setObjectName(_fromUtf8("action_close"))
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_uart = QtGui.QAction(MainWindow)
        self.action_uart.setObjectName(_fromUtf8("action_uart"))
        self.menu.addAction(self.action_uart)
        self.menu.addSeparator()
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_close, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "智能邮包终端", None))
        self.box_7.setText(_translate("MainWindow", "盒子7", None))
        self.box_8.setText(_translate("MainWindow", "盒子8", None))
        self.box_3.setText(_translate("MainWindow", "盒子3", None))
        self.box_2.setText(_translate("MainWindow", "盒子2", None))
        self.box_6.setText(_translate("MainWindow", "盒子6", None))
        self.box_5.setText(_translate("MainWindow", "盒子5", None))
        self.box_1.setText(_translate("MainWindow", "盒子1", None))
        self.box_4.setText(_translate("MainWindow", "盒子4", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_3.setTitle(_translate("MainWindow", "关于", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_close.setText(_translate("MainWindow", "关闭", None))
        self.action_save.setText(_translate("MainWindow", "保存", None))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_uart.setText(_translate("MainWindow", "串口设置", None))

