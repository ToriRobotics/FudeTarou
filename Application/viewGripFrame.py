import cv2
from PIL import Image, ImageTk

class GripFrame():
    cap:cv2
    def __init__(self):
        print("GripFrame")

    def show(self, dsize:int):
        self.img = cv2.imread("img/FudeGripLow.jpg")
        self.height, self.width=self.img.shape[:2]
        
        widthD=dsize
        heightD=int(dsize*int(self.height)/int(self.width))

        #self.heightD=dsize
        #self.widthD=int(dsize*int(self.width)/int(self.height))

        self.imgResize=cv2.resize(self.img, dsize=(widthD, heightD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()