from tkinter import*
from sqlite3 import*

root = Tk()
root.geometry('2000x1500')
def sechap3():
    a=connect("pvp.db")
    d=a.cursor()
    d.execute("select *from sechap3 where Q_no>1 and Q_no<=25")
    data=d.fetchall()
    Label1 = Label(root, text="View Question Bank",font=("Times new roman",20))
    Label1.grid(row=0, column=1)
    Label1 = Label(root, text="Questions",width=30,font=("Times new roman",16))
    Label1.grid(row=2, column=0)
    Label2 = Label(root, text="Type",width=10,font=("Times new roman",16))
    Label2.grid(row=2, column=1)
    Label3 = Label(root, text="Marks",width=10,font=("Times new roman",16))
    Label3.grid(row=2, column=2)
    Label4 = Label(root, text="Q.NO",width=10,font=("Times new roman",16))
    Label4.grid(row=2, column=3)

    for index, dat in enumerate(data):
        Label(root,text=dat[0],height=1,font=("Arial",10)).grid(row=index+21, column=0)
        Label(root, text=dat[1],height=1,font=("Arial",10)).grid(row=index+21, column=1)
        Label(root, text=dat[2],height=1,font=("Arial",10)).grid(row=index+21, column=2)
        Label(root, text=dat[3],height=1,font=("Arial",10)).grid(row=index+21, column=3)

    l1=Label(root,text="EDIT",font=("Times new roman",20)).place(x=1100,y=0)
    l1=Label(root,text="Question:",font=("bold",13)).place(x=950,y=40)
    entry  = Text(root,height=1,width=40)#Question show
    entry.place(x=1000,y=70)

    l1=Label(root,text="Type:",font=("bold",13)).place(x=950,y=100)
    entry1  = Text(root,height=1,width=20)#Question show
    entry1.place(x=1000,y=130)

    l1=Label(root,text="Mark:",font=("bold",13)).place(x=950,y=160)
    entry2  = Text(root,height=1,width=20)#Question show
    entry2.place(x=1000,y=190)

    l1=Label(root,text="Question which You Want to change:",font=("bold",13)).place(x=950,y=220)
    qno = Entry(root,width =5)#Question no
    qno.place(x=1230,y=220)
    b=Button(root,text="NEXT",bg="green",fg="white",command=next).place(x=1050,y=550)
    l1=Label(root,text="For next Remaining Questions",fg="red",font=("bold",13)).place(x=1030,y=580)

    
    def insert():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("create table if not exists sechap3(Q_no int ,Question text)")
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            b.execute("insert into sechap3 (Q_no,Question,Type,Marks) values(?,?,?,?)",(qno.get(),var,var1,var2))
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()



    def update():
            a=connect("pvp.db")
            b=a.cursor()
            var = entry.get('1.0','end-1c')
            b.execute("update sechap3 set Question = (?) where Q_no = (?) ",(var,qno.get(),))
            entry.delete('1.0',END)
            a.commit()
            qno.delete(0, END)
            updatetype()
            

    def updatetype():
            a=connect("pvp.db")
            b=a.cursor()
            var1= entry1.get('1.0','end-1c')
            b.execute("update sechap3 set Type = (?) where Q_no = (?) ",(var1,qno.get(),))
            entry1.delete('1.0',END)
            a.commit()
            qno.delete(0, END)
            updatemarks()
            
            
    def updatemarks():
            a=connect("pvp.db")
            b=a.cursor()
            var2 = entry2.get('1.0','end-1c')
            b.execute("update sechap3 set Marks = (?) where Q_no = (?) ",(var2,qno.get(),))
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()
           
            
    def ext():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Question from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry.insert(END,i[j],"")
            exttype()
            
                    

    def exttype():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Type from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry1.insert(END,i[j],"")
            extmark()

    def extmark():
            but1 = Button(root,state=DISABLED)
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Marks from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry2.insert(END,i[j],"")

    def delete():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("create table if not exists sechap3(Q_no int ,Question text)")
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            b.execute("delete from sechap3 where Question = (?) and Q_no = (?) ",(var,qno.get(),))
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()

    def refresh():
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
            
    but1 = Button(root,text ="EXTRACT",width = 8,command = ext);
    but1.place(x=1000,y=270)

    upd = Button(root,text ="UPDATE",width = 8,command = update);
    upd.place(x=1000,y=300)

    but = Button(root,text ="INSERT",width = 8,command = insert);
    but.place(x=1000,y=330)

    but = Button(root,text ="DELETE",width = 8,command = delete);
    but.place(x=1000,y=360)

    but1 = Button(root,text ="REFRESH",width = 8,command = refresh);
    but1.place(x=1000,y=390)


