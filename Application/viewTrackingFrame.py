import cv2
from PIL import Image, ImageTk

class TrackingFrame():
    cap:cv2
    def __init__(self):
        print("TrackingFrame")

    def show(self, dsize:int, position:int):
        self.img = cv2.imread("img/tracking.jpg")
        self.height, self.width=self.img.shape[:2]
        
        widthD=dsize
        heightD=int(dsize*int(self.height)/int(self.width))
        
        #print(position)
        #self.heightD=dsize
        #self.widthD=int(dsize*int(self.width)/int(self.height))

        
        if position==1:
            cv2.circle(self.img, (150, 150), 20, (200, 200, 255), thickness=-1)
        if position==2:
            cv2.circle(self.img, (450, 150), 20, (200, 200, 255), thickness=-1)
        if position==3:
            cv2.circle(self.img, (150, 450), 20, (200, 200, 255), thickness=-1)
        if position==4:
            cv2.circle(self.img, (450, 450), 20, (200, 200, 255), thickness=-1)
        if position==5:
            cv2.circle(self.img, (300, 300), 20, (200, 200, 255), thickness=-1)
        self.imgResize=cv2.resize(self.img, dsize=(widthD, widthD))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        #self.cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()