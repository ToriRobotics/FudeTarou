import cv2
from PIL import Image, ImageTk

class FudeFrame():
    cap:cv2
    def __init__(self):
        #self.cap=cv2.imread("img/mock.jpg")
        #self.height, self.width, self.channels=self.cap.shape[:3]
        print("FudeFrame")

    def show(self, dsize:int):
        #ret, self.frame=self.cap.imshow("cap")
        #self.frame = cv2.resize(self.frame, dsize=(dsize, int(dsize*int(self.height)/int(self.width))))
        #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.img = cv2.imread("img/mock.jpg")
        self.height, self.width=self.img.shape[:2]
        
        self.heightD=dsize
        self.widthD=int(dsize*int(self.width)/int(self.height))
        print(self.widthD)
        print(self.heightD)
        self.imgResize=cv2.resize(self.img, dsize=(self.widthD, self.heightD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        #self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()