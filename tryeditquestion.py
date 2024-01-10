from tkinter import *
from sqlite3 import*


root = Tk()
root.geometry("500x300")

l1=Label(root,text="Question:",font=("bold",13)).place(x=2,y=10)
entry  = Text(root,height=1,width=40)#Question show
entry.place(x=100,y=12)

l1=Label(root,text="Type:",font=("bold",13)).place(x=2,y=40)
entry1  = Text(root,height=1,width=20)#Question show
entry1.place(x=100,y=42)

l1=Label(root,text="Mark:",font=("bold",13)).place(x=2,y=70)
entry2  = Text(root,height=1,width=20)#Question show
entry2.place(x=100,y=72)

l1=Label(root,text="Question which You Want to change:",font=("bold",13)).place(x=2,y=100)
qno = Entry(root,width = 3)#Question no
qno.place(x=300,y=103)

def insert():
        a=connect("pvp.db")
        b=a.cursor()
        b.execute("create table if not exists chapter1(Q_no int ,Question text)")
        var = entry.get('1.0','end-1c')
        b.execute("insert into chapter1 (Q_no,Question) values(?,?)",(qno.get(),var,))
        entry.delete('1.0',END)
        a.commit()


def update():
        a=connect("pvp.db")
        b=a.cursor()
        var = entry.get('1.0','end-1c')
        b.execute("update chapter1 set Question = (?) where Q_no = (?) ",(var,qno.get(),))
        entry.delete('1.0',END)
        a.commit()
        updatetype()
        

def updatetype():
        a=connect("pvp.db")
        b=a.cursor()
        var1= entry1.get('1.0','end-1c')
        b.execute("update chapter1 set Type = (?) where Q_no = (?) ",(var1,qno.get(),))
        entry1.delete('1.0',END)
        a.commit()
        updatemarks()
        
        
def updatemarks():
        a=connect("pvp.db")
        b=a.cursor()
        var2 = entry2.get('1.0','end-1c')
        b.execute("update chapter1 set Marks = (?) where Q_no = (?) ",(var2,qno.get(),))
        entry2.delete('1.0',END)
        a.commit()
       
        


        

def ext():
        a=connect("pvp.db")
        b=a.cursor()
        b.execute("select Question from chapter1 where Q_no = (?)",(qno.get(),))
        result = b.fetchall()
        for i in result:
                for j in range(len(i)):
                        entry.insert(END,i[j],"")
        exttype()
        
                

def exttype():
        a=connect("pvp.db")
        b=a.cursor()
        b.execute("select Type from chapter1 where Q_no = (?)",(qno.get(),))
        result = b.fetchall()
        for i in result:
                for j in range(len(i)):
                        entry1.insert(END,i[j],"")
        extmark()

def extmark():
        a=connect("pvp.db")
        b=a.cursor()
        b.execute("select Marks from chapter1 where Q_no = (?)",(qno.get(),))
        result = b.fetchall()
        for i in result:
                for j in range(len(i)):
                        entry2.insert(END,i[j],"")
        
                        


but1 = Button(root,text ="EXTRACT",width = 8,command = ext);
but1.place(x=60,y=150)

upd = Button(root,text ="UPDATE",width = 8,command = update);
upd.place(x=60,y=180)

but = Button(root,text ="INSERT",width = 8,command = insert);
but.place(x=60,y=210)
root.mainloop()
