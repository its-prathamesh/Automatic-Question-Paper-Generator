from tkinter import*
from sqlite3 import*
from tkinter import messagebox


def database():
    a=connect("pvp.db")
    b=a.cursor()
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name.get(),aa,aa1))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name1.get(),aa2,aa3))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name2.get(),aa4,aa5))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name3.get(),aa6,aa7))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name4.get(),aa8,aa9))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name5.get(),a1,a2))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name6.get(),a3,a4))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name7.get(),a5,a6))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name8.get(),a7,a8))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name9.get(),a9,a10))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name10.get(),a11,a12))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name11.get(),a13,a14))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name12.get(),a15,a16))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name13.get(),a17,a18))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name14.get(),a19,a20))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name15.get(),a21,a22))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name16.get(),a23,a24))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name17.get(),a25,a26))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name18.get(),a27,a28))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name19.get(),a29,a30))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name20.get(),a31,a32))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name21.get(),a33,a34))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name22.get(),a35,a36))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name23.get(),a37,a38))
    b.execute("insert into chapter1 values ('{}','{}','{}')".format(name24.get(),a39,a40))
    
    a.commit()
    b.close()
    a.close()
    
    

root=Tk()
root.geometry('1500x1500')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.maxsize(w,h)


canvas=Canvas(root,height=h,width=w,bd=3,relief=RIDGE,scrollregion=(0,0,0,1500),highlightcolor="#016193")
canvas.place(x=0,y=0)
scroll=Scrollbar(canvas,orient=VERTICAL)
scroll.place(x=1335,y=10,relheight=0.965)
scroll.config(command = canvas.yview )
canvas.configure(yscrollcommand = scroll.set)

canvas.create_text((10,40),anchor=NW, text="Chapter 1",font=("bold",25))


#Question 1
global name
name=StringVar()
canvas.create_text((20,90),anchor=NW, text="Q.1",font= (20))
e=Entry(textvariable=name,width=50)
canvas.create_window((50,90),anchor=NW,window=e)
name.get()

variable = StringVar(root)
c=["R","U","A"]
s=Spinbox(canvas,values=c,textvariabl=variable)
def o():
    global aa
    if(str(variable.get())=='R'):
        aa = "R"

        
    elif(str(variable.get())=='U'):
        aa= "U"

        
    elif(str(variable.get())=='A'):
        aa= "A"
canvas.create_window((410,90), anchor='nw', window=s)

variable1 = StringVar(root)
c1=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c1,textvariabl=variable1)
def o1():
    global aa1
    if(str(variable1.get())=='2marks'):
        aa1=2

        
    elif(str(variable1.get())=='4marks'):
        aa1=4

    
    elif(str(variable1.get())=='6marks'):
        aa1=6

canvas.create_window((610,90), anchor='nw', window=s)

#Question 2
global name1
name1=StringVar()
canvas.create_text((20,140),anchor=NW, text="Q.2",font= (20))
e=Entry(textvariable=name1,width=50)
canvas.create_window((50,140),anchor=NW,window=e)
name1.get()

variable2 = StringVar(root)
c2=["R","U","A"]
s=Spinbox(canvas,values=c2,textvariabl=variable2)
def o2():
    global aa2
    if(str(variable2.get())=='R'):
        aa2 = "R"

        
    elif(str(variable2.get())=='U'):
        aa2= "U"

        
    elif(str(variable2.get())=='A'):
        aa2= "A"
canvas.create_window((410,140), anchor='nw', window=s)


variable3 = StringVar(root)
c3=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c3,textvariabl=variable3)
def o3():
    global aa3
    if(str(variable3.get())=='2marks'):
        aa3=2

        
    elif(str(variable3.get())=='4marks'):
        aa3=4

    
    elif(str(variable3.get())=='6marks'):
        aa3=6
canvas.create_window((610,140), anchor='nw', window=s)

#Question 3
global name2
name2=StringVar()
canvas.create_text((20,190),anchor=NW, text="Q.3",font= (20))
e=Entry(textvariable=name2,width=50)
canvas.create_window((50,190),anchor=NW,window=e)
name2.get()

