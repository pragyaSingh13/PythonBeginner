import tkinter

myui = tkinter.Tk()
myui.geometry("300x300")
name = tkinter.Label(myui,text="NAME:-").place(x=30,y=50)
phone=tkinter.Label(myui,text="Phone").place(x=30,y=90)

e1 = tkinter.Entry(myui).place(x=80,y=50)
e2 = tkinter.Entry(myui).place(x=80,y=90)
myui.mainloop()