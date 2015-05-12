# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uart_dialog.ui'
#
# Created: Sun May 03 00:17:13 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(249, 114)
        Form.setMaximumSize(QtCore.QSize(16777215, 150))
        Form.setStyleSheet(_fromUtf8("*{   \n"
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
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label32_11 = QtGui.QLabel(Form)
        self.label32_11.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.label32_11.setFont(font)
        self.label32_11.setObjectName(_fromUtf8("label32_11"))
        self.horizontalLayout_16.addWidget(self.label32_11)
        self.comboBox_baudrate = QtGui.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.comboBox_baudrate.setFont(font)
        self.comboBox_baudrate.setObjectName(_fromUtf8("comboBox_baudrate"))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.comboBox_baudrate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_242 = QtGui.QLabel(Form)
        self.label_242.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.label_242.setFont(font)
        self.label_242.setObjectName(_fromUtf8("label_242"))
        self.horizontalLayout_18.addWidget(self.label_242)
        self.comboBox_com = QtGui.QComboBox(Form)
        self.comboBox_com.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.comboBox_com.setFont(font)
        self.comboBox_com.setObjectName(_fromUtf8("comboBox_com"))
        self.horizontalLayout_18.addWidget(self.comboBox_com)
        self.pushButton_com = QtGui.QPushButton(Form)
        self.pushButton_com.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.pushButton_com.setFont(font)
        self.pushButton_com.setObjectName(_fromUtf8("pushButton_com"))
        self.horizontalLayout_18.addWidget(self.pushButton_com)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.pushButton_collect = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.pushButton_collect.setFont(font)
        self.pushButton_collect.setObjectName(_fromUtf8("pushButton_collect"))
        self.horizontalLayout_19.addWidget(self.pushButton_collect)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label32_11.setText(_translate("Form", "波特率", None))
        self.comboBox_baudrate.setItemText(0, _translate("Form", "115200", None))
        self.comboBox_baudrate.setItemText(1, _translate("Form", "57600", None))
        self.comboBox_baudrate.setItemText(2, _translate("Form", "19200", None))
        self.comboBox_baudrate.setItemText(3, _translate("Form", "9600", None))
        self.label_242.setText(_translate("Form", "串口", None))
        self.pushButton_com.setText(_translate("Form", "扫描", None))
        self.pushButton_collect.setText(_translate("Form", "开启串口", None))

