#-*- coding: utf-8 -*-
from serial import Serial
from serial.tools import list_ports 
from binascii import b2a_hex as str2int
from binascii import a2b_hex as int2str

def List2Str(str_list):
    str_temp = ''
    for x in str_list:
        temp  =hex(x)[2:]
        if len(temp) == 1:
            temp = '0'+temp
        str_temp+=int2str(temp)
    return str_temp

class Uart(Serial):
    def __init__(self,baudrate = 57600,timeout = 0.05):
        Serial.__init__(self)
        self.setBaudrate(baudrate)
        self.setTimeout(timeout)
        self.GetFreePort()
        
    def GetFreePort(self):
        self.freeport = list(list_ports.comports())
        return self.freeport
    def SetPortAuto(self):
        self.GetFreePort()
        if self.freeport:
            self.port  = self.freeport[0][0]
            self.close()
            return True
        else:
            return False
     
    def ReSetPort(self,port,baudrate):
        self.port = port
        self.baudrate = baudrate

    def GetData(self):
        data = ""
        while True:
            b = self.read()
            if b == '' and  data:
                return data
            else:
                        data += b
        
        
                
if __name__ == "__main__":
    a = Uart()
    a.SetPortAuto()
    a.open()
    for x in range(100):
        a.read()
    List2Str([1,2,3])
    '''while(True):
        b = str2int(a.read())
        if b != '':
            print int(b,16)'''