import cv2
from PIL import Image, ImageTk
import math

class AngleFrame():
    cap:cv2
    def __init__(self):
        print("AngleFrame")

    def show(self, dsize:int, angle:float):
        self.img = cv2.imread("img/angle.jpg")
        self.height, self.width=self.img.shape[:2]

        cv2.circle(self.img, (int(320+200*math.cos(math.radians(180-angle))), int(297 - 200*math.sin(math.radians(180-angle)))), 10, (100,100, 255), thickness=-1)
        self.imgResize=cv2.resize(self.img, dsize=(640, 360))
        self.imgRGB=cv2.cvtColor(self.imgResize, cv2.COLOR_BGR2RGB)

    def endShow(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()