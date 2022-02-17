import cv2
from PIL import Image, ImageTk
from cv2 import cvtColor
import numpy as np

class GripFrame():
    cap:cv2
    def __init__(self):
        print("GripFrame")

    def show(self, dsize:int, grip:int):
        self.img = cv2.imread("img/gripLow.jpg")
        self.height, self.width=self.img.shape[:2]

        widthH=393
        highH=60

        200-600

        #sensor0-1023
        #color0-155
        grip=min(int(grip/6*1.5), 155)
        cv2.rectangle(self.img,
              pt1=(150, 139),
              pt2=(150+widthH, 139+highH),
              color=(100, 100, 100+grip),
              thickness=-1,  
              )
        #self.heightD=dsize
        #self.widthD=int(dsize*int(self.width)/int(self.height))

        self.imgResize=cv2.resize(self.img, dsize=(640, 360))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()