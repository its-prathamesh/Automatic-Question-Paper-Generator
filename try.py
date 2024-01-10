from tkinter import*
from sqlite3 import*
from setpaperpython import*

def go():
    pythonpaper()
    

root=Tk()
root.title("Login Page")
root.geometry("2000x1500")
canvas = Canvas(root, width=2000, height=1500)
canvas.place(x=0,y=0)

b=Button(canvas,text="Add User",bg="lightgreen",command=go).place(x=300,y=300)
