import tkinter
from tkinter import *
from tkinter import messagebox
import math

def opencircuit():
    value1=float(V.get())
    value2=float(I.get())
    value3=float(WA.get())

    Iw=(value3)/(value1)
    Im=math.sqrt((value2*value2)-(Iw*Iw))
    Pw=(value3)/(value2*value1)
    Ro=value1/Iw
    Xo=value1/Im
    Label(text=f"Iw = {Iw}", font=30).place(x=100, y=400)
    Label(text=f"Im = {Im}", font=30).place(x=100, y=420)
    Label(text=f"pw = {Pw}", font=30).place(x=100, y=440)
    Label(text=f"Ro = {Ro}", font=30).place(x=100, y=460)
    Label(text=f"Xo = {Xo}", font=30).place(x=100, y=480)

def shortcircuit():
    value1=float(Vs.get())
    value2=float(Is.get())
    value3=float(Ws.get())

    Ro1=value3/(value2*value2)
    Zo1=value1/value2
    Xo1=math.sqrt((Zo1*Zo1)-(Ro1*Ro1))

    Label(text=f"Zo = {Zo1}", font=30).place(x=500, y=400)
    Label(text=f"Ro = {Ro1}", font=30).place(x=500, y=420)
    Label(text=f"Xo = {Xo1}", font=30).place(x=500, y=440)

root=Tk()
root.title("calculator")
root.geometry("800x600+450+90")

global V
global I
global WA
global Vs
global Is
global Ws

Label(text="OPEN CIRCUIT", font=40).place(x=150, y=50)
Label(text="V", font=23).place(x=100,y=100) 
Label(text="I", font=23).place(x=100,y=150) 
Label(text="W", font=23).place(x=100,y=200) 


V=Entry(root, width=15,bd=3, font=20)
V.place(x=150,y=100)

I=Entry(root, width=15,bd=3, font=20)
I.place(x=150,y=150)

WA=Entry(root, width=15,bd=3, font=20)
WA.place(x=150,y=200)

Button(text="calculate", font=20, bg="white", fg="black", width=11, height=2, command=opencircuit).place(x=150,y=260)


# short circuit test

Label(text="SHORT CIRCUIT", font=40).place(x=550, y=50)
Label(text="V", font=23).place(x=500,y=100) 
Label(text="I", font=23).place(x=500,y=150) 
Label(text="W", font=23).place(x=500,y=200) 



Vs=Entry(root, width=15,bd=3, font=20)
Vs.place(x=550,y=100)

Is=Entry(root, width=15,bd=3, font=20)
Is.place(x=550,y=150)

Ws=Entry(root, width=15,bd=3, font=20)
Ws.place(x=550,y=200)


Button(text="calculate", font=20, bg="white", fg="black", width=11, height=2, command=shortcircuit).place(x=550,y=260)


root.mainloop()