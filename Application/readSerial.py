import string
import serial
from threading import Thread
import math

class getAngle(Thread):
    def __init__(self, port:str):
        self.accX:float=0.0
        self.accY:float=0.0
        self.accZ:float=0.0

        self.ser = serial.Serial(port, 9600, timeout=None)
        
        #line=0.0 0.0 0.0 0.0 0.0 0.0


    def run(self):
        try:
            while True:
                line=self.ser.readline()
                rowData=line.split()
                self.EulerAngle(accX=rowData[0], accY=rowData[1], accZ=rowData[2])
        except:
            return


    def EulerAngle(self, accX:float, accY:float, accZ:float)->list:
        angleX=math.atan(-accY/-accZ)
        angleY=math.atan(accX/math.sqrt(math.pow(accY,2)+math.pow(accZ,2)))

        angle:list=[angleX,angleY]
        return(angle)