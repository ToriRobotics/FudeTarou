import cv2
from PIL import Image, ImageTk

class StressFrame():
    cap:cv2
    def __init__(self):
        print("StressFrame")

    def show(self, dsize:int, stress:int, shearX:int, shearY:int):
        self.img = cv2.imread("img/white256x256.jpg")
        self.height, self.width=self.img.shape[:2]
        
        self.heightD=dsize
        self.widthD=int(dsize*int(self.width)/int(self.height))
        self.imgResize=cv2.resize(self.img, dsize=(self.widthD, self.heightD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        #self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()