variable4 = StringVar(root)
c4=["R","U","A"]
s=Spinbox(canvas,values=c4,textvariabl=variable4)
def o4():
    global aa4
    if(str(variable4.get())=='R'):
        aa4="R"

        
    elif(str(variable4.get())=='U'):
        aa4="U"

        
    elif(str(variable4.get())=='A'):
        aa4="A"

canvas.create_window((410,190), anchor='nw', window=s)


variable5 = StringVar(root)
c5=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c5,textvariabl=variable5)
def o5():
    global aa5
    if(str(variable5.get())=='2marks'):
        aa5=2

        
    elif(str(variable5.get())=='4marks'):
        aa5=4

    
    elif(str(variable5.get())=='6marks'):
        aa5=6
canvas.create_window((610,190), anchor='nw', window=s)

#Question 4
global name3
name3=StringVar()
canvas.create_text((20,240),anchor=NW, text="Q.4",font= (20))
e=Entry(textvariable=name3,width=50)
canvas.create_window((50,240),anchor=NW,window=e)
name3.get()

variable6 = StringVar(root)
c6=["R","U","A"]
s=Spinbox(canvas,values=c6,textvariabl=variable6)
def o6():
    global aa6
    if(str(variable6.get())=='R'):
        aa6 = "R"

        
    elif(str(variable6.get())=='U'):
        aa6= "U"

        
    elif(str(variable6.get())=='A'):
        aa6= "A"
s.place(x=410,y=210)
canvas.create_window((410,240), anchor='nw', window=s)


variable7 = StringVar(root)
c7=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c7,textvariabl=variable7)
def o7():
    global aa7
    if(str(variable7.get())=='2marks'):
        aa7=2

        
    elif(str(variable7.get())=='4marks'):
        aa7=4

    
    elif(str(variable7.get())=='6marks'):
        aa7=6
canvas.create_window((610,240), anchor='nw', window=s)

#Question 5
global name4
name4=StringVar()
canvas.create_text((20,290),anchor=NW, text="Q.5",font= (20))
e=Entry(textvariable=name4,width=50)
canvas.create_window((50,290),anchor=NW,window=e)
name4.get()

variable8 = StringVar(root)
c8=["R","U","A"]
s=Spinbox(canvas,values=c8,textvariabl=variable8)
def o8():
    global aa8
    if(str(variable8.get())=='R'):
        aa8 = "R"

        
    elif(str(variable8.get())=='U'):
        aa8= "U"

        
    elif(str(variable8.get())=='A'):
        aa8= "A"
canvas.create_window((410,290), anchor='nw', window=s)


variable9 = StringVar(root)
c9=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c9,textvariabl=variable9)
def o9():
    global aa9
    if(str(variable9.get())=='2marks'):
        aa9=2

        
    elif(str(variable9.get())=='4marks'):
        aa9=4

    
    elif(str(variable9.get())=='6marks'):
        aa9=6
canvas.create_window((610,290), anchor='nw', window=s)

#Question 6
global name5
name5=StringVar()
canvas.create_text((20,340),anchor=NW, text="Q.6",font= (20))
e=Entry(textvariable=name5,width=50)
canvas.create_window((50,340),anchor=NW,window=e)
name5.get()

variabl0 = StringVar(root)
c10=["R","U","A"]
s=Spinbox(canvas,values=c10,textvariabl=variabl0)
def o10():
    global a1
    if(str(variabl0.get())=='R'):
        a1 = "R"

        
    elif(str(variabl0.get())=='U'):
        a1= "U"

        
    elif(str(variabl0.get())=='A'):
        a1= "A"

canvas.create_window((410,340), anchor='nw', window=s)


variabl1 = StringVar(root)
c11=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c11,textvariabl=variabl1)
def o11():
    global a2
    if(str(variabl1.get())=='2marks'):
        a2=2

        
    elif(str(variabl1.get())=='4marks'):
        a2=4

    
    elif(str(variabl1.get())=='6marks'):
        a2=6


canvas.create_window((610,340), anchor='nw', window=s)

#Question 7
global name6
name6=StringVar()
canvas.create_text((20,390),anchor=NW, text="Q.7",font= (20))
e=Entry(textvariable=name6,width=50)
canvas.create_window((50,390),anchor=NW,window=e)
name6.get()

