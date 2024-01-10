from tkinter import *
from sqlite3 import*
import Image

root=Tk()
root.title("Login Page")
root.geometry("500x500")

l2=Label(root,text="Image Name:",font= ("bold",13))
l2.place(x=30,y=50)
ac=StringVar()
Entry(root,textvariable=ac).place(x=200,y=50)

b=Button(root,text="Submit",bg="green",fg="white").place(x=60,y=130)
