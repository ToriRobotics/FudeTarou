import csv
import subprocess
import os
import datetime

class RecordData():
    header: list=["time", "stress", "shearX", "shearY", "grip", "angle", 
                        "rawStress", "rawShearX", "rawShearY", "rawGrip", "rawAngle"]

    def __init__(self, filename: str):
        self.filename = filename
        if not os.path.exists("log"):
            os.mkdir("log")

    def makeFile(self):
        subprocess.call(["touch", "log/" + self.filename + ".csv"])

    def openFile(self):
        self.file = open("log/" + self.filename + ".csv", "w")
        self.writer = csv.writer(self.file, lineterminator='\n')

    def makeHeader(self):
        self.writer.writerow(self.header)
    
    def addData(self, data:list):
        basetime=datetime.datetime.now()
        time=str(basetime.strftime("%m:%d:%H:%M:%S")) + ":" + str(basetime.microsecond)

        loglist:list=[]
        loglist.append(time)

        for i in data:
            loglist.append(i)

        self.writer.writerow(loglist)

    def closeFile(self):
        self.file.close()
        