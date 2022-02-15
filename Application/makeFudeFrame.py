import cv2
from PIL import Image, ImageTk

class FudeFrame():
    def __init__(self):
        print("FudeFrame")

    def show(self, dsize:int, stress:int, shearX:int, shearY:int):
        
        self.img = cv2.imread("img/mock.jpg")
        self.height, self.width=self.img.shape[:2]
        
        self.heightD=dsize
        self.widthD=int(dsize*int(self.width)/int(self.height))

        #stress 0->255
        cv2.circle(self.img, (int(self.width/2), int(self.height/2)), 3, (0,0,0), thickness=-1)
        cv2.circle(self.img, (int(self.width/2) + shearX, int(self.height/2) - shearY), 20, (255 -stress, 255 - stress, 255), thickness=-1)

        self.imgResize=cv2.resize(self.img, dsize=(self.widthD, self.heightD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        #self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()