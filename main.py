# -*- coding: utf-8 -*-
from mainwindow_ui import Ui_MainWindow,_translate
from PyQt4 import QtCore, QtGui
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import Qt
from time import ctime as getTime
import sys
BOX_LEN = 8
BOX_DATA_STR = [u"pos",u"姓名",u"电话",u"长度",u"宽度",u"重量"]
BOX_DATA_STR_LEN = 6
BOX_DATA_SPLIT = u"[DATAEND]"
#重设utf-8编码
sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('UTF-8')
sys.getdefaultencoding()
from uart_dialog import Uart_Widget
from serial.serialwin32 import SerialException
#线程 采集数据
class GettingUartData_Thread(QtCore.QThread):    
    def __init__(self,uart,parent=None):
        super(self.__class__, self).__init__(parent)
        self.stoped = False
        self.mutex = QtCore.QMutex()
        self.uart = uart
        self.getwrong_message = None
        
    def run(self):
        data  = None
        with QtCore.QMutexLocker(self.mutex):
            self.stoped = False
        
        try:
            self.uart.open()
        except SerialException,e:
            self.getwrong_message = e
            self.emit(QtCore.SIGNAL("UartData"), data,self.getwrong_message)
        while True:
            if self.stoped  == True:
                return
            try:
                data =   self.uart.GetData()
            except SerialException,e :
                self.getwrong_message = e
                if data:
                    self.emit(QtCore.SIGNAL("UartData"), data,self.getwrong_message)
            if data:  
                self.emit(QtCore.SIGNAL("UartData"), data,self.getwrong_message)
        
    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.uart.close()
            self.getwrong_message = None
            self.stoped = True
    
    def isStop(self):
        with QtCore.QMutexLocker(self.mutex):
            return self.stoped
        
class My_Box():
    def __init__(self,button):
        self.button = None
        if type(button) == QtGui.QPushButton:
            self.button = button
            self.information = None
            self.setEnable(None)
    def setEnable(self,information):
        if information:
            self.button.setEnabled(True)
            self.information = information
            self.button.setStyleSheet("""background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   
                                 stop: 0 #10080B,   
                                 stop: 1.0 #9F111C);""");
        else:
            self.button.setEnabled(False)
            self.information = None
            self.button.setStyleSheet("""
                                        background: rgb(10, 10,10);
                                        border-color: #0A1320;   
                                        color:#6A6864""");
    def getInformation(self):
        return self.information
    def printInformation(self):
        temp_str = u''
        for x in range(1,BOX_DATA_STR_LEN):
            pos = BOX_DATA_STR[x]
            temp_str += pos + u':' + str(self.information[pos])+u'\n'
            
        return temp_str
        
