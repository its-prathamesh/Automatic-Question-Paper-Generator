from tkinter import*
from sqlite3 import*

root=Tk()
root.title("Login Page")
root.geometry("2000x1500")
canvas = Canvas(root, width=2000, height=1500)
canvas.place(x=0,y=0)


canvas = Canvas(root, width=2000, height=1500)
canvas.place(x=0,y=0)
bimg=PhotoImage(file='gpm1.png')
canvas.create_image(670,350,image=bimg)
sub=PhotoImage(file='subject.png')
canvas.create_image(685,140,image=sub)
infosec=PhotoImage(file='is.png')
b=Button(root,image=infosec,height="60",width="710",bg="white",padx=2,pady=2,bd=5).place(x=340,y=260)
se=PhotoImage(file='se.png')
b=Button(root,image=se,height="60",width="710",bg="white",padx=2,pady=2,bd=5).place(x=340,y=330)
linux=PhotoImage(file='linux.png')
b=Button(root,image=linux,height="60",width="710",bg="white",padx=2,pady=2,bd=5).place(x=340,y=400)
py=PhotoImage(file='py.png')
b=Button(root,image=py,height="60",width="710",bg="white",padx=2,pady=2,bd=5).place(x=340,y=470)
mainloop()
