import string
import serial
from threading import Thread
import math
import os


#musi,angle,stress,shearX,shearY,grip
class getAngle(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.accX:float=0.0
        self.accY:float=0.0
        self.accZ:float=0.0

        #musi,angle,stress,shearX,shearY,grip
        self.rawData:list[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        '''
        for file in os.listdir("/dev"):
            if "tty.usbmodem" in file:
                self.ser.port = "/dev/"+file
                self.ser.open()
        '''
        try:
            #self.ser.port = "/dev/cu.usbserial-14330"
            self.ser.port = "/dev/ttyUSB0"
            #self.ser.port = "/dev/cu.usbserial-143120"
            self.ser.open()
        except:
            return
        #line=0.0 0.0 0.0 0.0 0.0 0.0




    def run(self):
        try:
            while True:
                try:
                    #musi,angle,stress,shearX,shearY,grip
                    line=self.ser.readline().decode('utf-8')
                    base=line.split(" ")
                    self.rawData = [float(i) for i in base]
                    #print(self.rawData)
                    #self.EulerAngle(accX=rowData[0], accY=rowData[1], accZ=rowData[2])
                    #print(self.rawData)
                except:
                    import traceback
                    print(traceback.format_exc())
                    return
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            self.rawData=[0, 0, 0]
            return



    def EulerAngle(self, accX:float, accY:float, accZ:float)->list:
        angleX=math.atan(-accY/-accZ)
        angleY=math.atan(accX/math.sqrt(math.pow(accY,2)+math.pow(accZ,2)))

        angle:list=[angleX,angleY]
        return(angle)