variabl2 = StringVar(root)
c12=["R","U","A"]
s=Spinbox(canvas,values=c12,textvariabl=variabl2)
def o12():
    global a3
    if(str(variabl2.get())=='R'):
        a3 = "R"

        
    elif(str(variabl2.get())=='U'):
        a3= "U"

        
    elif(str(variabl2.get())=='A'):
        a3= "A"
canvas.create_window((410,390), anchor='nw', window=s)


variabl3 = StringVar(root)
c13=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c13,textvariabl=variabl3)
def o13():
    global a4
    if(str(variabl3.get())=='2marks'):
        a4=2

        
    elif(str(variabl3.get())=='4marks'):
        a4=4

    
    elif(str(variabl3.get())=='6marks'):
        a4=6
canvas.create_window((610,390), anchor='nw', window=s)

#Question 8
global name7
name7=StringVar()
canvas.create_text((20,440),anchor=NW, text="Q.8",font= (20))
e=Entry(textvariable=name7,width=50)
canvas.create_window((50,440),anchor=NW,window=e)
name7.get()

variabl4 = StringVar(root)
c14=["R","U","A"]
s=Spinbox(canvas,values=c14,textvariabl=variabl4)
def o14():
    global a5
    if(str(variabl4.get())=='R'):
        a5 = "R"

        
    elif(str(variabl4.get())=='U'):
        a5= "U"

        
    elif(str(variabl4.get())=='A'):
        a5= "A"
canvas.create_window((410,440), anchor='nw', window=s)


variabl5 = StringVar(root)
c15=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c15,textvariabl=variabl5)
def o15():
    global a6
    if(str(variabl5.get())=='2marks'):
        a6=2

        
    elif(str(variabl5.get())=='4marks'):
        a6=4

    
    elif(str(variabl5.get())=='6marks'):
        a6=6
canvas.create_window((610,440), anchor='nw', window=s)

#Question 9
global name8
name8=StringVar()
canvas.create_text((20,490),anchor=NW, text="Q.9",font= (20))
e=Entry(textvariable=name8,width=50)
canvas.create_window((50,490),anchor=NW,window=e)
name8.get()

variabl6 = StringVar(root)
c16=["R","U","A"]
s=Spinbox(canvas,values=c16,textvariabl=variabl6)
def o16():
    global a7
    if(str(variabl6.get())=='R'):
        a7 = "R"

        
    elif(str(variabl6.get())=='U'):
        a7= "U"

        
    elif(str(variabl6.get())=='A'):
        a7= "A"
s.place(x=410,y=460)
canvas.create_window((410,490), anchor='nw', window=s)


variabl7 = StringVar(root)
c17=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c17,textvariabl=variabl7)
def o17():
    global a8
    if(str(variabl7.get())=='2marks'):
        a8=2

        
    elif(str(variabl7.get())=='4marks'):
        a8=4

    
    elif(str(variabl7.get())=='6marks'):
        a8=6
canvas.create_window((610,490), anchor='nw', window=s)


#Question 10
global name9
name9=StringVar()
canvas.create_text((15,540),anchor=NW, text="Q.10",font= (20))
e=Entry(textvariable=name9,width=50)
canvas.create_window((50,540),anchor=NW,window=e)
name9.get()

variabl8 = StringVar(root)
c18=["R","U","A"]
s=Spinbox(canvas,values=c18,textvariabl=variabl8)
def o18():
    global a9
    if(str(variabl8.get())=='R'):
        a9 = "R"

        
    elif(str(variabl8.get())=='U'):
        a9= "U"

        
    elif(str(variabl8.get())=='A'):
        a9= "A"
canvas.create_window((410,540), anchor='nw', window=s)


variabl9 = StringVar(root)
c19=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c19,textvariabl=variabl9)
def o19():
    global a10
    if(str(variabl9.get())=='2marks'):
        a10=2

        
    elif(str(variabl9.get())=='4marks'):
        a10=4

    
    elif(str(variabl9.get())=='6marks'):
        a10=6
canvas.create_window((610,540), anchor='nw', window=s)


#Question 11
global name10
name10=StringVar()
canvas.create_text((15,590),anchor=NW, text="Q.11",font= (20))
e=Entry(textvariable=name10,width=50)
canvas.create_window((50,590),anchor=NW,window=e)
name10.get()

