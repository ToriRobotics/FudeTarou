import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps
import datetime
import os
import serial
import readSerial
import makeFudeFrame
import viewStressFrame

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master.geometry("1280x720")
        self.master.title("FudeTarou")
        self.master.resizable(width=False, height=False)

        self.createFrame()

        self.thread=readSerial.getAngle()
        self.thread.start()
        self.fudeFrame=makeFudeFrame.FudeFrame()
        self.stressFrame=viewStressFrame.StressFrame()

        self.showFrame()

    def createFrame(self):
        self.background=tk.Frame(self.master, width=1280, height=720, bg="#C4C4C4")
        self.background.place(x=0, y=0)
    
    def showFrame(self):
        self.fudeFrame.show(dsize=450, stress=self.thread.rawData[0], shearX=self.thread.rawData[1], shearY=self.thread.rawData[2])
        self.imgPIL=PIL.Image.fromarray(self.fudeFrame.imgRGB)
        self.imgTk=PIL.ImageTk.PhotoImage(self.imgPIL)
        
        self.stressCanvas=tk.Canvas(self.master, width=640, height=720)
        self.stressCanvas.place(x=0, y=0)
        
        self.gripCanvas=tk.Canvas(self.master, width=640, height=360)
        self.gripCanvas.place(x=640, y=0)

        self.angleCanvas=tk.Canvas(self.master, width=640, height=360)
        self.angleCanvas.place(x=640, y=360)

        self.stressFrame.show(dsize=450, stress=self.thread.rawData[0], shearX=self.thread.rawData[1], shearY=self.thread.rawData[2])
        self.imgPIL=PIL.Image.fromarray(self.stressFrame.imgRGB)
        self.imgTk=PIL.ImageTk.PhotoImage(self.imgPIL)
        self.stressCanvas.create_image(0, 0, image=self.imgTk)
        '''
        self.canvas = tk.Canvas(self.master, width=self.fudeFrame.widthD, height=self.fudeFrame.heightD)
        #canvasの位置
        self.canvas.place(x=0, y=0)
        #canvas内の画像の位置
        self.canvas.create_image(0, 0, image = self.imgTk, anchor="nw")
        '''

        self.master.after(100, self.showFrame)

def main():
    root=tk.Tk()
    app=Application(master = root)
    app.mainloop()

if __name__=="__main__":
    main()
