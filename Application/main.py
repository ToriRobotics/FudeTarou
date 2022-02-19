import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps
import datetime
import os
from numpy import pad
import serial
import readSerial
import get_position
#import makeFudeFrame
import viewStressFrame
import viewGripFrame
import viewAngleFrame
import viewTrackingFrame

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master.geometry("1280x720")
        self.master.title("FudeTarou")
        self.master.resizable(width=False, height=False)

        self.createFrame()

        self.thread=readSerial.getAngle()
        self.thread.start()
        self.thread2=get_position.getPosition()
        self.thread2.start()
        #self.fudeFrame=makeFudeFrame.FudeFrame()
        self.stressFrame=viewStressFrame.StressFrame()
        self.gripFrame=viewGripFrame.GripFrame()
        self.angleFrame=viewAngleFrame.AngleFrame()
        self.trackingFrame=viewTrackingFrame.TrackingFrame()

        self.showFrame()
        self.createWidget()
        self.subWin=None
        #self.showSubWindow()

        self.point = 0

    def createFrame(self):
        #self.background=tk.Frame(self.master, width=1280, height=720, bg="#C4C4C4")
        #self.background.place(x=0, y=0)

        self.buttonFrame=tk.Frame(self.master, width=1280, height=40, bg="#262626")
        self.buttonFrame.place(x=0, y=0)
    
    def createWidget(self):
        button_FudeTracking=tk.Button(self.buttonFrame, text="tracking", width=3, command=self.setupSubWindow)
        button_FudeTracking.grid(row=0, column=0, padx=0, pady=0, sticky=tk.E)
        button_endApp=tk.Button(self.buttonFrame, text="exit", width=3, command=self.exitApp)
        button_endApp.grid(row=0, column=1, padx=0, pady=0, sticky=tk.E)

    def showFrame(self):
        self.stressCanvas=tk.Canvas(self.master, width=640, height=720)
        self.stressCanvas.place(x=0, y=30)
        
        self.gripCanvas=tk.Canvas(self.master, width=640, height=360)
        self.gripCanvas.place(x=640, y=0)

        self.angleCanvas=tk.Canvas(self.master, width=640, height=360)
        self.angleCanvas.place(x=640, y=360)

        self.stressFrame.show(dsize=640, stress=self.thread.rawData[2], shearX=self.thread.rawData[3], shearY=self.thread.rawData[4])
        #self.stressFrame.show(dsize=640, stress=, shearX=0, shearY=0)
        self.stressimgPIL=PIL.Image.fromarray(self.stressFrame.imgRGB)
        self.stressimgTk=PIL.ImageTk.PhotoImage(self.stressimgPIL)
        self.stressCanvas.create_image(0, 40, image=self.stressimgTk, anchor="nw")
        
        self.gripFrame.show(dsize=640, grip=self.thread.rawData[5])
        self.gripimgPIL=PIL.Image.fromarray(self.gripFrame.imgRGB)
        self.gripimgTk=PIL.ImageTk.PhotoImage(self.gripimgPIL)
        self.gripCanvas.create_image(0, 0, image=self.gripimgTk, anchor="nw")

        self.angleFrame.show(dsize=640, angle=self.thread.rawData[1])
        self.angleimgPIL=PIL.Image.fromarray(self.angleFrame.imgRGB)
        self.angleimgTk=PIL.ImageTk.PhotoImage(self.angleimgPIL)
        self.angleCanvas.create_image(0, 0, image=self.angleimgTk, anchor="nw")

        self.point = self.thread2.point
        self.master.after(100, self.showFrame)

    def exitApp(self):
        self.master.destroy()

    def setupSubWindow(self):
        if self.subWin == None or not self.subWin.winfo_exists():
            self.subWin = tk.Toplevel()
            self.subWin.resizable(width=False, height=False)
            self.subWin.geometry("600x600")
            self.subWin.title("FudeTracking")
            self.trackingCanvas=tk.Canvas(self.subWin, width=600, height=600)
            self.trackingCanvas.place(x=0, y=30)
        self.trackingFrame.show(dsize=600, position=self.thread2.point)
        self.trackingimgPIL=PIL.Image.fromarray(self.trackingFrame.imgRGB)
        self.trackingimgTk=PIL.ImageTk.PhotoImage(self.trackingimgPIL)
        self.trackingCanvas.create_image(0, 0, image=self.trackingimgTk, anchor="nw")

        self.subButtonFrame=tk.Frame(self.subWin, width=600, height=30, bg="#262626")
        self.subButtonFrame.place(x=0, y=0)

        subButton_endApp=tk.Button(self.subButtonFrame, text="exit", width=3, command=self.exitSubApp)
        subButton_endApp.grid(row=0, column=0, padx=0, pady=0, sticky=tk.E)

        self.master.after(100, self.setupSubWindow)

    def exitSubApp(self):
        self.subWin.destroy()



def main():
    root=tk.Tk()
    app=Application(master = root)
    app.mainloop()

if __name__=="__main__":
    main()
