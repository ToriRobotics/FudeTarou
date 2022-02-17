import cv2
from PIL import Image, ImageTk

class StressFrame():
    cap:cv2
    def __init__(self):
        print("StressFrame")

    def show(self, dsize:int, stress:int, shearX:int, shearY:int):
        self.img = cv2.imread("img/white256x256.jpg")
        self.height, self.width=self.img.shape[:2]
        
        widthD=dsize
        heightD=int(dsize*int(self.height)/int(self.width))

        #self.heightD=dsize
        #self.widthD=int(dsize*int(self.width)/int(self.height))

         #stress 0->255
        cv2.circle(self.img, (int(self.width/2), int(self.height/2)), 3, (0,0,0), thickness=-1)
        stress=min(stress*3,255)
        cv2.circle(self.img, (int(self.width/2) + shearX, int(self.height/2) - shearY), 20, (255 -stress, 255 - stress, 200), thickness=-1)

        self.imgResize=cv2.resize(self.img, dsize=(widthD, widthD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        #self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()