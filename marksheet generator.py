from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageDraw,ImageFont
import math


global m
global p
global c
global t
global a
#functions

def calc():
    m = float(math1.get())
    p = float(physics1.get())
    c = float(chemistry1.get())
    t = (m+p+c)
    a = t/3
    total1.insert(0,t)
    avg1.insert(0,a)
    if (a>=95):
        grade1.insert(0,"O")
    elif (a>=90 and a<95):
        grade1.insert(0,"A+")
    elif (a>=80 and a<90):
        grade1.insert(0,"A")
    elif (a>=70 and a<80):
        grade1.insert(0,"B+")
    elif (a>=60 and a<70):
        grade1.insert(0,"B")
    elif (a>=50 and a<60):
        grade1.insert(0,"C")
    elif (a>=90 and a<95):
        grade1.insert(o,"P")
    else:
        grade1.insert(0,"Fail")

def delete():
    math1.delete(0,'end')
    physics1.delete(0,'end')
    chemistry1.delete(0,'end')
    total1.delete(0,'end')
    avg1.delete(0,'end')
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')

def mg():
    name = str(t1.get())
    class1 = str(t2.get())
    roll = str(t3.get())
    m1 = str(math1.get())
    p1 = str(physics1.get())
    c1 = str(chemistry1.get())
    totalm = str(total1.get())
    avgm = str(avg1.get())
    gradem = str(grade1.get())
    
    image = Image.open('ms.png')
    draw = ImageDraw.Draw(image)
    points1 = 120,65
    points2 = 120,115
    points3 = 120,155
    points4 = 115,265
    points5 = 180,265
    points6 = 250,265
    points7 = 415,265
    points8 = 480,265
    points9 = 770,265
    font1 = ImageFont.truetype("arial.ttf", 20)
    draw.text(points1,name,"black", font=font1)
    draw.text(points2,class1,"black", font=font1)
    draw.text(points3,roll,"black", font=font1)
    draw.text(points4,m1,"black", font=font1)
    draw.text(points5,p1,"black", font=font1)
    draw.text(points6,c1,"black", font=font1)
    draw.text(points7,totalm,"black", font=font1)
    draw.text(points8,avgm,"black", font=font1)
    draw.text(points9,gradem,"black", font=font1)
    image.save(rf'{t1.get()}.png')
    image.show()
    
win = Tk()
win.title("Marksheet Generator")
win.geometry("800x500")
win.maxsize(800,500)
win.minsize(800,500)
win['bg'] = "dark orange"

l1 = Label(win,text="Student's Name", font=("verdana",12,"bold"),borderwidth=5).grid(row=0, column=0, padx=20, pady=25)
t1 = Entry(win,borderwidth=7,width=20,font=("verdana",10,"bold"))
t1.grid(row=0, column=1,padx=20,pady=25)

l2 = Label(win,text="Student's Class", font=("verdana",12,"bold"),borderwidth=5).grid(row=1, column=0, padx=20, pady=25)
t2 = Entry(win,borderwidth=7,width=20,font=("verdana",10,"bold"))
t2.grid(row=1, column=1,padx=20,pady=25)

l3 = Label(win,text="Student's Roll", font=("verdana",12,"bold"),borderwidth=5).grid(row=2, column=0, padx=20, pady=25)
t3 = Entry(win,borderwidth=7,width=20,font=("verdana",10,"bold"))
t3.grid(row=2, column=1,padx=20,pady=25)
           
heading = Label(win,text="Marks",font=("verdana",18,"bold"),fg="gold",bg="dark orange",borderwidth=6).place(x=575,y=0)

math = Label(win,text="Math",font=("verdana",12,"bold"),borderwidth=5).place(x=475,y=60)
math1 = Entry(win,borderwidth=7,width=15,font=("verdana 10 bold"))
math1.place(x=590,y=60) 

physics = Label(win,text="Physics",font=("verdana",12,"bold"),borderwidth=5).place(x=475,y=120)
physics1 = Entry(win,borderwidth=7,width=15,font=("verdana 10 bold"))
physics1.place(x=590,y=120) 

chemistry = Label(win,text="Chemistry",font=("verdana",12,"bold"),borderwidth=5).place(x=475,y=180)
chemistry1 = Entry(win,borderwidth=7,width=15,font=("verdana 10 bold"))
chemistry1.place(x=590,y=180) 

# result space 


total = Label(win,text="Total",font=("verdana",12,"bold"),borderwidth=5).place(x=80,y=300)
total1 = Entry(win,borderwidth=7,width=20,font=("verdana 10 bold"))
total1.place(x=200,y=300)

avg = Label(win,text="Avarage",font=("verdana",12,"bold"),borderwidth=5).place(x=80,y=360)
avg1 = Entry(win,borderwidth=7,width=20,font=("verdana 10 bold"))
avg1.place(x=200,y=360)

grade = Label(win,text="Grade",font=("verdana",12,"bold"),borderwidth=5).place(x=80,y=420)
grade1 = Entry(win,borderwidth=7,width=20,font=("verdana 10 bold"))
grade1.place(x=200,y=420)




# buttons

calculate = Button(win,text="Calculate",width=12,borderwidth=5,font=("verdana 8 bold"),command=calc).place(x=600,y=260)
generate = Button(win,text="Generate",width=12,borderwidth=5,font=("verdana 8 bold"),command=mg).place(x=600,y=300)
clear = Button(win,text="Clear",width=12,borderwidth=5,font=("verdana 8 bold"),command=delete).place(x=600,y=340)


win.mainloop()


           
        

           
        
