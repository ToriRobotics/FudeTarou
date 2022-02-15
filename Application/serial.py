import serial
from threading import Thread
import math

class readSerial(Thread):
    def __init__(self):
        self.accX:float=0.0
        self.accY:float=0.0
        self.accZ:float=0.0

    def loop(self):
        try:
            while True:
                self.EulerAngle(accX=self.accX, accY=self.accY, accZ=self.accZ)
        except:
            return
    
    def read(self):
        print("noma")

    def EulerAngle(self, accX:float, accY:float, accZ:float)->list:
        angleX=math.atan(-accY/-accZ)
        angleY=math.atan(accX/math.sqrt(math.pow(accY,2)+math.pow(accZ,2)))

        angle:list=[angleX,angleY]
        return(angle)