variabl10 = StringVar(root)
c20=["R","U","A"]
s=Spinbox(canvas,values=c20,textvariabl=variabl10)
def o20():
    global a11
    if(str(variabl10.get())=='R'):
        a11 = "R"

        
    elif(str(variabl10.get())=='U'):
        a11= "U"

        
    elif(str(variabl10.get())=='A'):
        a11= "A"
canvas.create_window((410,590), anchor='nw', window=s)


variabl11 = StringVar(root)
c21=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c21,textvariabl=variabl11)
def o21():
    global a12
    if(str(variabl11.get())=='2marks'):
        a12=2

        
    elif(str(variabl11.get())=='4marks'):
        a12=4

    
    elif(str(variabl11.get())=='6marks'):
        a12=6
canvas.create_window((610,590), anchor='nw', window=s)

#Question 12
global name11
name11=StringVar()
canvas.create_text((15,640),anchor=NW, text="Q.12",font= (20))
e=Entry(textvariable=name11,width=50)
canvas.create_window((50,640),anchor=NW,window=e)
name11.get()

variabl12 = StringVar(root)
c22=["R","U","A"]
s=Spinbox(canvas,values=c22,textvariabl=variabl12)
def o22():
    global a13
    if(str(variabl12.get())=='R'):
        a13 = "R"

        
    elif(str(variabl12.get())=='U'):
        a13= "U"

        
    elif(str(variabl12.get())=='A'):
        a13= "A"
canvas.create_window((410,640), anchor='nw', window=s)


variabl13 = StringVar(root)
c23=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c23,textvariabl=variabl13)
def o23():
    global a14
    if(str(variabl13.get())=='2marks'):
        a14=2

        
    elif(str(variabl13.get())=='4marks'):
        a14=4

    
    elif(str(variabl13.get())=='6marks'):
        a14=6
canvas.create_window((610,640), anchor='nw', window=s)


#Question 13
global name12
name12=StringVar()
canvas.create_text((15,690),anchor=NW, text="Q.13",font= (20))
e=Entry(textvariable=name12,width=50)
canvas.create_window((50,690),anchor=NW,window=e)
name12.get()

variabl14 = StringVar(root)
c24=["R","U","A"]
s=Spinbox(canvas,values=c24,textvariabl=variabl14)
def o24():
    global a15
    if(str(variabl14.get())=='R'):
        a15 = "R"

        
    elif(str(variabl14.get())=='U'):
        a15= "U"

        
    elif(str(variabl14.get())=='A'):
        a15= "A"
canvas.create_window((410,690), anchor='nw', window=s)


variabl15 = StringVar(root)
c25=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c25,textvariabl=variabl15)
def o25():
    global a16
    if(str(variabl15.get())=='2marks'):
        a16=2

        
    elif(str(variabl15.get())=='4marks'):
        a16=4

    
    elif(str(variabl15.get())=='6marks'):
        a16=6
canvas.create_window((610,690), anchor='nw', window=s)

#Question 14
global name13
name13=StringVar()
canvas.create_text((15,740),anchor=NW, text="Q.14",font= (20))
e=Entry(textvariable=name13,width=50)
canvas.create_window((50,740),anchor=NW,window=e)
name13.get()

variabl16 = StringVar(root)
c26=["R","U","A"]
s=Spinbox(canvas,values=c26,textvariabl=variabl16)
def o26():
    global a17
    if(str(variabl16.get())=='R'):
        a17 = "R"

        
    elif(str(variabl16.get())=='U'):
        a17= "U"

        
    elif(str(variabl16.get())=='A'):
        a17= "A"
canvas.create_window((410,740), anchor='nw', window=s)


variabl17 = StringVar(root)
c27=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c27,textvariabl=variabl17)
def o27():
    global a18
    if(str(variabl17.get())=='2marks'):
        a18=2

        
    elif(str(variabl17.get())=='4marks'):
        a18=4

    
    elif(str(variabl17.get())=='6marks'):
        a18=6
canvas.create_window((610,740), anchor='nw', window=s)

