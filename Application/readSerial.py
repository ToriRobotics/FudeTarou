import string
import serial
from threading import Thread
import math
import os

class getAngle(Thread):
    def __init__(self):
        super().__init__()
        self.accX:float=0.0
        self.accY:float=0.0
        self.accZ:float=0.0

        self.rawData = [0, 0, 0]

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        '''
        for file in os.listdir("/dev"):
            if "tty.usbmodem" in file:
                self.ser.port = "/dev/"+file
                self.ser.open()
        '''

        self.ser.port = "/dev/cu.usbserial-14330"
        self.ser.open()
        #line=0.0 0.0 0.0 0.0 0.0 0.0


    def run(self):
        try:
            while True:
                line=self.ser.readline()
                self.rawData=line.split()
                self.rawData = [int(i) for i in self.rawData]
                #print(rawData)
                #self.EulerAngle(accX=rowData[0], accY=rowData[1], accZ=rowData[2])
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return



    def EulerAngle(self, accX:float, accY:float, accZ:float)->list:
        angleX=math.atan(-accY/-accZ)
        angleY=math.atan(accX/math.sqrt(math.pow(accY,2)+math.pow(accZ,2)))

        angle:list=[angleX,angleY]
        return(angle)