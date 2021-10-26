import tkinter
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database="world"
    )

    if mydb.cursor:
        print("Connection Successful!")

    mySql_Create_Table_Query = """CREATE TABLE
    students( 
                    Id int(11),
                    Name varchar(250))"""

    cursor = mydb.cursor()
    print("students table created successfully")
    win = tkinter.Tk()
    win.geometry("300x300")

    name1 = tkinter.IntVar()
    name2 = tkinter.StringVar()
    name=tkinter.Label(win,text="Name:-").place(x=30,y=50)
    phone = tkinter.Label(win,text="Phone").place(x=30,y=90)
    txt1=tkinter.Entry(win,textvariable=name1).place(x=80,y=50)
    txt2=tkinter.Entry(win,textvariable=name2).place(x=80,y=90)

    def save(event):
        sql ="INSERT INTO students(Id,Name) VALUES (%s,%s)"
        val =(name1.get(),name2.get())
        cursor.execute(sql,val)
        mydb.commit()
        print("Data Inserted")

        widget =tkinter.Button(win,text="Submit")
        widget.place(x=100,y=200)
        widget.bind('<Button-1>',save)
        win.mainloop()

except Exception as e:
    print("There are Exceptions ",e)