#Question 15
global name14
name14=StringVar()
canvas.create_text((15,790),anchor=NW, text="Q.15",font= (20))
e=Entry(textvariable=name14,width=50)
canvas.create_window((50,790),anchor=NW,window=e)
name14.get()

variabl18 = StringVar(root)
c28=["R","U","A"]
s=Spinbox(canvas,values=c28,textvariabl=variabl18)
def o28():
    global a19
    if(str(variabl18.get())=='R'):
        a19 = "R"

        
    elif(str(variabl18.get())=='U'):
        a19= "U"

        
    elif(str(variabl18.get())=='A'):
        a19= "A"
canvas.create_window((410,790), anchor='nw', window=s)


variabl19 = StringVar(root)
c29=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c29,textvariabl=variabl19)
def o29():
    global a20
    if(str(variabl19.get())=='2marks'):
        a20=2

        
    elif(str(variabl19.get())=='4marks'):
        a20=4

    
    elif(str(variabl19.get())=='6marks'):
        a20=6
canvas.create_window((610,790), anchor='nw', window=s)

#Question 16
global name15
name15=StringVar()
canvas.create_text((15,840),anchor=NW, text="Q.16",font= (20))
e=Entry(textvariable=name15,width=50)
canvas.create_window((50,840),anchor=NW,window=e)
name15.get()

variabl20 = StringVar(root)
c30=["R","U","A"]
s=Spinbox(canvas,values=c30,textvariabl=variabl20)
def o30():
    global a21
    if(str(variabl20.get())=='R'):
        a21 = "R"

        
    elif(str(variabl20.get())=='U'):
        a21= "U"

        
    elif(str(variabl20.get())=='A'):
        a21= "A"
canvas.create_window((410,840), anchor='nw', window=s)


variabl21 = StringVar(root)
c31=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c31,textvariabl=variabl21)
def o31():
    global a22
    if(str(variabl21.get())=='2marks'):
        a22=2

        
    elif(str(variabl21.get())=='4marks'):
        a22=4

    
    elif(str(variabl21.get())=='6marks'):
        a22=6
canvas.create_window((610,840), anchor='nw', window=s)

#Question 17
global name16
name16=StringVar()
canvas.create_text((15,890),anchor=NW, text="Q.17",font= (20))
e=Entry(textvariable=name16,width=50)
canvas.create_window((50,890),anchor=NW,window=e)
name16.get()

variabl22 = StringVar(root)
c32=["R","U","A"]
s=Spinbox(canvas,values=c32,textvariabl=variabl22)
def o32():
    global a23
    if(str(variabl22.get())=='R'):
        a23 = "R"

        
    elif(str(variabl22.get())=='U'):
        a23= "U"

        
    elif(str(variabl22.get())=='A'):
        a23= "A"
canvas.create_window((410,890), anchor='nw', window=s)


variabl23 = StringVar(root)
c33=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c33,textvariabl=variabl23)
def o33():
    global a24
    if(str(variabl23.get())=='2marks'):
        a24=2

        
    elif(str(variabl23.get())=='4marks'):
        a24=4

    
    elif(str(variabl23.get())=='6marks'):
        a24=6
canvas.create_window((610,890), anchor='nw', window=s)

#Question 18
global name17
name17=StringVar()
canvas.create_text((15,940),anchor=NW, text="Q.18",font= (20))
e=Entry(textvariable=name17,width=50)
canvas.create_window((50,940),anchor=NW,window=e)
name17.get()

variabl24 = StringVar(root)
c34=["R","U","A"]
s=Spinbox(canvas,values=c34,textvariabl=variabl24)
def o34():
    global a25
    if(str(variabl24.get())=='R'):
        a25 = "R"

        
    elif(str(variabl24.get())=='U'):
        a25= "U"

        
    elif(str(variabl24.get())=='A'):
        a25= "A"
canvas.create_window((410,940), anchor='nw', window=s)


variabl25 = StringVar(root)
c35=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c35,textvariabl=variabl25)
def o35():
    global a26
    if(str(variabl25.get())=='2marks'):
        a26=2

        
    elif(str(variabl25.get())=='4marks'):
        a26=4

    
    elif(str(variabl25.get())=='6marks'):
        a26=6
canvas.create_window((610,940), anchor='nw', window=s)