class Widget_Show(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self) # Ui_Form.setupUi
        self.textBrowser.setText(u"")
        self.cuurent_pos = 0;
        self.Uart_Widget = Uart_Widget()
        self.Uart_Widget.setModal(True)
        self.connect(self.action_uart, QtCore.SIGNAL("triggered()"), self.Uart_Widget.show)
        self.connect(self.action_open, QtCore.SIGNAL("triggered()"), self.openFile)
        self.connect(self.action_save, QtCore.SIGNAL("triggered()"), self.saveFile)
        self.my_box_array = []
        self.Uart_Widget.setCollectFunc(self.startCollectFunc)
        self.Uart_Widget.setStopCollectFunc(self.stopCollectFunc)
        for x in range(1,BOX_LEN+1):
            temp_box = eval("self.box_%d"%x)
            self.my_box_array.append(My_Box(temp_box))
        self.connect(eval("self.box_%d"%1),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(0))
        self.connect(eval("self.box_%d"%2),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(1))
        self.connect(eval("self.box_%d"%3),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(2))
        self.connect(eval("self.box_%d"%4),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(3))
        self.connect(eval("self.box_%d"%5),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(4))
        self.connect(eval("self.box_%d"%6),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(5))
        self.connect(eval("self.box_%d"%7),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(6))
        self.connect(eval("self.box_%d"%8),QtCore.SIGNAL("clicked()"),lambda:self.printInformation(7))
        self.Uart_Widget.show()
        self.file = None
        #self.addingData("0#1#2#3#4#5#6#",None)
    #开始采集回调函数     
    def startCollectFunc(self):
        #串口数据线程
        self.adddata  = GettingUartData_Thread(self.Uart_Widget.getUart())
        #采集串口数据
        self.connect(self.adddata, QtCore.SIGNAL("UartData"), self.addingData)
        self.adddata.start()
        print "start"
        
    #结束采集回调函数
    def stopCollectFunc(self):
        self.adddata.stop()
        if  self.adddata.isStop():
            self.disconnect(self.adddata, QtCore.SIGNAL("UartData"),
                                self.addingData)
        self.adddata.stop()
        self.adddata.quit()
        self.adddata.wait()
        self.adddata.deleteLater()
        
    #数据采集函数
    def addingData(self,data,message):
        if message:
            QtGui.QMessageBox.warning(self,u"串口错误",str(message))
            self.Uart_Widget.startCollect()
        self.data2List(self.processData(data))
        
    #数据采集处理函数
    def processData(self,data):
            #data = "0#1+f#"
            print data
            data_in = data.split('#')
            data_out = {}
            if data_in[0] == '0':
                if len(data_in)  == 8 :
                    data_out['mode'] = 'enable'
                    for x in range(0,BOX_DATA_STR_LEN):
                        if x == 0:
                            data_out[BOX_DATA_STR[x]] = int(data_in[1][0])
                        else:
                            data_out[BOX_DATA_STR[x]] = unicode(data_in[x+1],'gbk')
                    return data_out
                elif len(data_in)  == 3 and data_in[1][-1] == 'f':
                    data_out['mode'] = 'disable'
                    data_out[BOX_DATA_STR[0]] = int(data_in[1][0])
                    return data_out
            return None
            
    #将数据写入boxList
    def data2List(self,data):
        if data:
            if data['mode'] == 'enable':
                self.my_box_array[data[BOX_DATA_STR[0]]].setEnable(data)
            elif data['mode'] == 'disable':
                if self.cuurent_pos == data[BOX_DATA_STR[0]]:
                    self.textBrowser.setText("")
                self.my_box_array[data[BOX_DATA_STR[0]]].setEnable(None)
            #print data.count('#')
    #显示盒子信息        
    def printInformation(self,pos):
        self.cuurent_pos = pos
        self.textBrowser.setText(self.my_box_array[pos].printInformation())
        
    #打开文件 
    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,(u"打开文件"),"",u"Data Files(*.txt);;Else Files(*.*)")
        file = open(filename,'r')
        data =  file.read()
        SPLITED = data.split(BOX_DATA_SPLIT)
        SPLITED.reverse()
        for x in SPLITED:
            boxs = x.split("\n")
            for index in range(len(boxs)-1,-1,-1):
                if boxs[index] == u"":
                    boxs.pop(index)
            if len(boxs) == 9:
                for x in range(1,9):
                    temp_data =  eval(boxs[x])
                    if temp_data != None:
                        self.data2List(temp_data)
                    else:
                        self.data2List({BOX_DATA_STR[0]:x,'mode':'disable'})
                break
        
    #保存文件 
    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self,(u"打开文件"),"",u"Data Files(*.txt);;Else Files(*.*)")
        
        self.file = open(filename,'a+')
        print >>self.file, u"[%s]"%str(getTime())
        for x in range(BOX_LEN):
            print >>self.file, self.my_box_array[x].getInformation()
        print >>self.file, BOX_DATA_SPLIT
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = Widget_Show()
    #widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #widget.showFullScreen()
    widget.show()
    sys.exit(app.exec_())