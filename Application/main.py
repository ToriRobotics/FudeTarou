import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps
import datetime
import os
import serial

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master.geometry("720x450")
        self.master.title("FudeTarou")
        self.master.resizable(width=False, height=False)

        self.createFrame()

    def createFrame(self):
        self.background=tk.Frame(self.master, width=720, height=450, bg="#C4C4C4")
        self.background.place(x=0, y=0)

def main():
    root=tk.Tk()
    app=Application(master = root)
    app.mainloop()

if __name__=="__main__":
    main()