#Question 19
global name18
name18=StringVar()
canvas.create_text((15,990),anchor=NW, text="Q.19",font= (20))
e=Entry(textvariable=name18,width=50)
canvas.create_window((50,990),anchor=NW,window=e)
name18.get()

variabl26 = StringVar(root)
c36=["R","U","A"]
s=Spinbox(canvas,values=c36,textvariabl=variabl26)
def o36():
    global a27
    if(str(variabl26.get())=='R'):
        a27 = "R"

        
    elif(str(variabl26.get())=='U'):
        a27= "U"

        
    elif(str(variabl26.get())=='A'):
        a27= "A"
canvas.create_window((410,990), anchor='nw', window=s)


variabl27 = StringVar(root)
c37=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c37,textvariabl=variabl27)
def o37():
    global a28
    if(str(variabl27.get())=='2marks'):
        a28=2

        
    elif(str(variabl27.get())=='4marks'):
        a28=4

    
    elif(str(variabl27.get())=='6marks'):
        a28=6
canvas.create_window((610,990), anchor='nw', window=s)

#Question 20
global name19
name19=StringVar()
canvas.create_text((15,1040),anchor=NW, text="Q.20",font= (20))
e=Entry(textvariable=name19,width=50)
canvas.create_window((50,1040),anchor=NW,window=e)
name19.get()

variabl28 = StringVar(root)
c38=["R","U","A"]
s=Spinbox(canvas,values=c38,textvariabl=variabl28)
def o38():
    global a29
    if(str(variabl28.get())=='R'):
        a29 = "R"

        
    elif(str(variabl28.get())=='U'):
        a29= "U"

        
    elif(str(variabl28.get())=='A'):
        a29= "A"
canvas.create_window((410,1040), anchor='nw', window=s)


variabl29 = StringVar(root)
c39=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c39,textvariabl=variabl29)
def o39():
    global a30
    if(str(variabl29.get())=='2marks'):
        a30=2

        
    elif(str(variabl29.get())=='4marks'):
        a30=4

    
    elif(str(variabl29.get())=='6marks'):
        a30=6
canvas.create_window((610,1040), anchor='nw', window=s)

#Question 21
global name20
name20=StringVar()
canvas.create_text((15,1090),anchor=NW, text="Q.21",font= (20))
e=Entry(textvariable=name20,width=50)
canvas.create_window((50,1090),anchor=NW,window=e)
name20.get()

variabl30 = StringVar(root)
c40=["R","U","A"]
s=Spinbox(canvas,values=c40,textvariabl=variabl30)
def o40():
    global a31
    if(str(variabl30.get())=='R'):
        a31= "R"

        
    elif(str(variabl30.get())=='U'):
        a31= "U"

        
    elif(str(variabl30.get())=='A'):
        a31= "A"
canvas.create_window((410,1090), anchor='nw', window=s)


variabl31 = StringVar(root)
c41=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c41,textvariabl=variabl31)
def o41():
    global a32
    if(str(variabl31.get())=='2marks'):
        a32=2

        
    elif(str(variabl31.get())=='4marks'):
        a32=4

    
    elif(str(variabl31.get())=='6marks'):
        a32=6
canvas.create_window((610,1090), anchor='nw', window=s)


#Question 22
global name21
name21=StringVar()
canvas.create_text((15,1140),anchor=NW, text="Q.22",font= (20))
e=Entry(textvariable=name21,width=50)
canvas.create_window((50,1140),anchor=NW,window=e)
name21.get()

variabl32 = StringVar(root)
c42=["R","U","A"]
s=Spinbox(canvas,values=c42,textvariabl=variabl32)
def o42():
    global a33
    if(str(variabl32.get())=='R'):
        a33= "R"

        
    elif(str(variabl32.get())=='U'):
        a33= "U"

        
    elif(str(variabl32.get())=='A'):
        a33= "A"
canvas.create_window((410,1140), anchor='nw', window=s)


variabl33 = StringVar(root)
c43=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c43,textvariabl=variabl33)
def o43():
    global a34
    if(str(variabl33.get())=='2marks'):
        a34=2

        
    elif(str(variabl33.get())=='4marks'):
        a34=4

    
    elif(str(variabl33.get())=='6marks'):
        a34=6
