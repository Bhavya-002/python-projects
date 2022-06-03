#import the required library
from tkinter import *
#create object
root = Tk()
#set geometry
root.geometry("200x530")
              #list of cursors
cursors = ["arrow", "circle", "Clock", "cross", "dotbox", "exchange","fleur", "heart", "man","mouse", "pirate", "plus","shuttle", "sizing","spider", "spraycan", "star", "target", "tcross", "trek"]


for cursor in cursors:

    Button(root, text=cursor,cursor=cursor).pack()

root.mainloop()