def next():
    
    root1 = Tk()
    root1.geometry('2000x1500')
    a=connect("pvp.db")
    d=a.cursor()
    d.execute("select *from sechap3 where Q_no>25 and Q_no<=50")
    data=d.fetchall()
    Label1 = Label(root1, text="View Question Bank",font=("Times new roman",20))
    Label1.grid(row=0, column=1)
    Label1 = Label(root1, text="Questions",width=8,font=("Times new roman",16))
    Label1.grid(row=2, column=0)
    Label2 = Label(root1, text="Type",width=8,font=("Times new roman",16))
    Label2.grid(row=2, column=1)
    Label3 = Label(root1, text="Marks",width=10,font=("Times new roman",16))
    Label3.grid(row=2, column=2)
    Label4 = Label(root1, text="Q.NO",width=10,font=("Times new roman",16))
    Label4.grid(row=2, column=3)

    for index, dat in enumerate(data):
        Label(root1,text=dat[0],height=1,font=("Arial",10)).grid(row=index+21, column=0)
        Label(root1, text=dat[1],height=1,font=("Arial",10)).grid(row=index+21, column=1)
        Label(root1, text=dat[2],height=1,font=("Arial",10)).grid(row=index+21, column=2)
        Label(root1, text=dat[3],height=1,font=("Arial",10)).grid(row=index+21, column=3)

    l1=Label(root1,text="EDIT",font=("Times new roman",20)).place(x=1100,y=0)
    l1=Label(root1,text="Question:",font=("bold",13)).place(x=950,y=40)
    entry  = Text(root1,height=1,width=40)#Question show
    entry.place(x=1000,y=70)

    l1=Label(root1,text="Type:",font=("bold",13)).place(x=950,y=100)
    entry1  = Text(root1,height=1,width=20)#Question show
    entry1.place(x=1000,y=130)

    l1=Label(root1,text="Mark:",font=("bold",13)).place(x=950,y=160)
    entry2  = Text(root1,height=1,width=20)#Question show
    entry2.place(x=1000,y=190)

    l1=Label(root1,text="Question which You Want to change:",font=("bold",13)).place(x=950,y=220)
    qno = Entry(root1,width =5)#Question no
    qno.place(x=1230,y=220)
    b=Button(root1,text="BACK",bg="green",fg="white").place(x=1050,y=550)

    
    def insert():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("create table if not exists sechap3(Q_no int ,Question text)")
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            b.execute("insert into sechap3 (Q_no,Question,Type,Marks) values(?,?,?,?)",(qno.get(),var,var1,var2))
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()



    def update():
            a=connect("pvp.db")
            b=a.cursor()
            var = entry.get('1.0','end-1c')
            b.execute("update sechap3 set Question = (?) where Q_no = (?) ",(var,qno.get(),))
            entry.delete('1.0',END)
            a.commit()
            qno.delete(0, END)
            updatetype()
            

    def updatetype():
            a=connect("pvp.db")
            b=a.cursor()
            var1= entry1.get('1.0','end-1c')
            b.execute("update sechap3 set Type = (?) where Q_no = (?) ",(var1,qno.get(),))
            entry1.delete('1.0',END)
            a.commit()
            qno.delete(0, END)
            updatemarks()
            
            
    def updatemarks():
            a=connect("pvp.db")
            b=a.cursor()
            var2 = entry2.get('1.0','end-1c')
            b.execute("update sechap3 set Marks = (?) where Q_no = (?) ",(var2,qno.get(),))
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()
           
            
    def ext():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Question from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry.insert(END,i[j],"")
            exttype()
            
                    

    def exttype():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Type from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry1.insert(END,i[j],"")
            extmark()

    def extmark():
            but1 = Button(root1,state=DISABLED)
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("select Marks from sechap3 where Q_no = (?)",(qno.get(),))
            result = b.fetchall()
            for i in result:
                    for j in range(len(i)):
                            entry2.insert(END,i[j],"")

    def delete():
            a=connect("pvp.db")
            b=a.cursor()
            b.execute("create table if not exists sechap3(Q_no int ,Question text)")
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            b.execute("delete from sechap3 where Question = (?) and Q_no = (?) ",(var,qno.get(),))
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
            a.commit()

    def refresh():
            var = entry.get('1.0','end-1c')
            var1=entry1.get('1.0','end-1c')
            var2=entry2.get('1.0','end-1c')
            
            entry.delete('1.0',END)
            entry1.delete('1.0',END)
            entry2.delete('1.0',END)
            qno.delete(0, END)
    def back():
        root.destroy()
        root1.destroy()
    b=Button(root1,text="BACK",bg="green",fg="white",command=back).place(x=1050,y=550)

            
    but1 = Button(root1,text ="EXTRACT",width = 8,command = ext);
    but1.place(x=1000,y=270)

    upd = Button(root1,text ="UPDATE",width = 8,command = update);
    upd.place(x=1000,y=300)

    but = Button(root1,text ="INSERT",width = 8,command = insert);
    but.place(x=1000,y=330)

    but = Button(root1,text ="DELETE",width = 8,command = delete);
    but.place(x=1000,y=360)

    but1 = Button(root1,text ="REFRESH",width = 8,command = refresh);
    but1.place(x=1000,y=390)
    mainloop()
    
sechap3()

    
