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

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master.geometry("720x450")
        self.master.title("FudeTarou")
        self.master.resizable(width=False, height=False)

        self.createFrame()

        #self.thread=readSerial.getAngle(port="port")
        self.fudeFrame=makeFudeFrame.FudeFrame()

        self.showFrame()

    def createFrame(self):
        self.background=tk.Frame(self.master, width=720, height=450, bg="#C4C4C4")
        self.background.place(x=0, y=0)

    
    def showFrame(self):
        self.fudeFrame.show(dsize=450)
        self.imgPIL=PIL.Image.fromarray(self.fudeFrame.imgRGB)
        self.imgTk=PIL.ImageTk.PhotoImage(self.imgPIL)

        self.canvas = tk.Canvas(self.master, width=self.fudeFrame.widthD, height=self.fudeFrame.heightD)
        #canvasの位置
        self.canvas.place(x=0, y=0)
        #canvas内の画像の位置
        self.canvas.create_image(0, 0, image = self.imgTk, anchor="nw")

        #self.master.after(100, self.showFrame)


def main():
    root=tk.Tk()
    app=Application(master = root)
    app.mainloop()

if __name__=="__main__":
    main()