canvas.create_window((610,1140), anchor='nw', window=s)


#Question 23
global name22
name22=StringVar()
canvas.create_text((15,1190),anchor=NW, text="Q.23",font= (20))
e=Entry(textvariable=name22,width=50)
canvas.create_window((50,1190),anchor=NW,window=e)
name22.get()

variabl34 = StringVar(root)
c44=["R","U","A"]
s=Spinbox(canvas,values=c44,textvariabl=variabl34)
def o44():
    global a35
    if(str(variabl34.get())=='R'):
        a35= "R"

        
    elif(str(variabl34.get())=='U'):
        a35= "U"

        
    elif(str(variabl34.get())=='A'):
        a35= "A"
canvas.create_window((410,1190), anchor='nw', window=s)


variabl35 = StringVar(root)
c45=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c45,textvariabl=variabl35)
def o45():
    global a36
    if(str(variabl35.get())=='2marks'):
        a36=2

        
    elif(str(variabl35.get())=='4marks'):
        a36=4

    
    elif(str(variabl35.get())=='6marks'):
        a36=6
canvas.create_window((610,1190), anchor='nw', window=s)

#Question 24
global name23
name23=StringVar()
canvas.create_text((15,1240),anchor=NW, text="Q.24",font= (20))
e=Entry(textvariable=name23,width=50)
canvas.create_window((50,1240),anchor=NW,window=e)
name23.get()

variabl36 = StringVar(root)
c46=["R","U","A"]
s=Spinbox(canvas,values=c46,textvariabl=variabl36)
def o46():
    global a37
    if(str(variabl36.get())=='R'):
        a37= "R"

        
    elif(str(variabl36.get())=='U'):
        a37= "U"

        
    elif(str(variabl36.get())=='A'):
        a37= "A"
canvas.create_window((410,1240), anchor='nw', window=s)


variabl37 = StringVar(root)
c47=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c47,textvariabl=variabl37)
def o47():
    global a38
    if(str(variabl37.get())=='2marks'):
        a38=2

        
    elif(str(variabl37.get())=='4marks'):
        a38=4

    
    elif(str(variabl37.get())=='6marks'):
        a38=6
canvas.create_window((610,1240), anchor='nw', window=s)

#Question 25
global name24
name24=StringVar()
canvas.create_text((15,1290),anchor=NW, text="Q.25",font= (20))
e=Entry(textvariable=name24,width=50)
canvas.create_window((50,1290),anchor=NW,window=e)
name24.get()

variabl38 = StringVar(root)
c48=["R","U","A"]
s=Spinbox(canvas,values=c48,textvariabl=variabl38)
def o48():
    global a39
    if(str(variabl38.get())=='R'):
        a39= "R"

        
    elif(str(variabl38.get())=='U'):
        a39= "U"

        
    elif(str(variabl38.get())=='A'):
        a39= "A"
canvas.create_window((410,1290), anchor='nw', window=s)


variabl39 = StringVar(root)
c49=["2marks","4marks","6marks"]
s=Spinbox(canvas,values=c49,textvariabl=variabl39)
def o49():
    global a40
    if(str(variabl39.get())=='2marks'):
        a40=2

        
    elif(str(variabl39.get())=='4marks'):
        a40=4

    
    elif(str(variabl39.get())=='6marks'):
        a40=6
canvas.create_window((610,1290), anchor='nw', window=s)

def om3():
    o()
    o1()
    o2()
    o3()
    o4()
    o5()
    o6()
    o7()
    o8()
    o9()
    o10()
    o11()
    o12()
    o13()
    o14()
    o15()
    o16()
    o17()
    o18()
    o19()
    o20()
    o21()
    o22()
    o23()
    o24()
    o25()
    o26()
    o27()
    o28()
    o29()
    o30()
    o31()
    o32()
    o33()
    o34()
    o35()
    o36()
    o37()
    o38()
    o39()
    o40()
    o41()
    o42()
    o43()
    o44()
    o45()
    o46()
    o47()
    o48()
    o49()
    database()


b=Button(canvas,text="Submit",bg="lightgreen",command=om3)
canvas.create_window((700,1350), anchor='nw', window=b)
