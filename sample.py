from tkinter import*
from sqlite3 import*

root=Tk()
root.title("Login Page")
root.geometry("2000x1500")
canvas = Canvas(root, width=2000, height=1500)
canvas.place(x=0,y=0)

def dept():
    canvas=Canvas(root, width=2000, height=1500,bg="lightgrey")
    canvas.place(x=0,y=0)
    bimg=PhotoImage(file='gpm1.png')
    canvas.create_image(670,350,image=bimg)
    bimg1=PhotoImage(file='dept.png')
    canvas.create_image(670,350,image=bimg1)
    bimg2=PhotoImage(file='ITCO.png')
    canvas.create_image(670,190,image=bimg2)
    bimg3=PhotoImage(file='MECHCIVIL.png')
    canvas.create_image(670,300,image=bimg3)
    bimg4=PhotoImage(file='ECEE.png')
    canvas.create_image(670,410,image=bimg4)
    bimg5=PhotoImage(file='RLI.png')
    canvas.create_image(670,530,image=bimg5)


    pic1=PhotoImage(file='it1.png')
    pic2=PhotoImage(file='co1.png')
    pic3=PhotoImage(file='me1.png')
    pic4=PhotoImage(file='ec1.png')
    pic5=PhotoImage(file='ce1.png')
    pic6=PhotoImage(file='ee1.png')
    pic7=PhotoImage(file='le1.png')
    pic8=PhotoImage(file='ru1.png')
    pic9=PhotoImage(file='is1.png')
    #Donot change any placings

    b=Button(root,image=pic1,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=260,y=170)
    b=Button(root,image=pic2,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=700,y=170)

    b=Button(root,image=pic3,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=260,y=280)
    b=Button(root,image=pic5,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=700,y=280)

    b=Button(root,image=pic4,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=260,y=390)
    b=Button(root,image=pic6,height="40",width="330",activebackground="green",padx=2,pady=2).place(x=700,y=390)

    b=Button(root,image=pic7,height="40",width="290",activebackground="green",padx=2,pady=2).place(x=220,y=500)
    b=Button(root,image=pic8,height="40",width="310",activebackground="green",padx=2,pady=2).place(x=520,y=530)
    b=Button(root,image=pic9,height="40",width="280",activebackground="green",padx=2,pady=2).place(x=840,y=500)
    mainloop()

dept()



