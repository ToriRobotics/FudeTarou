import string
import serial
from threading import Thread
import math
import os
import numpy as np


#musi,angle,stress,shearX,shearY,grip
class getPosition(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.point:int = 0

        #musi,angle,stress,shearX,shearY,grip
        self.rawData:list[float] = [0.0, 0.0, 0.0, 0.0]

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
                    self.point = self.estimatePoint(self.rawData)
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

    def estimatePoint(self, point_data:list)->int:
        data = np.array(point_data)
        mean = np.mean(data)
        variance = np.var(data)
        min_idx = np.argmin(data)


        point = int(min_idx + 1)
        if variance < 500:

            point = 5
        if mean > 200:
            point = 0

        print(point)
        return point

if __name__ == "__main__":
    thread=getPosition()
    thread.start()
    thread.join()