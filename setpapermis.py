from tkinter import *
from sqlite3 import*

import random

    
def mispaper():
    root = Tk()
    root.geometry('1500x1500')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.maxsize(w,h)


    canvas=Canvas(root,height=h,width=w,bd=2,relief=RIDGE,scrollregion=(0,0,0,2200),highlightcolor="#016193")
    canvas.place(x=0,y=0)
    scroll=Scrollbar(canvas,orient=VERTICAL)
    scroll.place(x=1335,y=10,relheight=0.965)
    scroll.config(command = canvas.yview )
    canvas.configure(yscrollcommand = scroll.set)

    a=connect('pvp.db')
    d=a.cursor()
    #chapter 1 all Questions
    d.execute("select Question from mischap1 where Type= 'R' and Marks = 2 ")
    rec=d.fetchall()    
    L1=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'R' and Marks = 4 ")
    rec=d.fetchall()    
    L2=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'R' and Marks = 6 ")
    rec=d.fetchall()    
    L3=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'U' and Marks = 2 ")
    rec=d.fetchall()    
    L4=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'U' and Marks = 4 ")
    rec=d.fetchall()    
    L5=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'U' and Marks = 6 ")
    rec=d.fetchall()    
    L6=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'A' and Marks = 2 ")
    rec=d.fetchall()    
    L7=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'A' and Marks = 4 ")
    rec=d.fetchall()    
    L8=list(sum(rec,()))
    d.execute("select Question from mischap1 where Type= 'A' and Marks = 6 ")
    rec=d.fetchall()    
    L9=list(sum(rec,()))

    #chapter 2 all Questions
    d.execute("select Question from mischap2 where Type= 'R' and Marks = 2 ")
    rec=d.fetchall()    
    L10=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'R' and Marks = 4 ")
    rec=d.fetchall()    
    L11=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'R' and Marks = 6 ")
    rec=d.fetchall()    
    L12=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'U' and Marks = 2 ")
    rec=d.fetchall()    
    L13=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'U' and Marks = 4 ")
    rec=d.fetchall()    
    L14=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'U' and Marks = 6 ")
    rec=d.fetchall()    
    L15=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'A' and Marks = 2 ")
    rec=d.fetchall()    
    L16=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'A' and Marks = 4 ")
    rec=d.fetchall()    
    L17=list(sum(rec,()))
    d.execute("select Question from mischap2 where Type= 'A' and Marks = 6 ")
    rec=d.fetchall()    
    L18=list(sum(rec,()))

    #chapter 3 all Questions
    d.execute("select Question from mischap3 where Type= 'R' and Marks = 2 ")
    rec=d.fetchall()    
    L19=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'R' and Marks = 4 ")
    rec=d.fetchall()    
    L20=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'R' and Marks = 6 ")
    rec=d.fetchall()    
    L21=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'U' and Marks = 2 ")
    rec=d.fetchall()    
    L22=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'U' and Marks = 4 ")
    rec=d.fetchall()    
    L23=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'U' and Marks = 6 ")
    rec=d.fetchall()    
    L24=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'A' and Marks = 2 ")
    rec=d.fetchall()    
    L25=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'A' and Marks = 4 ")
    rec=d.fetchall()    
    L26=list(sum(rec,()))
    d.execute("select Question from mischap3 where Type= 'A' and Marks = 6 ")
    rec=d.fetchall()    
    L27=list(sum(rec,()))

    #chapter 4 all Questions
    d.execute("select Question from mischap4 where Type= 'R' and Marks = 2 ")
    rec=d.fetchall()    
    L28=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'R' and Marks = 4 ")
    rec=d.fetchall()    
    L29=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'R' and Marks = 6 ")
    rec=d.fetchall()    
    L30=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'U' and Marks = 2 ")
    rec=d.fetchall()    
    L31=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'U' and Marks = 4 ")
    rec=d.fetchall()    
    L32=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'U' and Marks = 6 ")
    rec=d.fetchall()    
    L33=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'A' and Marks = 2 ")
    rec=d.fetchall()    
    L34=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'A' and Marks = 4 ")
    rec=d.fetchall()    
    L35=list(sum(rec,()))
    d.execute("select Question from mischap4 where Type= 'A' and Marks = 6 ")
    rec=d.fetchall()    
    L36=list(sum(rec,()))

    #chapter 5 all Questions
    d.execute("select Question from mischap5 where Type= 'R' and Marks = 2 ")
    rec=d.fetchall()    
    L37=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'R' and Marks = 4 ")
    rec=d.fetchall()    
    L38=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'R' and Marks = 6 ")
    rec=d.fetchall()    
    L39=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'U' and Marks = 2 ")
    rec=d.fetchall()    
    L40=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'U' and Marks = 4 ")
    rec=d.fetchall()    
    L41=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'U' and Marks = 6 ")
    rec=d.fetchall()    
    L42=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'A' and Marks = 2 ")
    rec=d.fetchall()    
    L43=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'A' and Marks = 4 ")
    rec=d.fetchall()    
    L44=list(sum(rec,()))
    d.execute("select Question from mischap5 where Type= 'A' and Marks = 6 ")
    rec=d.fetchall()    
    L45=list(sum(rec,()))


    #----------------------------------------Layout--------------------------------
    canvas.create_text((300,40),anchor=NW, text="GOVERNMENT POLYTECHNIC MUMBAI",font= ("bold",25))
    canvas.create_text((350,80),anchor=NW, text="TERM END EXAMINATION",font= ("bold",25))

    global acc,bc


    canvas.create_text((230,130),anchor=NW, text="Programme:",font= ("bold",15))
    acc=StringVar()
    e=Entry(canvas,textvariable=acc)
    canvas.create_window((350,136),anchor=NW,window=e)
   
    canvas.create_text((230,170),anchor=NW, text="Course Title:",font= ("bold",15))
    bc=StringVar()
    e=Entry(canvas,textvariable=bc)
    canvas.create_window((350,176),anchor=NW,window=e)


    canvas.create_text((230,210),anchor=NW, text="03Hours/70marks",font= ("bold",15))

    canvas.create_text((500,210),anchor=NW, text="Enrolment No.",font= ("bold",15))

    canvas.create_rectangle(640,210,680,230,fill="white")
    canvas.create_rectangle(680,210,720,230,fill="white")
    canvas.create_rectangle(720,210,760,230,fill="white")
    canvas.create_rectangle(760,210,800,230,fill="white")
    canvas.create_rectangle(800,210,840,230,fill="white")
    canvas.create_rectangle(840,210,880,230,fill="white")
    canvas.create_rectangle(880,210,920,230,fill="white")
    canvas.create_rectangle(920,210,960,230,fill="white")
    canvas.create_rectangle(960,210,1000,230,fill="white")

    canvas.create_line((230,250),(1050,250))

    canvas.create_text((230,260),anchor=NW, text="Instructions:",font= ("bold",14))

    canvas.create_text((230,290),anchor=NW, text="1.  Attempt all the questions.",font= ("bold",10))

    canvas.create_text((230,310),anchor=NW, text="2.  Illustrate your answer with near sketches wherever necessary.",font= ("bold",10))

    canvas.create_text((230,330),anchor=NW, text="3.  Use of Mathematical Tables,Steam Table and Pocket Calculator(non-programmable) is permissible.",font= ("bold",10))

    canvas.create_text((230,350),anchor=NW, text="4.  Marks on Right Hand Side indicate full marks for the question.",font= ("bold",10))

    canvas.create_text((230,370),anchor=NW, text="5.  Assumme suitable additional data,if necessay.",font= ("bold",10))

    canvas.create_line((230,400),(1050,400))
    #----------------------------------------------------End layout--------------------------------------------------

    
    def next1():
        print (aa3)
        from previewpython import preview
        preview(aa,aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12,aa13,aa14,aa15,aa16,aa17,aa18,aa19,aa20,aa21,aa22,aa23,aa24,aa25,aa26,aa27,aa28,aa29,aa30)
        

        
    canvas.create_text((230,420),anchor=NW, text="Q.1              Attempt any SIX                                                                             12Marks",font= ("bold",15))
    #Question 1 .a
    canvas.create_text((230,460),anchor=NW, text="   a",font= (20))
    variable = StringVar(root)
    c1=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c1,textvariabl=variable,state='readonly',wrap=True)
    def om():
        global aa
        if(str(variable.get())=='mischap1(R 2)'):
            aa=random.choice(L1)
            L1.remove(aa)
        elif(str(variable.get())=='mischap1(R 4)'):
            aa=random.choice(L2)
            L2.remove(aa)
        elif(str(variable.get())=='mischap1(R 6)'):
            aa=random.choice(L3)
            L3.remove(aa)
        elif(str(variable.get())=='mischap1(U 2)'):
            aa=random.choice(L4)
            L4.remove(aa)
        elif(str(variable.get())=='mischap1(U 4)'):
            aa=random.choice(L5)
            L5.remove(aa)
        elif(str(variable.get())=='mischap1(U 6)'):
            aa=random.choice(L6)
            L6.remove(aa)
        elif(str(variable.get())=='mischap1(A 2)'):
            aa=random.choice(L7)
            L7.remove(aa)
        elif(str(variable.get())=='mischap1(A 4)'):
            aa=random.choice(L8)
            L8.remove(aa)
        elif(str(variable.get())=='mischap1(A 6)'):
            aa=random.choice(L9)
            L9.remove(aa)
        elif(str(variable.get())=='mischap2(R 2)'):
            aa=random.choice(L10)
            L10.remove(aa)
        elif(str(variable.get())=='mischap2(R 4)'):
            aa=random.choice(L11)
            L11.remove(aa)
        elif(str(variable.get())=='mischap2(R 6)'):
            aa=random.choice(L12)
            L12.remove(aa)
        elif(str(variable.get())=='mischap2(U 2)'):
            aa=random.choice(L13)
            L13.remove(aa)
        elif(str(variable.get())=='mischap2(U 4)'):
            aa=random.choice(L14)
            L14.remove(aa)
        elif(str(variable.get())=='mischap2(U 6)'):
            aa=random.choice(L15)
            L15.remove(aa)
        elif(str(variable.get())=='mischap2(A 2)'):
            aa=random.choice(L16)
            L16.remove(aa)
        elif(str(variable.get())=='mischap2(A 4)'):
            aa=random.choice(L17)
            L17.remove(aa)
        elif(str(variable.get())=='mischap2(A 6)'):
            aa=random.choice(L18)
            L18.remove(aa)
        elif(str(variable.get())=='mischap3(R 2)'):
            aa=random.choice(L19)
            L19.remove(aa)
        elif(str(variable.get())=='mischap3(R 4)'):
            aa=random.choice(L20)
            L20.remove(aa)
        elif(str(variable.get())=='mischap3(R 6)'):
            aa=random.choice(L21)
            L21.remove(aa)
        elif(str(variable.get())=='mischap3(U 2)'):
            aa=random.choice(L22)
            L22.remove(aa)
        elif(str(variable.get())=='mischap3(U 4)'):
            aa=random.choice(L23)
            L23.remove(aa)
        elif(str(variable.get())=='mischap3(U 6)'):
            aa=random.choice(L24)
            L24.remove(aa)
        elif(str(variable.get())=='mischap3(A 2)'):
            aa=random.choice(L25)
            L25.remove(aa)
        elif(str(variable.get())=='mischap3(A 4)'):
            aa=random.choice(L26)
            L26.remove(aa)
        elif(str(variable.get())=='mischap3(A 6)'):
            aa=random.choice(L27)
            L27.remove(aa)
        elif(str(variable.get())=='mischap4(R 2)'):
            aa=random.choice(L28)
            L28.remove(aa)
        elif(str(variable.get())=='mischap4(R 4)'):
            aa=random.choice(L29)
            L29.remove(aa)
        elif(str(variable.get())=='mischap4(R 6)'):
            aa=random.choice(L30)
            L30.remove(aa)
        elif(str(variable.get())=='mischap4(U 2)'):
            aa=random.choice(L31)
            L31.remove(aa)
        elif(str(variable.get())=='mischap4(U 4)'):
            aa=random.choice(L32)
            L32.remove(aa)
        elif(str(variable.get())=='mischap4(U 6)'):
            aa=random.choice(L33)
            L33.remove(aa)
        elif(str(variable.get())=='mischap4(A 2)'):
            aa=random.choice(L34)
            L34.remove(aa)
        elif(str(variable.get())=='mischap4(A 4)'):
            aa=random.choice(L35)
            L35.remove(aa)
        elif(str(variable.get())=='mischap4(A 6)'):
            aa=random.choice(L36)
            L36.remove(aa)
        elif(str(variable.get())=='mischap5(R 2)'):
            aa=random.choice(L37)
            L37.remove(aa)
        elif(str(variable.get())=='mischap5(R 4)'):
            aa=random.choice(L38)
            L38.remove(aa)
        elif(str(variable.get())=='mischap5(R 6)'):
            aa=random.choice(L39)
            L39.remove(aa)
        elif(str(variable.get())=='mischap5(U 2)'):
            aa=random.choice(L40)
            L40.remove(aa)
        elif(str(variable.get())=='mischap5(U 4)'):
            aa=random.choice(L41)
            L41.remove(aa)
        elif(str(variable.get())=='mischap5(U 6)'):
            aa=random.choice(L42)
            L42.remove(aa)
        elif(str(variable.get())=='mischap5(A 2)'):
            aa=random.choice(L43)
            L43.remove(aa)
        elif(str(variable.get())=='mischap5(A 4)'):
            aa=random.choice(L44)
            L44.remove(aa)
        elif(str(variable.get())=='mischap5(A 6)'):
            aa=random.choice(L45)
            L45.remove(aa)
        
    canvas.create_window((300,460), anchor='nw', window=s)

    #Question 1 .b
    canvas.create_text((230,500),anchor=NW, text="   b",font= (20))
    variable1 = StringVar(root)
    c2=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c2,textvariabl=variable1,state='readonly',wrap=True)
    def om1():
        global aa1
        if(str(variable1.get())=='mischap1(R 2)'):
            aa1=random.choice(L1)
            L1.remove(aa1)
        elif(str(variable1.get())=='mischap1(R 4)'):
            aa1=random.choice(L2)
            L2.remove(aa1)
        elif(str(variable1.get())=='mischap1(R 6)'):
            aa1=random.choice(L3)
            L3.remove(aa1)
        elif(str(variable1.get())=='mischap1(U 2)'):
            aa1=random.choice(L4)
            L4.remove(aa1)
        elif(str(variable1.get())=='mischap1(U 4)'):
            aa1=random.choice(L5)
            L5.remove(aa1)
        elif(str(variable1.get())=='mischap1(U 6)'):
            aa1=random.choice(L6)
            L6.remove(aa1)
        elif(str(variable1.get())=='mischap1(A 2)'):
            aa1=random.choice(L7)
            L7.remove(aa1)
        elif(str(variable1.get())=='mischap1(A 4)'):
            aa1=random.choice(L8)
            L8.remove(aa1)
        elif(str(variable1.get())=='mischap1(A 6)'):
            aa1=random.choice(L9)
            L9.remove(aa1)
        elif(str(variable1.get())=='mischap2(R 2)'):
            aa1=random.choice(L10)
            L10.remove(aa1)
        elif(str(variable1.get())=='mischap2(R 4)'):
            aa1=random.choice(L11)
            L11.remove(aa1)
        elif(str(variable1.get())=='mischap2(R 6)'):
            aa1=random.choice(L12)
            L12.remove(aa1)
        elif(str(variable1.get())=='mischap2(U 2)'):
            aa1=random.choice(L13)
            L13.remove(aa1)
        elif(str(variable1.get())=='mischap2(U 4)'):
            aa1=random.choice(L14)
            L14.remove(aa1)
        elif(str(variable1.get())=='mischap2(U 6)'):
            aa1=random.choice(L15)
            L15.remove(aa1)
        elif(str(variable1.get())=='mischap2(A 2)'):
            aa1=random.choice(L16)
            L16.remove(aa1)
        elif(str(variable1.get())=='mischap2(A 4)'):
            aa1=random.choice(L17)
            L17.remove(aa1)
        elif(str(variable1.get())=='mischap2(A 6)'):
            aa1=random.choice(L18)
            L18.remove(aa1)
        elif(str(variable1.get())=='mischap3(R 2)'):
            aa1=random.choice(L19)
            L19.remove(aa1)
        elif(str(variable1.get())=='mischap3(R 4)'):
            aa1=random.choice(L20)
            L20.remove(aa1)
        elif(str(variable1.get())=='mischap3(R 6)'):
            aa1=random.choice(L21)
            L21.remove(aa1)
        elif(str(variable1.get())=='mischap3(U 2)'):
            aa1=random.choice(L22)
            L22.remove(aa1)
        elif(str(variable1.get())=='mischap3(U 4)'):
            aa1=random.choice(L23)
            L23.remove(aa1)
        elif(str(variable1.get())=='mischap3(U 6)'):
            aa1=random.choice(L24)
            L24.remove(aa1)
        elif(str(variable1.get())=='mischap3(A 2)'):
            aa1=random.choice(L25)
            L25.remove(aa1)
        elif(str(variable1.get())=='mischap3(A 4)'):
            aa1=random.choice(L26)
            L26.remove(aa1)
        elif(str(variable1.get())=='mischap3(A 6)'):
            aa1=random.choice(L27)
            L27.remove(aa1)
        elif(str(variable1.get())=='mischap4(R 2)'):
            aa1=random.choice(L28)
            L28.remove(aa1)
        elif(str(variable1.get())=='mischap4(R 4)'):
            aa1=random.choice(L29)
            L29.remove(aa1)
        elif(str(variable1.get())=='mischap4(R 6)'):
            aa1=random.choice(L30)
            L30.remove(aa1)
        elif(str(variable1.get())=='mischap4(U 2)'):
            aa1=random.choice(L31)
            L31.remove(aa1)
        elif(str(variable1.get())=='mischap4(U 4)'):
            aa1=random.choice(L32)
            L32.remove(aa1)
        elif(str(variable1.get())=='mischap4(U 6)'):
            aa1=random.choice(L33)
            L33.remove(aa1)
        elif(str(variable1.get())=='mischap4(A 2)'):
            aa1=random.choice(L34)
            L34.remove(aa1)
        elif(str(variable1.get())=='mischap4(A 4)'):
            aa1=random.choice(L35)
            L35.remove(aa1)
        elif(str(variable1.get())=='mischap4(A 6)'):
            aa1=random.choice(L36)
            L36.remove(aa1)
        elif(str(variable1.get())=='mischap5(R 2)'):
            aa1=random.choice(L37)
            L37.remove(aa1)
        elif(str(variable1.get())=='mischap5(R 4)'):
            aa1=random.choice(L38)
            L38.remove(aa1)
        elif(str(variable1.get())=='mischap5(R 6)'):
            aa1=random.choice(L39)
            L39.remove(aa1)
        elif(str(variable1.get())=='mischap5(U 2)'):
            aa1=random.choice(L40)
            L40.remove(aa1)
        elif(str(variable1.get())=='mischap5(U 4)'):
            aa1=random.choice(L41)
            L41.remove(aa1)
        elif(str(variable1.get())=='mischap5(U 6)'):
            aa1=random.choice(L42)
            L42.remove(aa1)
        elif(str(variable1.get())=='mischap5(A 2)'):
            aa1=random.choice(L43)
            L43.remove(aa1)
        elif(str(variable1.get())=='mischap5(A 4)'):
            aa1=random.choice(L44)
            L44.remove(aa1)
        elif(str(variable1.get())=='mischap5(A 6)'):
            aa1=random.choice(L45)
            L45.remove(aa1)
    canvas.create_window((300,500), anchor='nw', window=s)

    #Question 1 .c
    canvas.create_text((230,540),anchor=NW, text="   c",font= (20))
    variable2 = StringVar(root)
    c3=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c3,textvariabl=variable2,state='readonly',wrap=True)
    def om2():
        global aa2
        if(str(variable2.get())=='mischap1(R 2)'):
            aa2=random.choice(L1)
            L1.remove(aa2)
        elif(str(variable2.get())=='mischap1(R 4)'):
            aa2=random.choice(L2)
            L2.remove(aa2)
        elif(str(variable2.get())=='mischap1(R 6)'):
            aa2=random.choice(L3)
            L3.remove(aa2)
        elif(str(variable2.get())=='mischap1(U 2)'):
            aa2=random.choice(L4)
            L4.remove(aa2)
        elif(str(variable2.get())=='mischap1(U 4)'):
            aa2=random.choice(L5)
            L5.remove(aa2)
        elif(str(variable2.get())=='mischap1(U 6)'):
            aa2=random.choice(L6)
            L6.remove(aa2)
        elif(str(variable2.get())=='mischap1(A 2)'):
            aa2=random.choice(L7)
            L7.remove(aa2)
        elif(str(variable2.get())=='mischap1(A 4)'):
            aa2=random.choice(L8)
            L8.remove(aa2)
        elif(str(variable2.get())=='mischap1(A 6)'):
            aa2=random.choice(L9)
            L9.remove(aa2)
        elif(str(variable2.get())=='mischap2(R 2)'):
            aa2=random.choice(L10)
            L10.remove(aa2)
        elif(str(variable2.get())=='mischap2(R 4)'):
            aa2=random.choice(L11)
            L11.remove(aa2)
        elif(str(variable2.get())=='mischap2(R 6)'):
            aa2=random.choice(L12)
            L12.remove(aa2)
        elif(str(variable2.get())=='mischap2(U 2)'):
            aa2=random.choice(L13)
            L13.remove(aa2)
        elif(str(variable2.get())=='mischap2(U 4)'):
            aa2=random.choice(L14)
            L14.remove(aa2)
        elif(str(variable2.get())=='mischap2(U 6)'):
            aa2=random.choice(L15)
            L15.remove(aa2)
        elif(str(variable2.get())=='mischap2(A 2)'):
            aa2=random.choice(L16)
            L16.remove(aa2)
        elif(str(variable2.get())=='mischap2(A 4)'):
            aa2=random.choice(L17)
            L17.remove(aa2)
        elif(str(variable2.get())=='mischap2(A 6)'):
            aa2=random.choice(L18)
            L18.remove(aa2)
        elif(str(variable2.get())=='mischap3(R 2)'):
            aa2=random.choice(L19)
            L19.remove(aa2)
        elif(str(variable2.get())=='mischap3(R 4)'):
            aa2=random.choice(L20)
            L20.remove(aa2)
        elif(str(variable2.get())=='mischap3(R 6)'):
            aa2=random.choice(L21)
            L21.remove(aa2)
        elif(str(variable2.get())=='mischap3(U 2)'):
            aa2=random.choice(L22)
            L22.remove(aa2)
        elif(str(variable2.get())=='mischap3(U 4)'):
            aa2=random.choice(L23)
            L23.remove(aa2)
        elif(str(variable2.get())=='mischap3(U 6)'):
            aa2=random.choice(L24)
            L24.remove(aa2)
        elif(str(variable2.get())=='mischap3(A 2)'):
            aa2=random.choice(L25)
            L25.remove(aa2)
        elif(str(variable2.get())=='mischap3(A 4)'):
            aa2=random.choice(L26)
            L26.remove(aa2)
        elif(str(variable2.get())=='mischap3(A 6)'):
            aa2=random.choice(L27)
            L27.remove(aa2)
        elif(str(variable2.get())=='mischap4(R 2)'):
            aa2=random.choice(L28)
            L28.remove(aa2)
        elif(str(variable2.get())=='mischap4(R 4)'):
            aa2=random.choice(L29)
            L29.remove(aa2)
        elif(str(variable2.get())=='mischap4(R 6)'):
            aa2=random.choice(L30)
            L30.remove(aa2)
        elif(str(variable2.get())=='mischap4(U 2)'):
            aa2=random.choice(L31)
            L31.remove(aa2)
        elif(str(variable2.get())=='mischap4(U 4)'):
            aa2=random.choice(L32)
            L32.remove(aa2)
        elif(str(variable2.get())=='mischap4(U 6)'):
            aa2=random.choice(L33)
            L33.remove(aa2)
        elif(str(variable2.get())=='mischap4(A 2)'):
            aa2=random.choice(L34)
            L34.remove(aa2)
        elif(str(variable2.get())=='mischap4(A 4)'):
            aa2=random.choice(L35)
            L35.remove(aa2)
        elif(str(variable2.get())=='mischap4(A 6)'):
            aa2=random.choice(L36)
            L36.remove(aa2)
        elif(str(variable2.get())=='mischap5(R 2)'):
            aa2=random.choice(L37)
            L37.remove(aa2)
        elif(str(variable2.get())=='mischap5(R 4)'):
            aa2=random.choice(L38)
            L38.remove(aa2)
        elif(str(variable2.get())=='mischap5(R 6)'):
            aa2=random.choice(L39)
            L39.remove(aa2)
        elif(str(variable2.get())=='mischap5(U 2)'):
            aa2=random.choice(L40)
            L40.remove(aa2)
        elif(str(variable2.get())=='mischap5(U 4)'):
            aa2=random.choice(L41)
            L41.remove(aa2)
        elif(str(variable2.get())=='mischap5(U 6)'):
            aa2=random.choice(L42)
            L42.remove(aa2)
        elif(str(variable2.get())=='mischap5(A 2)'):
            aa2=random.choice(L43)
            L43.remove(aa2)
        elif(str(variable2.get())=='mischap5(A 4)'):
            aa2=random.choice(L44)
            L44.remove(aa2)
        elif(str(variable2.get())=='mischap5(A 6)'):
            aa2=random.choice(L45)
            L45.remove(aa2)
    canvas.create_window((300,540), anchor='nw', window=s)


    #Question 1 .d
    canvas.create_text((230,580),anchor=NW, text="   d",font= (20))
    variable3 = StringVar(root)
    c4=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c4,textvariabl=variable3,state='readonly',wrap=True)
    def om4():
        global aa3
        if(str(variable3.get())=='mischap1(R 2)'):
            aa3=random.choice(L1)
            L1.remove(aa3)
        elif(str(variable3.get())=='mischap1(R 4)'):
            aa3=random.choice(L2)
            L2.remove(aa3)
        elif(str(variable3.get())=='mischap1(R 6)'):
            aa3=random.choice(L3)
            L3.remove(aa3)
        elif(str(variable3.get())=='mischap1(U 2)'):
            aa3=random.choice(L4)
            L4.remove(aa3)
        elif(str(variable3.get())=='mischap1(U 4)'):
            aa3=random.choice(L5)
            L5.remove(aa3)
        elif(str(variable3.get())=='mischap1(U 6)'):
            aa3=random.choice(L6)
            L6.remove(aa3)
        elif(str(variable3.get())=='mischap1(A 2)'):
            aa3=random.choice(L7)
            L7.remove(aa3)
        elif(str(variable3.get())=='mischap1(A 4)'):
            aa3=random.choice(L8)
            L8.remove(aa3)
        elif(str(variable3.get())=='mischap1(A 6)'):
            aa3=random.choice(L9)
            L9.remove(aa3)
        elif(str(variable3.get())=='mischap2(R 2)'):
            aa3=random.choice(L10)
            L10.remove(aa3)
        elif(str(variable3.get())=='mischap2(R 4)'):
            aa3=random.choice(L11)
            L11.remove(aa3)
        elif(str(variable3.get())=='mischap2(R 6)'):
            aa3=random.choice(L12)
            L12.remove(aa3)
        elif(str(variable3.get())=='mischap2(U 2)'):
            aa3=random.choice(L13)
            L13.remove(aa3)
        elif(str(variable3.get())=='mischap2(U 4)'):
            aa3=random.choice(L14)
            L14.remove(aa3)
        elif(str(variable3.get())=='mischap2(U 6)'):
            aa3=random.choice(L15)
            L15.remove(aa3)
        elif(str(variable3.get())=='mischap2(A 2)'):
            aa3=random.choice(L16)
            L16.remove(aa3)
        elif(str(variable3.get())=='mischap2(A 4)'):
            aa3=random.choice(L17)
            L17.remove(aa3)
        elif(str(variable3.get())=='mischap2(A 6)'):
            aa3=random.choice(L18)
            L18.remove(aa3)
        elif(str(variable3.get())=='mischap3(R 2)'):
            aa3=random.choice(L19)
            L19.remove(aa3)
        elif(str(variable3.get())=='mischap3(R 4)'):
            aa3=random.choice(L20)
            L20.remove(aa3)
        elif(str(variable3.get())=='mischap3(R 6)'):
            aa3=random.choice(L21)
            L21.remove(aa3)
        elif(str(variable3.get())=='mischap3(U 2)'):
            aa3=random.choice(L22)
            L22.remove(aa3)
        elif(str(variable3.get())=='mischap3(U 4)'):
            aa3=random.choice(L23)
            L23.remove(aa3)
        elif(str(variable3.get())=='mischap3(U 6)'):
            aa3=random.choice(L24)
            L24.remove(aa3)
        elif(str(variable3.get())=='mischap3(A 2)'):
            aa3=random.choice(L25)
            L25.remove(aa3)
        elif(str(variable3.get())=='mischap3(A 4)'):
            aa3=random.choice(L26)
            L26.remove(aa3)
        elif(str(variable3.get())=='mischap3(A 6)'):
            aa3=random.choice(L27)
            L27.remove(aa3)
        elif(str(variable3.get())=='mischap4(R 2)'):
            aa3=random.choice(L28)
            L28.remove(aa3)
        elif(str(variable3.get())=='mischap4(R 4)'):
            aa3=random.choice(L29)
            L29.remove(aa3)
        elif(str(variable3.get())=='mischap4(R 6)'):
            aa3=random.choice(L30)
            L30.remove(aa3)
        elif(str(variable3.get())=='mischap4(U 2)'):
            aa3=random.choice(L31)
            L31.remove(aa3)
        elif(str(variable3.get())=='mischap4(U 4)'):
            aa3=random.choice(L32)
            L32.remove(aa3)
        elif(str(variable3.get())=='mischap4(U 6)'):
            aa3=random.choice(L33)
            L33.remove(aa3)
        elif(str(variable3.get())=='mischap4(A 2)'):
            aa3=random.choice(L34)
            L34.remove(aa3)
        elif(str(variable3.get())=='mischap4(A 4)'):
            aa3=random.choice(L35)
            L35.remove(aa3)
        elif(str(variable3.get())=='mischap4(A 6)'):
            aa3=random.choice(L36)
            L36.remove(aa3)
        elif(str(variable3.get())=='mischap5(R 2)'):
            aa3=random.choice(L37)
            L37.remove(aa3)
        elif(str(variable3.get())=='mischap5(R 4)'):
            aa3=random.choice(L38)
            L38.remove(aa3)
        elif(str(variable3.get())=='mischap5(R 6)'):
            aa3=random.choice(L39)
            L39.remove(aa3)
        elif(str(variable3.get())=='mischap5(U 2)'):
            aa3=random.choice(L40)
            L40.remove(aa3)
        elif(str(variable3.get())=='mischap5(U 4)'):
            aa3=random.choice(L41)
            L41.remove(aa3)
        elif(str(variable3.get())=='mischap5(U 6)'):
            aa3=random.choice(L42)
            L42.remove(aa3)
        elif(str(variable3.get())=='mischap5(A 2)'):
            aa3=random.choice(L43)
            L43.remove(aa3)
        elif(str(variable3.get())=='mischap5(A 4)'):
            aa3=random.choice(L44)
            L44.remove(aa3)
        elif(str(variable3.get())=='mischap5(A 6)'):
            aa3=random.choice(L45)
            L45.remove(aa3)
    canvas.create_window((300,580), anchor='nw', window=s)

    #Question 1 .e
    canvas.create_text((230,620),anchor=NW, text="   e",font= (20))
    variable4 = StringVar(root)
    c5=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c5,textvariabl=variable4,state='readonly',wrap=True)
    def om5():
        global aa4
        if(str(variable4.get())=='mischap1(R 2)'):
            aa4=random.choice(L1)
            L1.remove(aa4)
        elif(str(variable4.get())=='mischap1(R 4)'):
            aa4=random.choice(L2)
            L2.remove(aa4)
        elif(str(variable4.get())=='mischap1(R 6)'):
            aa4=random.choice(L3)
            L3.remove(aa4)
        elif(str(variable4.get())=='mischap1(U 2)'):
            aa4=random.choice(L4)
            L4.remove(aa4)
        elif(str(variable4.get())=='mischap1(U 4)'):
            aa4=random.choice(L5)
            L5.remove(aa4)
        elif(str(variable4.get())=='mischap1(U 6)'):
            aa4=random.choice(L6)
            L6.remove(aa4)
        elif(str(variable4.get())=='mischap1(A 2)'):
            aa4=random.choice(L7)
            L7.remove(aa4)
        elif(str(variable4.get())=='mischap1(A 4)'):
            aa4=random.choice(L8)
            L8.remove(aa4)
        elif(str(variable4.get())=='mischap1(A 6)'):
            aa4=random.choice(L9)
            L9.remove(aa4)
        elif(str(variable4.get())=='mischap2(R 2)'):
            aa4=random.choice(L10)
            L10.remove(aa4)
        elif(str(variable4.get())=='mischap2(R 4)'):
            aa4=random.choice(L11)
            L11.remove(aa4)
        elif(str(variable4.get())=='mischap2(R 6)'):
            aa4=random.choice(L12)
            L12.remove(aa4)
        elif(str(variable4.get())=='mischap2(U 2)'):
            aa4=random.choice(L13)
            L13.remove(aa4)
        elif(str(variable4.get())=='mischap2(U 4)'):
            aa4=random.choice(L14)
            L14.remove(aa4)
        elif(str(variable4.get())=='mischap2(U 6)'):
            aa4=random.choice(L15)
            L15.remove(aa4)
        elif(str(variable4.get())=='mischap2(A 2)'):
            aa4=random.choice(L16)
            L16.remove(aa4)
        elif(str(variable4.get())=='mischap2(A 4)'):
            aa4=random.choice(L17)
            L17.remove(aa4)
        elif(str(variable4.get())=='mischap2(A 6)'):
            aa4=random.choice(L18)
            L18.remove(aa4)
        elif(str(variable4.get())=='mischap3(R 2)'):
            aa4=random.choice(L19)
            L19.remove(aa4)
        elif(str(variable4.get())=='mischap3(R 4)'):
            aa4=random.choice(L20)
            L20.remove(aa4)
        elif(str(variable4.get())=='mischap3(R 6)'):
            aa4=random.choice(L21)
            L21.remove(aa4)
        elif(str(variable4.get())=='mischap3(U 2)'):
            aa4=random.choice(L22)
            L22.remove(aa4)
        elif(str(variable4.get())=='mischap3(U 4)'):
            aa4=random.choice(L23)
            L23.remove(aa4)
        elif(str(variable4.get())=='mischap3(U 6)'):
            aa4=random.choice(L24)
            L24.remove(aa4)
        elif(str(variable4.get())=='mischap3(A 2)'):
            aa4=random.choice(L25)
            L25.remove(aa4)
        elif(str(variable4.get())=='mischap3(A 4)'):
            aa4=random.choice(L26)
            L26.remove(aa4)
        elif(str(variable4.get())=='mischap3(A 6)'):
            aa4=random.choice(L27)
            L27.remove(aa4)
        elif(str(variable4.get())=='mischap4(R 2)'):
            aa4=random.choice(L28)
            L28.remove(aa4)
        elif(str(variable4.get())=='mischap4(R 4)'):
            aa4=random.choice(L29)
            L29.remove(aa4)
        elif(str(variable4.get())=='mischap4(R 6)'):
            aa4=random.choice(L30)
            L30.remove(aa4)
        elif(str(variable4.get())=='mischap4(U 2)'):
            aa4=random.choice(L31)
            L31.remove(aa4)
        elif(str(variable4.get())=='mischap4(U 4)'):
            aa4=random.choice(L32)
            L32.remove(aa4)
        elif(str(variable4.get())=='mischap4(U 6)'):
            aa4=random.choice(L33)
            L33.remove(aa4)
        elif(str(variable4.get())=='mischap4(A 2)'):
            aa4=random.choice(L34)
            L34.remove(aa4)
        elif(str(variable4.get())=='mischap4(A 4)'):
            aa4=random.choice(L35)
            L35.remove(aa4)
        elif(str(variable4.get())=='mischap4(A 6)'):
            aa4=random.choice(L36)
            L36.remove(aa4)
        elif(str(variable4.get())=='mischap5(R 2)'):
            aa4=random.choice(L37)
            L37.remove(aa4)
        elif(str(variable4.get())=='mischap5(R 4)'):
            aa4=random.choice(L38)
            L38.remove(aa4)
        elif(str(variable4.get())=='mischap5(R 6)'):
            aa4=random.choice(L39)
            L39.remove(aa4)
        elif(str(variable4.get())=='mischap5(U 2)'):
            aa4=random.choice(L40)
            L40.remove(aa4)
        elif(str(variable4.get())=='mischap5(U 4)'):
            aa4=random.choice(L41)
            L41.remove(aa4)
        elif(str(variable4.get())=='mischap5(U 6)'):
            aa4=random.choice(L42)
            L42.remove(aa4)
        elif(str(variable4.get())=='mischap5(A 2)'):
            aa4=random.choice(L43)
            L43.remove(aa4)
        elif(str(variable4.get())=='mischap5(A 4)'):
            aa4=random.choice(L44)
            L44.remove(aa4)
        elif(str(variable4.get())=='mischap5(A 6)'):
            aa4=random.choice(L45)
            L45.remove(aa4)
    canvas.create_window((300,620), anchor='nw', window=s)


    #Question 1 .f
    canvas.create_text((230,660),anchor=NW, text="   f",font= (20))
    variable5 = StringVar(root)
    c6=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c6,textvariabl=variable5,state='readonly',wrap=True)
    def om6():
        global aa5
        if(str(variable5.get())=='mischap1(R 2)'):
            aa5=random.choice(L1)
            L1.remove(aa5)
        elif(str(variable5.get())=='mischap1(R 4)'):
            aa5=random.choice(L2)
            L2.remove(aa5)
        elif(str(variable5.get())=='mischap1(R 6)'):
            aa5=random.choice(L3)
            L3.remove(aa5)
        elif(str(variable5.get())=='mischap1(U 2)'):
            aa5=random.choice(L4)
            L4.remove(aa5)
        elif(str(variable5.get())=='mischap1(U 4)'):
            aa5=random.choice(L5)
            L5.remove(aa5)
        elif(str(variable5.get())=='mischap1(U 6)'):
            aa5=random.choice(L6)
            L6.remove(aa5)
        elif(str(variable5.get())=='mischap1(A 2)'):
            aa5=random.choice(L7)
            L7.remove(aa5)
        elif(str(variable5.get())=='mischap1(A 4)'):
            aa5=random.choice(L8)
            L8.remove(aa5)
        elif(str(variable5.get())=='mischap1(A 6)'):
            aa5=random.choice(L9)
            L9.remove(aa5)
        elif(str(variable5.get())=='mischap2(R 2)'):
            aa5=random.choice(L10)
            L10.remove(aa5)
        elif(str(variable5.get())=='mischap2(R 4)'):
            aa5=random.choice(L11)
            L11.remove(aa5)
        elif(str(variable5.get())=='mischap2(R 6)'):
            aa5=random.choice(L12)
            L12.remove(aa5)
        elif(str(variable5.get())=='mischap2(U 2)'):
            aa5=random.choice(L13)
            L13.remove(aa5)
        elif(str(variable5.get())=='mischap2(U 4)'):
            aa5=random.choice(L14)
            L14.remove(aa5)
        elif(str(variable5.get())=='mischap2(U 6)'):
            aa5=random.choice(L15)
            L15.remove(aa5)
        elif(str(variable5.get())=='mischap2(A 2)'):
            aa5=random.choice(L16)
            L16.remove(aa5)
        elif(str(variable5.get())=='mischap2(A 4)'):
            aa5=random.choice(L17)
            L17.remove(aa5)
        elif(str(variable5.get())=='mischap2(A 6)'):
            aa5=random.choice(L18)
            L18.remove(aa5)
        elif(str(variable5.get())=='mischap3(R 2)'):
            aa5=random.choice(L19)
            L19.remove(aa5)
        elif(str(variable5.get())=='mischap3(R 4)'):
            aa5=random.choice(L20)
            L20.remove(aa5)
        elif(str(variable5.get())=='mischap3(R 6)'):
            aa5=random.choice(L21)
            L21.remove(aa5)
        elif(str(variable5.get())=='mischap3(U 2)'):
            aa5=random.choice(L22)
            L22.remove(aa5)
        elif(str(variable5.get())=='mischap3(U 4)'):
            aa5=random.choice(L23)
            L23.remove(aa5)
        elif(str(variable5.get())=='mischap3(U 6)'):
            aa5=random.choice(L24)
            L24.remove(aa5)
        elif(str(variable5.get())=='mischap3(A 2)'):
            aa5=random.choice(L25)
            L25.remove(aa5)
        elif(str(variable5.get())=='mischap3(A 4)'):
            aa5=random.choice(L26)
            L26.remove(aa5)
        elif(str(variable5.get())=='mischap3(A 6)'):
            aa5=random.choice(L27)
            L27.remove(aa5)
        elif(str(variable5.get())=='mischap4(R 2)'):
            aa5=random.choice(L28)
            L28.remove(aa5)
        elif(str(variable5.get())=='mischap4(R 4)'):
            aa5=random.choice(L29)
            L29.remove(aa5)
        elif(str(variable5.get())=='mischap4(R 6)'):
            aa5=random.choice(L30)
            L30.remove(aa5)
        elif(str(variable5.get())=='mischap4(U 2)'):
            aa5=random.choice(L31)
            L31.remove(aa5)
        elif(str(variable5.get())=='mischap4(U 4)'):
            aa5=random.choice(L32)
            L32.remove(aa5)
        elif(str(variable5.get())=='mischap4(U 6)'):
            aa5=random.choice(L33)
            L33.remove(aa5)
        elif(str(variable5.get())=='mischap4(A 2)'):
            aa5=random.choice(L34)
            L34.remove(aa5)
        elif(str(variable5.get())=='mischap4(A 4)'):
            aa5=random.choice(L35)
            L35.remove(aa5)
        elif(str(variable5.get())=='mischap4(A 6)'):
            aa5=random.choice(L36)
            L36.remove(aa5)
        elif(str(variable5.get())=='mischap5(R 2)'):
            aa5=random.choice(L37)
            L37.remove(aa5)
        elif(str(variable5.get())=='mischap5(R 4)'):
            aa5=random.choice(L38)
            L38.remove(aa5)
        elif(str(variable5.get())=='mischap5(R 6)'):
            aa5=random.choice(L39)
            L39.remove(aa5)
        elif(str(variable5.get())=='mischap5(U 2)'):
            aa5=random.choice(L40)
            L40.remove(aa5)
        elif(str(variable5.get())=='mischap5(U 4)'):
            aa5=random.choice(L41)
            L41.remove(aa5)
        elif(str(variable5.get())=='mischap5(U 6)'):
            aa5=random.choice(L42)
            L42.remove(aa5)
        elif(str(variable5.get())=='mischap5(A 2)'):
            aa5=random.choice(L43)
            L43.remove(aa5)
        elif(str(variable5.get())=='mischap5(A 4)'):
            aa5=random.choice(L44)
            L44.remove(aa5)
        elif(str(variable5.get())=='mischap5(A 6)'):
            aa5=random.choice(L45)
            L45.remove(aa5)

    canvas.create_window((300,660), anchor='nw', window=s)

    #Question 1 .g
    canvas.create_text((230,700),anchor=NW, text="   g",font= (20))
    variable6 = StringVar(root)
    c7=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c7,textvariabl=variable6,state='readonly',wrap=True)
    def om7():
        global aa6
        if(str(variable6.get())=='mischap1(R 2)'):
            aa6=random.choice(L1)
            L1.remove(aa6)
        elif(str(variable6.get())=='mischap1(R 4)'):
            aa6=random.choice(L2)
            L2.remove(aa6)
        elif(str(variable6.get())=='mischap1(R 6)'):
            aa6=random.choice(L3)
            L3.remove(aa6)
        elif(str(variable6.get())=='mischap1(U 2)'):
            aa6=random.choice(L4)
            L4.remove(aa6)
        elif(str(variable6.get())=='mischap1(U 4)'):
            aa6=random.choice(L5)
            L5.remove(aa6)
        elif(str(variable6.get())=='mischap1(U 6)'):
            aa6=random.choice(L6)
            L6.remove(aa6)
        elif(str(variable6.get())=='mischap1(A 2)'):
            aa6=random.choice(L7)
            L7.remove(aa6)
        elif(str(variable6.get())=='mischap1(A 4)'):
            aa6=random.choice(L8)
            L8.remove(aa6)
        elif(str(variable6.get())=='mischap1(A 6)'):
            aa6=random.choice(L9)
            L9.remove(aa6)
        elif(str(variable6.get())=='mischap2(R 2)'):
            aa6=random.choice(L10)
            L10.remove(aa6)
        elif(str(variable6.get())=='mischap2(R 4)'):
            aa6=random.choice(L11)
            L11.remove(aa6)
        elif(str(variable6.get())=='mischap2(R 6)'):
            aa6=random.choice(L12)
            L12.remove(aa6)
        elif(str(variable6.get())=='mischap2(U 2)'):
            aa6=random.choice(L13)
            L13.remove(aa6)
        elif(str(variable6.get())=='mischap2(U 4)'):
            aa6=random.choice(L14)
            L14.remove(aa6)
        elif(str(variable6.get())=='mischap2(U 6)'):
            aa6=random.choice(L15)
            L15.remove(aa6)
        elif(str(variable6.get())=='mischap2(A 2)'):
            aa6=random.choice(L16)
            L16.remove(aa6)
        elif(str(variable6.get())=='mischap2(A 4)'):
            aa6=random.choice(L17)
            L17.remove(aa6)
        elif(str(variable6.get())=='mischap2(A 6)'):
            aa6=random.choice(L18)
            L18.remove(aa6)
        elif(str(variable6.get())=='mischap3(R 2)'):
            aa6=random.choice(L19)
            L19.remove(aa6)
        elif(str(variable6.get())=='mischap3(R 4)'):
            aa6=random.choice(L20)
            L20.remove(aa6)
        elif(str(variable6.get())=='mischap3(R 6)'):
            aa6=random.choice(L21)
            L21.remove(aa6)
        elif(str(variable6.get())=='mischap3(U 2)'):
            aa6=random.choice(L22)
            L22.remove(aa6)
        elif(str(variable6.get())=='mischap3(U 4)'):
            aa6=random.choice(L23)
            L23.remove(aa6)
        elif(str(variable6.get())=='mischap3(U 6)'):
            aa6=random.choice(L24)
            L24.remove(aa6)
        elif(str(variable6.get())=='mischap3(A 2)'):
            aa6=random.choice(L25)
            L25.remove(aa6)
        elif(str(variable6.get())=='mischap3(A 4)'):
            aa6=random.choice(L26)
            L26.remove(aa6)
        elif(str(variable6.get())=='mischap3(A 6)'):
            aa6=random.choice(L27)
            L27.remove(aa6)
        elif(str(variable6.get())=='mischap4(R 2)'):
            aa6=random.choice(L28)
            L28.remove(aa6)
        elif(str(variable6.get())=='mischap4(R 4)'):
            aa6=random.choice(L29)
            L29.remove(aa6)
        elif(str(variable6.get())=='mischap4(R 6)'):
            aa6=random.choice(L30)
            L30.remove(aa6)
        elif(str(variable6.get())=='mischap4(U 2)'):
            aa6=random.choice(L31)
            L31.remove(aa6)
        elif(str(variable6.get())=='mischap4(U 4)'):
            aa6=random.choice(L32)
            L32.remove(aa6)
        elif(str(variable6.get())=='mischap4(U 6)'):
            aa6=random.choice(L33)
            L33.remove(aa6)
        elif(str(variable6.get())=='mischap4(A 2)'):
            aa6=random.choice(L34)
            L34.remove(aa6)
        elif(str(variable6.get())=='mischap4(A 4)'):
            aa6=random.choice(L35)
            L35.remove(aa6)
        elif(str(variable6.get())=='mischap4(A 6)'):
            aa6=random.choice(L36)
            L36.remove(aa6)
        elif(str(variable6.get())=='mischap5(R 2)'):
            aa6=random.choice(L37)
            L37.remove(aa6)
        elif(str(variable6.get())=='mischap5(R 4)'):
            aa6=random.choice(L38)
            L38.remove(aa6)
        elif(str(variable6.get())=='mischap5(R 6)'):
            aa6=random.choice(L39)
            L39.remove(aa6)
        elif(str(variable6.get())=='mischap5(U 2)'):
            aa6=random.choice(L40)
            L40.remove(aa6)
        elif(str(variable6.get())=='mischap5(U 4)'):
            aa6=random.choice(L41)
            L41.remove(aa6)
        elif(str(variable6.get())=='mischap5(U 6)'):
            aa6=random.choice(L42)
            L42.remove(aa6)
        elif(str(variable6.get())=='mischap5(A 2)'):
            aa6=random.choice(L43)
            L43.remove(aa6)
        elif(str(variable6.get())=='mischap5(A 4)'):
            aa6=random.choice(L44)
            L44.remove(aa6)
        elif(str(variable6.get())=='mischap5(A 6)'):
            aa6=random.choice(L45)
            L45.remove(aa6)
    canvas.create_window((300,700), anchor='nw', window=s)

#----------------------------------------------------------------------------------------------------------------------------------
#                                       question2 Start
#----------------------------------------------------------------------------------------------------------------------------------

    canvas.create_text((230,740),anchor=NW, text="Q.1              Attempt any THREE                                                                          12Marks",font= ("bold",15))
    #Question 2 .a
    canvas.create_text((230,780),anchor=NW, text="   a",font= (20))
    variable7 = StringVar(root)
    c8=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c8,textvariabl=variable7,state='readonly',wrap=True)
    def om8():
        global aa7
        if(str(variable7.get())=='mischap1(R 2)'):
            aa7=random.choice(L1)
            L1.remove(aa7)
        elif(str(variable7.get())=='mischap1(R 4)'):
            aa7=random.choice(L2)
            L2.remove(aa7)
        elif(str(variable7.get())=='mischap1(R 6)'):
            aa7=random.choice(L3)
            L3.remove(aa7)
        elif(str(variable7.get())=='mischap1(U 2)'):
            aa7=random.choice(L4)
            L4.remove(aa7)
        elif(str(variable7.get())=='mischap1(U 4)'):
            aa7=random.choice(L5)
            L5.remove(aa7)
        elif(str(variable7.get())=='mischap1(U 6)'):
            aa7=random.choice(L6)
            L6.remove(aa7)
        elif(str(variable7.get())=='mischap1(A 2)'):
            aa7=random.choice(L7)
            L7.remove(aa7)
        elif(str(variable7.get())=='mischap1(A 4)'):
            aa7=random.choice(L8)
            L8.remove(aa7)
        elif(str(variable7.get())=='mischap1(A 6)'):
            aa7=random.choice(L9)
            L9.remove(aa7)
        elif(str(variable7.get())=='mischap2(R 2)'):
            aa7=random.choice(L10)
            L10.remove(aa7)
        elif(str(variable7.get())=='mischap2(R 4)'):
            aa7=random.choice(L11)
            L11.remove(aa7)
        elif(str(variable7.get())=='mischap2(R 6)'):
            aa7=random.choice(L12)
            L12.remove(aa7)
        elif(str(variable7.get())=='mischap2(U 2)'):
            aa7=random.choice(L13)
            L13.remove(aa7)
        elif(str(variable7.get())=='mischap2(U 4)'):
            aa7=random.choice(L14)
            L14.remove(aa7)
        elif(str(variable7.get())=='mischap2(U 6)'):
            aa7=random.choice(L15)
            L15.remove(aa7)
        elif(str(variable7.get())=='mischap2(A 2)'):
            aa7=random.choice(L16)
            L16.remove(aa7)
        elif(str(variable7.get())=='mischap2(A 4)'):
            aa7=random.choice(L17)
            L17.remove(aa7)
        elif(str(variable7.get())=='mischap2(A 6)'):
            aa7=random.choice(L18)
            L18.remove(aa7)
        elif(str(variable7.get())=='mischap3(R 2)'):
            aa7=random.choice(L19)
            L19.remove(aa7)
        elif(str(variable7.get())=='mischap3(R 4)'):
            aa7=random.choice(L20)
            L20.remove(aa7)
        elif(str(variable7.get())=='mischap3(R 6)'):
            aa7=random.choice(L21)
            L21.remove(aa7)
        elif(str(variable7.get())=='mischap3(U 2)'):
            aa7=random.choice(L22)
            L22.remove(aa7)
        elif(str(variable7.get())=='mischap3(U 4)'):
            aa7=random.choice(L23)
            L23.remove(aa7)
        elif(str(variable7.get())=='mischap3(U 6)'):
            aa7=random.choice(L24)
            L24.remove(aa7)
        elif(str(variable7.get())=='mischap3(A 2)'):
            aa7=random.choice(L25)
            L25.remove(aa7)
        elif(str(variable7.get())=='mischap3(A 4)'):
            aa7=random.choice(L26)
            L26.remove(aa7)
        elif(str(variable7.get())=='mischap3(A 6)'):
            aa7=random.choice(L27)
            L27.remove(aa7)
        elif(str(variable7.get())=='mischap4(R 2)'):
            aa7=random.choice(L28)
            L28.remove(aa7)
        elif(str(variable7.get())=='mischap4(R 4)'):
            aa7=random.choice(L29)
            L29.remove(aa7)
        elif(str(variable7.get())=='mischap4(R 6)'):
            aa7=random.choice(L30)
            L30.remove(aa7)
        elif(str(variable7.get())=='mischap4(U 2)'):
            aa7=random.choice(L31)
            L31.remove(aa7)
        elif(str(variable7.get())=='mischap4(U 4)'):
            aa7=random.choice(L32)
            L32.remove(aa7)
        elif(str(variable7.get())=='mischap4(U 6)'):
            aa7=random.choice(L33)
            L33.remove(aa7)
        elif(str(variable7.get())=='mischap4(A 2)'):
            aa7=random.choice(L34)
            L34.remove(aa7)
        elif(str(variable7.get())=='mischap4(A 4)'):
            aa7=random.choice(L35)
            L35.remove(aa7)
        elif(str(variable7.get())=='mischap4(A 6)'):
            aa7=random.choice(L36)
            L36.remove(aa7)
        elif(str(variable7.get())=='mischap5(R 2)'):
            aa7=random.choice(L37)
            L37.remove(aa7)
        elif(str(variable7.get())=='mischap5(R 4)'):
            aa7=random.choice(L38)
            L38.remove(aa7)
        elif(str(variable7.get())=='mischap5(R 6)'):
            aa7=random.choice(L39)
            L39.remove(aa7)
        elif(str(variable7.get())=='mischap5(U 2)'):
            aa7=random.choice(L40)
            L40.remove(aa7)
        elif(str(variable7.get())=='mischap5(U 4)'):
            aa7=random.choice(L41)
            L41.remove(aa7)
        elif(str(variable7.get())=='mischap5(U 6)'):
            aa7=random.choice(L42)
            L42.remove(aa7)
        elif(str(variable7.get())=='mischap5(A 2)'):
            aa7=random.choice(L43)
            L43.remove(aa7)
        elif(str(variable7.get())=='mischap5(A 4)'):
            aa7=random.choice(L44)
            L44.remove(aa7)
        elif(str(variable7.get())=='mischap5(A 6)'):
            aa7=random.choice(L45)
            L45.remove(aa7)
    canvas.create_window((300,780), anchor='nw', window=s)

    #Question 2 .b
    canvas.create_text((230,820),anchor=NW, text="   b",font= (20))
    variable8 = StringVar(root)
    c9=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c9,textvariabl=variable8,state='readonly',wrap=True)
    def om9():
        global aa8
        if(str(variable8.get())=='mischap1(R 2)'):
            aa8=random.choice(L1)
            L1.remove(aa8)
        elif(str(variable8.get())=='mischap1(R 4)'):
            aa8=random.choice(L2)
            L2.remove(aa8)
        elif(str(variable8.get())=='mischap1(R 6)'):
            aa8=random.choice(L3)
            L3.remove(aa8)
        elif(str(variable8.get())=='mischap1(U 2)'):
            aa8=random.choice(L4)
            L4.remove(aa8)
        elif(str(variable8.get())=='mischap1(U 4)'):
            aa8=random.choice(L5)
            L5.remove(aa8)
        elif(str(variable8.get())=='mischap1(U 6)'):
            aa8=random.choice(L6)
            L6.remove(aa8)
        elif(str(variable8.get())=='mischap1(A 2)'):
            aa8=random.choice(L7)
            L7.remove(aa8)
        elif(str(variable8.get())=='mischap1(A 4)'):
            aa8=random.choice(L8)
            L8.remove(aa8)
        elif(str(variable8.get())=='mischap1(A 6)'):
            aa8=random.choice(L9)
            L9.remove(aa8)
        elif(str(variable8.get())=='mischap2(R 2)'):
            aa8=random.choice(L10)
            L10.remove(aa8)
        elif(str(variable8.get())=='mischap2(R 4)'):
            aa8=random.choice(L11)
            L11.remove(aa8)
        elif(str(variable8.get())=='mischap2(R 6)'):
            aa8=random.choice(L12)
            L12.remove(aa8)
        elif(str(variable8.get())=='mischap2(U 2)'):
            aa8=random.choice(L13)
            L13.remove(aa8)
        elif(str(variable8.get())=='mischap2(U 4)'):
            aa8=random.choice(L14)
            L14.remove(aa8)
        elif(str(variable8.get())=='mischap2(U 6)'):
            aa8=random.choice(L15)
            L15.remove(aa8)
        elif(str(variable8.get())=='mischap2(A 2)'):
            aa8=random.choice(L16)
            L16.remove(aa8)
        elif(str(variable8.get())=='mischap2(A 4)'):
            aa8=random.choice(L17)
            L17.remove(aa8)
        elif(str(variable8.get())=='mischap2(A 6)'):
            aa8=random.choice(L18)
            L18.remove(aa8)
        elif(str(variable8.get())=='mischap3(R 2)'):
            aa8=random.choice(L19)
            L19.remove(aa8)
        elif(str(variable8.get())=='mischap3(R 4)'):
            aa8=random.choice(L20)
            L20.remove(aa8)
        elif(str(variable8.get())=='mischap3(R 6)'):
            aa8=random.choice(L21)
            L21.remove(aa8)
        elif(str(variable8.get())=='mischap3(U 2)'):
            aa8=random.choice(L22)
            L22.remove(aa8)
        elif(str(variable8.get())=='mischap3(U 4)'):
            aa8=random.choice(L23)
            L23.remove(aa8)
        elif(str(variable8.get())=='mischap3(U 6)'):
            aa8=random.choice(L24)
            L24.remove(aa8)
        elif(str(variable8.get())=='mischap3(A 2)'):
            aa8=random.choice(L25)
            L25.remove(aa8)
        elif(str(variable8.get())=='mischap3(A 4)'):
            aa8=random.choice(L26)
            L26.remove(aa8)
        elif(str(variable8.get())=='mischap3(A 6)'):
            aa8=random.choice(L27)
            L27.remove(aa8)
        elif(str(variable8.get())=='mischap4(R 2)'):
            aa8=random.choice(L28)
            L28.remove(aa8)
        elif(str(variable8.get())=='mischap4(R 4)'):
            aa8=random.choice(L29)
            L29.remove(aa8)
        elif(str(variable8.get())=='mischap4(R 6)'):
            aa8=random.choice(L30)
            L30.remove(aa8)
        elif(str(variable8.get())=='mischap4(U 2)'):
            aa8=random.choice(L31)
            L31.remove(aa8)
        elif(str(variable8.get())=='mischap4(U 4)'):
            aa8=random.choice(L32)
            L32.remove(aa8)
        elif(str(variable8.get())=='mischap4(U 6)'):
            aa8=random.choice(L33)
            L33.remove(aa8)
        elif(str(variable8.get())=='mischap4(A 2)'):
            aa8=random.choice(L34)
            L34.remove(aa8)
        elif(str(variable8.get())=='mischap4(A 4)'):
            aa8=random.choice(L35)
            L35.remove(aa8)
        elif(str(variable8.get())=='mischap4(A 6)'):
            aa8=random.choice(L36)
            L36.remove(aa8)
        elif(str(variable8.get())=='mischap5(R 2)'):
            aa8=random.choice(L37)
            L37.remove(aa8)
        elif(str(variable8.get())=='mischap5(R 4)'):
            aa8=random.choice(L38)
            L38.remove(aa8)
        elif(str(variable8.get())=='mischap5(R 6)'):
            aa8=random.choice(L39)
            L39.remove(aa8)
        elif(str(variable8.get())=='mischap5(U 2)'):
            aa8=random.choice(L40)
            L40.remove(aa8)
        elif(str(variable8.get())=='mischap5(U 4)'):
            aa8=random.choice(L41)
            L41.remove(aa8)
        elif(str(variable8.get())=='mischap5(U 6)'):
            aa8=random.choice(L42)
            L42.remove(aa8)
        elif(str(variable8.get())=='mischap5(A 2)'):
            aa8=random.choice(L43)
            L43.remove(aa8)
        elif(str(variable8.get())=='mischap5(A 4)'):
            aa8=random.choice(L44)
            L44.remove(aa8)
        elif(str(variable8.get())=='mischap5(A 6)'):
            aa8=random.choice(L45)
            L45.remove(aa8)
    canvas.create_window((300,820), anchor='nw', window=s)

    #Question 2 .c
    canvas.create_text((230,860),anchor=NW, text="   c",font= (20))
    variable9 = StringVar(root)
    c10=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c10,textvariabl=variable9,state='readonly',wrap=True)
    def om10():
        global aa9
        if(str(variable9.get())=='mischap1(R 2)'):
            aa9=random.choice(L1)
            L1.remove(aa9)
        elif(str(variable9.get())=='mischap1(R 4)'):
            aa9=random.choice(L2)
            L2.remove(aa9)
        elif(str(variable9.get())=='mischap1(R 6)'):
            aa9=random.choice(L3)
            L3.remove(aa9)
        elif(str(variable9.get())=='mischap1(U 2)'):
            aa9=random.choice(L4)
            L4.remove(aa9)
        elif(str(variable9.get())=='mischap1(U 4)'):
            aa9=random.choice(L5)
            L5.remove(aa9)
        elif(str(variable9.get())=='mischap1(U 6)'):
            aa9=random.choice(L6)
            L6.remove(aa9)
        elif(str(variable9.get())=='mischap1(A 2)'):
            aa9=random.choice(L7)
            L7.remove(aa9)
        elif(str(variable9.get())=='mischap1(A 4)'):
            aa9=random.choice(L8)
            L8.remove(aa9)
        elif(str(variable9.get())=='mischap1(A 6)'):
            aa9=random.choice(L9)
            L9.remove(aa9)
        elif(str(variable9.get())=='mischap2(R 2)'):
            aa9=random.choice(L10)
            L10.remove(aa9)
        elif(str(variable9.get())=='mischap2(R 4)'):
            aa9=random.choice(L11)
            L11.remove(aa9)
        elif(str(variable9.get())=='mischap2(R 6)'):
            aa9=random.choice(L12)
            L12.remove(aa9)
        elif(str(variable9.get())=='mischap2(U 2)'):
            aa9=random.choice(L13)
            L13.remove(aa9)
        elif(str(variable9.get())=='mischap2(U 4)'):
            aa9=random.choice(L14)
            L14.remove(aa9)
        elif(str(variable9.get())=='mischap2(U 6)'):
            aa9=random.choice(L15)
            L15.remove(aa9)
        elif(str(variable9.get())=='mischap2(A 2)'):
            aa9=random.choice(L16)
            L16.remove(aa9)
        elif(str(variable9.get())=='mischap2(A 4)'):
            aa9=random.choice(L17)
            L17.remove(aa9)
        elif(str(variable9.get())=='mischap2(A 6)'):
            aa9=random.choice(L18)
            L18.remove(aa9)
        elif(str(variable9.get())=='mischap3(R 2)'):
            aa9=random.choice(L19)
            L19.remove(aa9)
        elif(str(variable9.get())=='mischap3(R 4)'):
            aa9=random.choice(L20)
            L20.remove(aa9)
        elif(str(variable9.get())=='mischap3(R 6)'):
            aa9=random.choice(L21)
            L21.remove(aa9)
        elif(str(variable9.get())=='mischap3(U 2)'):
            aa9=random.choice(L22)
            L22.remove(aa9)
        elif(str(variable9.get())=='mischap3(U 4)'):
            aa9=random.choice(L23)
            L23.remove(aa9)
        elif(str(variable9.get())=='mischap3(U 6)'):
            aa9=random.choice(L24)
            L24.remove(aa9)
        elif(str(variable9.get())=='mischap3(A 2)'):
            aa9=random.choice(L25)
            L25.remove(aa9)
        elif(str(variable9.get())=='mischap3(A 4)'):
            aa9=random.choice(L26)
            L26.remove(aa9)
        elif(str(variable9.get())=='mischap3(A 6)'):
            aa9=random.choice(L27)
            L27.remove(aa9)
        elif(str(variable9.get())=='mischap4(R 2)'):
            aa9=random.choice(L28)
            L28.remove(aa9)
        elif(str(variable9.get())=='mischap4(R 4)'):
            aa9=random.choice(L29)
            L29.remove(aa9)
        elif(str(variable9.get())=='mischap4(R 6)'):
            aa9=random.choice(L30)
            L30.remove(aa9)
        elif(str(variable9.get())=='mischap4(U 2)'):
            aa9=random.choice(L31)
            L31.remove(aa9)
        elif(str(variable9.get())=='mischap4(U 4)'):
            aa9=random.choice(L32)
            L32.remove(aa9)
        elif(str(variable9.get())=='mischap4(U 6)'):
            aa9=random.choice(L33)
            L33.remove(aa9)
        elif(str(variable9.get())=='mischap4(A 2)'):
            aa9=random.choice(L34)
            L34.remove(aa9)
        elif(str(variable9.get())=='mischap4(A 4)'):
            aa9=random.choice(L35)
            L35.remove(aa9)
        elif(str(variable9.get())=='mischap4(A 6)'):
            aa9=random.choice(L36)
            L36.remove(aa9)
        elif(str(variable9.get())=='mischap5(R 2)'):
            aa9=random.choice(L37)
            L37.remove(aa9)
        elif(str(variable9.get())=='mischap5(R 4)'):
            aa9=random.choice(L38)
            L38.remove(aa9)
        elif(str(variable9.get())=='mischap5(R 6)'):
            aa9=random.choice(L39)
            L39.remove(aa9)
        elif(str(variable9.get())=='mischap5(U 2)'):
            aa9=random.choice(L40)
            L40.remove(aa9)
        elif(str(variable9.get())=='mischap5(U 4)'):
            aa9=random.choice(L41)
            L41.remove(aa9)
        elif(str(variable9.get())=='mischap5(U 6)'):
            aa9=random.choice(L42)
            L42.remove(aa9)
        elif(str(variable9.get())=='mischap5(A 2)'):
            aa9=random.choice(L43)
            L43.remove(aa9)
        elif(str(variable9.get())=='mischap5(A 4)'):
            aa9=random.choice(L44)
            L44.remove(aa9)
        elif(str(variable9.get())=='mischap5(A 6)'):
            aa9=random.choice(L45)
            L45.remove(aa9)
    canvas.create_window((300,860), anchor='nw', window=s)

    #Question 2 .d
    canvas.create_text((230,900),anchor=NW, text="   d",font= (20))
    variable10 = StringVar(root)
    c11=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c11,textvariabl=variable10,state='readonly',wrap=True)
    def om11():
        global aa10
        if(str(variable10.get())=='mischap1(R 2)'):
            aa10=random.choice(L1)
            L1.remove(aa10)
        elif(str(variable10.get())=='mischap1(R 4)'):
            aa10=random.choice(L2)
            L2.remove(aa10)
        elif(str(variable10.get())=='mischap1(R 6)'):
            aa10=random.choice(L3)
            L3.remove(aa10)
        elif(str(variable10.get())=='mischap1(U 2)'):
            aa10=random.choice(L4)
            L4.remove(aa10)
        elif(str(variable10.get())=='mischap1(U 4)'):
            aa10=random.choice(L5)
            L5.remove(aa10)
        elif(str(variable10.get())=='mischap1(U 6)'):
            aa10=random.choice(L6)
            L6.remove(aa10)
        elif(str(variable10.get())=='mischap1(A 2)'):
            aa10=random.choice(L7)
            L7.remove(aa10)
        elif(str(variable10.get())=='mischap1(A 4)'):
            aa10=random.choice(L8)
            L8.remove(aa10)
        elif(str(variable10.get())=='mischap1(A 6)'):
            aa10=random.choice(L9)
            L9.remove(aa10)
        elif(str(variable10.get())=='mischap2(R 2)'):
            aa10=random.choice(L10)
            L10.remove(aa10)
        elif(str(variable10.get())=='mischap2(R 4)'):
            aa10=random.choice(L11)
            L11.remove(aa10)
        elif(str(variable10.get())=='mischap2(R 6)'):
            aa10=random.choice(L12)
            L12.remove(aa10)
        elif(str(variable10.get())=='mischap2(U 2)'):
            aa10=random.choice(L13)
            L13.remove(aa10)
        elif(str(variable10.get())=='mischap2(U 4)'):
            aa10=random.choice(L14)
            L14.remove(aa10)
        elif(str(variable10.get())=='mischap2(U 6)'):
            aa10=random.choice(L15)
            L15.remove(aa10)
        elif(str(variable10.get())=='mischap2(A 2)'):
            aa10=random.choice(L16)
            L16.remove(aa10)
        elif(str(variable10.get())=='mischap2(A 4)'):
            aa10=random.choice(L17)
            L17.remove(aa10)
        elif(str(variable10.get())=='mischap2(A 6)'):
            aa10=random.choice(L18)
            L18.remove(aa10)
        elif(str(variable10.get())=='mischap3(R 2)'):
            aa10=random.choice(L19)
            L19.remove(aa10)
        elif(str(variable10.get())=='mischap3(R 4)'):
            aa10=random.choice(L20)
            L20.remove(aa10)
        elif(str(variable10.get())=='mischap3(R 6)'):
            aa10=random.choice(L21)
            L21.remove(aa10)
        elif(str(variable10.get())=='mischap3(U 2)'):
            aa10=random.choice(L22)
            L22.remove(aa10)
        elif(str(variable10.get())=='mischap3(U 4)'):
            aa10=random.choice(L23)
            L23.remove(aa10)
        elif(str(variable10.get())=='mischap3(U 6)'):
            aa10=random.choice(L24)
            L24.remove(aa10)
        elif(str(variable10.get())=='mischap3(A 2)'):
            aa10=random.choice(L25)
            L25.remove(aa10)
        elif(str(variable10.get())=='mischap3(A 4)'):
            aa10=random.choice(L26)
            L26.remove(aa10)
        elif(str(variable10.get())=='mischap3(A 6)'):
            aa10=random.choice(L27)
            L27.remove(aa10)
        elif(str(variable10.get())=='mischap4(R 2)'):
            aa10=random.choice(L28)
            L28.remove(aa10)
        elif(str(variable10.get())=='mischap4(R 4)'):
            aa10=random.choice(L29)
            L29.remove(aa10)
        elif(str(variable10.get())=='mischap4(R 6)'):
            aa10=random.choice(L30)
            L30.remove(aa10)
        elif(str(variable10.get())=='mischap4(U 2)'):
            aa10=random.choice(L31)
            L31.remove(aa10)
        elif(str(variable10.get())=='mischap4(U 4)'):
            aa10=random.choice(L32)
            L32.remove(aa10)
        elif(str(variable10.get())=='mischap4(U 6)'):
            aa10=random.choice(L33)
            L33.remove(aa10)
        elif(str(variable10.get())=='mischap4(A 2)'):
            aa10=random.choice(L34)
            L34.remove(aa10)
        elif(str(variable10.get())=='mischap4(A 4)'):
            aa10=random.choice(L35)
            L35.remove(aa10)
        elif(str(variable10.get())=='mischap4(A 6)'):
            aa10=random.choice(L36)
            L36.remove(aa10)
        elif(str(variable10.get())=='mischap5(R 2)'):
            aa10=random.choice(L37)
            L37.remove(aa10)
        elif(str(variable10.get())=='mischap5(R 4)'):
            aa10=random.choice(L38)
            L38.remove(aa10)
        elif(str(variable10.get())=='mischap5(R 6)'):
            aa10=random.choice(L39)
            L39.remove(aa10)
        elif(str(variable10.get())=='mischap5(U 2)'):
            aa10=random.choice(L40)
            L40.remove(aa10)
        elif(str(variable10.get())=='mischap5(U 4)'):
            aa10=random.choice(L41)
            L41.remove(aa10)
        elif(str(variable10.get())=='mischap5(U 6)'):
            aa10=random.choice(L42)
            L42.remove(aa10)
        elif(str(variable10.get())=='mischap5(A 2)'):
            aa10=random.choice(L43)
            L43.remove(aa10)
        elif(str(variable10.get())=='mischap5(A 4)'):
            aa10=random.choice(L44)
            L44.remove(aa10)
        elif(str(variable10.get())=='mischap5(A 6)'):
            aa10=random.choice(L45)
            L45.remove(aa10)
    canvas.create_window((300,900), anchor='nw', window=s)

#-----------------------------------------------------------------------------------------------------------------------------
#                                                         Question3 Startf
#-------------------------------------------------------------------------------------------------------------------------------------
    canvas.create_text((230,940),anchor=NW, text="Q.3              Attempt any THREE                                                                          12Marks",font= ("bold",15))

    #Question 3 .a
    canvas.create_text((230,980),anchor=NW, text="   a",font= (20))
    variable11 = StringVar(root)
    c12=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c12,textvariabl=variable11,state='readonly',wrap=True)
    def om12():
        global aa11
        if(str(variable11.get())=='mischap1(R 2)'):
            aa11=random.choice(L1)
            L1.remove(aa11)
        elif(str(variable11.get())=='mischap1(R 4)'):
            aa11=random.choice(L2)
            L2.remove(aa11)
        elif(str(variable11.get())=='mischap1(R 6)'):
            aa11=random.choice(L3)
            L3.remove(aa11)
        elif(str(variable11.get())=='mischap1(U 2)'):
            aa11=random.choice(L4)
            L4.remove(aa11)
        elif(str(variable11.get())=='mischap1(U 4)'):
            aa11=random.choice(L5)
            L5.remove(aa11)
        elif(str(variable11.get())=='mischap1(U 6)'):
            aa11=random.choice(L6)
            L6.remove(aa11)
        elif(str(variable11.get())=='mischap1(A 2)'):
            aa11=random.choice(L7)
            L7.remove(aa11)
        elif(str(variable11.get())=='mischap1(A 4)'):
            aa11=random.choice(L8)
            L8.remove(aa11)
        elif(str(variable11.get())=='mischap1(A 6)'):
            aa11=random.choice(L9)
            L9.remove(aa11)
        elif(str(variable11.get())=='mischap2(R 2)'):
            aa11=random.choice(L10)
            L10.remove(aa11)
        elif(str(variable11.get())=='mischap2(R 4)'):
            aa11=random.choice(L11)
            L11.remove(aa11)
        elif(str(variable11.get())=='mischap2(R 6)'):
            aa11=random.choice(L12)
            L12.remove(aa11)
        elif(str(variable11.get())=='mischap2(U 2)'):
            aa11=random.choice(L13)
            L13.remove(aa11)
        elif(str(variable11.get())=='mischap2(U 4)'):
            aa11=random.choice(L14)
            L14.remove(aa11)
        elif(str(variable11.get())=='mischap2(U 6)'):
            aa11=random.choice(L15)
            L15.remove(aa11)
        elif(str(variable11.get())=='mischap2(A 2)'):
            aa11=random.choice(L16)
            L16.remove(aa11)
        elif(str(variable11.get())=='mischap2(A 4)'):
            aa11=random.choice(L17)
            L17.remove(aa11)
        elif(str(variable11.get())=='mischap2(A 6)'):
            aa11=random.choice(L18)
            L18.remove(aa11)
        elif(str(variable11.get())=='mischap3(R 2)'):
            aa11=random.choice(L19)
            L19.remove(aa11)
        elif(str(variable11.get())=='mischap3(R 4)'):
            aa11=random.choice(L20)
            L20.remove(aa11)
        elif(str(variable11.get())=='mischap3(R 6)'):
            aa11=random.choice(L21)
            L21.remove(aa11)
        elif(str(variable11.get())=='mischap3(U 2)'):
            aa11=random.choice(L22)
            L22.remove(aa11)
        elif(str(variable11.get())=='mischap3(U 4)'):
            aa11=random.choice(L23)
            L23.remove(aa11)
        elif(str(variable11.get())=='mischap3(U 6)'):
            aa11=random.choice(L24)
            L24.remove(aa11)
        elif(str(variable11.get())=='mischap3(A 2)'):
            aa11=random.choice(L25)
            L25.remove(aa11)
        elif(str(variable11.get())=='mischap3(A 4)'):
            aa11=random.choice(L26)
            L26.remove(aa11)
        elif(str(variable11.get())=='mischap3(A 6)'):
            aa11=random.choice(L27)
            L27.remove(aa11)
        elif(str(variable11.get())=='mischap4(R 2)'):
            aa11=random.choice(L28)
            L28.remove(aa11)
        elif(str(variable11.get())=='mischap4(R 4)'):
            aa11=random.choice(L29)
            L29.remove(aa11)
        elif(str(variable11.get())=='mischap4(R 6)'):
            aa11=random.choice(L30)
            L30.remove(aa11)
        elif(str(variable11.get())=='mischap4(U 2)'):
            aa11=random.choice(L31)
            L31.remove(aa11)
        elif(str(variable11.get())=='mischap4(U 4)'):
            aa11=random.choice(L32)
            L32.remove(aa11)
        elif(str(variable11.get())=='mischap4(U 6)'):
            aa11=random.choice(L33)
            L33.remove(aa11)
        elif(str(variable11.get())=='mischap4(A 2)'):
            aa11=random.choice(L34)
            L34.remove(aa11)
        elif(str(variable11.get())=='mischap4(A 4)'):
            aa11=random.choice(L35)
            L35.remove(aa11)
        elif(str(variable11.get())=='mischap4(A 6)'):
            aa11=random.choice(L36)
            L36.remove(aa11)
        elif(str(variable11.get())=='mischap5(R 2)'):
            aa11=random.choice(L37)
            L37.remove(aa11)
        elif(str(variable11.get())=='mischap5(R 4)'):
            aa11=random.choice(L38)
            L38.remove(aa11)
        elif(str(variable11.get())=='mischap5(R 6)'):
            aa11=random.choice(L39)
            L39.remove(aa11)
        elif(str(variable11.get())=='mischap5(U 2)'):
            aa11=random.choice(L40)
            L40.remove(aa11)
        elif(str(variable11.get())=='mischap5(U 4)'):
            aa11=random.choice(L41)
            L41.remove(aa11)
        elif(str(variable11.get())=='mischap5(U 6)'):
            aa11=random.choice(L42)
            L42.remove(aa11)
        elif(str(variable11.get())=='mischap5(A 2)'):
            aa11=random.choice(L43)
            L43.remove(aa11)
        elif(str(variable11.get())=='mischap5(A 4)'):
            aa11=random.choice(L44)
            L44.remove(aa11)
        elif(str(variable11.get())=='mischap5(A 6)'):
            aa11=random.choice(L45)
            L45.remove(aa11)
        elif(str(variable.get())=='pychap6(R 2)'):
            aa11=random.choice(L46)
            L46.remove(aa11)
        elif(str(variable.get())=='pychap6(R 4)'):
            aa11=random.choice(L47)
            L47.remove(aa11)
        elif(str(variable.get())=='pychap6(R 6)'):
            aa11=random.choice(L48)
            L48.remove(aa11)
        elif(str(variable.get())=='pychap6(U 2)'):
            aa11=random.choice(L49)
            L49.remove(aa11)
        elif(str(variable.get())=='pychap6(U 4)'):
            aa11=random.choice(L50)
            L50.remove(aa11)
        elif(str(variable.get())=='pychap6(U 6)'):
            aa11=random.choice(L51)
            L51.remove(aa11)
        elif(str(variable.get())=='pychap6(A 2)'):
            aa11=random.choice(L52)
            L52.remove(aa11)
        elif(str(variable.get())=='pychap6(A 4)'):
            aa11=random.choice(L53)
            L53.remove(aa11)
        elif(str(variable.get())=='pychap6(A 6)'):
            aa11=random.choice(L54)
            L54.remove(aa11)
    canvas.create_window((300,980), anchor='nw', window=s)

    #Question 3 .b
    canvas.create_text((230,1020),anchor=NW, text="   b",font= (20))
    variable12 = StringVar(root)
    c13=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c13,textvariabl=variable12,state='readonly',wrap=True)
    def om13():
        global aa12
        if(str(variable12.get())=='mischap1(R 2)'):
            aa12=random.choice(L1)
            L1.remove(aa12)
        elif(str(variable12.get())=='mischap1(R 4)'):
            aa12=random.choice(L2)
            L2.remove(aa12)
        elif(str(variable12.get())=='mischap1(R 6)'):
            aa12=random.choice(L3)
            L3.remove(aa12)
        elif(str(variable12.get())=='mischap1(U 2)'):
            aa12=random.choice(L4)
            L4.remove(aa12)
        elif(str(variable12.get())=='mischap1(U 4)'):
            aa12=random.choice(L5)
            L5.remove(aa12)
        elif(str(variable12.get())=='mischap1(U 6)'):
            aa12=random.choice(L6)
            L6.remove(aa12)
        elif(str(variable12.get())=='mischap1(A 2)'):
            aa12=random.choice(L7)
            L7.remove(aa12)
        elif(str(variable12.get())=='mischap1(A 4)'):
            aa12=random.choice(L8)
            L8.remove(aa12)
        elif(str(variable12.get())=='mischap1(A 6)'):
            aa12=random.choice(L9)
            L9.remove(aa12)
        elif(str(variable12.get())=='mischap2(R 2)'):
            aa12=random.choice(L10)
            L10.remove(aa12)
        elif(str(variable12.get())=='mischap2(R 4)'):
            aa12=random.choice(L11)
            L11.remove(aa12)
        elif(str(variable12.get())=='mischap2(R 6)'):
            aa12=random.choice(L12)
            L12.remove(aa12)
        elif(str(variable12.get())=='mischap2(U 2)'):
            aa12=random.choice(L13)
            L13.remove(aa12)
        elif(str(variable12.get())=='mischap2(U 4)'):
            aa12=random.choice(L14)
            L14.remove(aa12)
        elif(str(variable12.get())=='mischap2(U 6)'):
            aa12=random.choice(L15)
            L15.remove(aa12)
        elif(str(variable12.get())=='mischap2(A 2)'):
            aa12=random.choice(L16)
            L16.remove(aa12)
        elif(str(variable12.get())=='mischap2(A 4)'):
            aa12=random.choice(L17)
            L17.remove(aa12)
        elif(str(variable12.get())=='mischap2(A 6)'):
            aa12=random.choice(L18)
            L18.remove(aa12)
        elif(str(variable12.get())=='mischap3(R 2)'):
            aa12=random.choice(L19)
            L19.remove(aa12)
        elif(str(variable12.get())=='mischap3(R 4)'):
            aa12=random.choice(L20)
            L20.remove(aa12)
        elif(str(variable12.get())=='mischap3(R 6)'):
            aa12=random.choice(L21)
            L21.remove(aa12)
        elif(str(variable12.get())=='mischap3(U 2)'):
            aa12=random.choice(L22)
            L22.remove(aa12)
        elif(str(variable12.get())=='mischap3(U 4)'):
            aa12=random.choice(L23)
            L23.remove(aa12)
        elif(str(variable12.get())=='mischap3(U 6)'):
            aa12=random.choice(L24)
            L24.remove(aa12)
        elif(str(variable12.get())=='mischap3(A 2)'):
            aa12=random.choice(L25)
            L25.remove(aa12)
        elif(str(variable12.get())=='mischap3(A 4)'):
            aa12=random.choice(L26)
            L26.remove(aa12)
        elif(str(variable12.get())=='mischap3(A 6)'):
            aa12=random.choice(L27)
            L27.remove(aa12)
        elif(str(variable12.get())=='mischap4(R 2)'):
            aa12=random.choice(L28)
            L28.remove(aa12)
        elif(str(variable12.get())=='mischap4(R 4)'):
            aa12=random.choice(L29)
            L29.remove(aa12)
        elif(str(variable12.get())=='mischap4(R 6)'):
            aa12=random.choice(L30)
            L30.remove(aa12)
        elif(str(variable12.get())=='mischap4(U 2)'):
            aa12=random.choice(L31)
            L31.remove(aa12)
        elif(str(variable12.get())=='mischap4(U 4)'):
            aa12=random.choice(L32)
            L32.remove(aa12)
        elif(str(variable12.get())=='mischap4(U 6)'):
            aa12=random.choice(L33)
            L33.remove(aa12)
        elif(str(variable12.get())=='mischap4(A 2)'):
            aa12=random.choice(L34)
            L34.remove(aa12)
        elif(str(variable12.get())=='mischap4(A 4)'):
            aa12=random.choice(L35)
            L35.remove(aa12)
        elif(str(variable12.get())=='mischap4(A 6)'):
            aa12=random.choice(L36)
            L36.remove(aa12)
        elif(str(variable12.get())=='mischap5(R 2)'):
            aa12=random.choice(L37)
            L37.remove(aa12)
        elif(str(variable12.get())=='mischap5(R 4)'):
            aa12=random.choice(L38)
            L38.remove(aa12)
        elif(str(variable12.get())=='mischap5(R 6)'):
            aa12=random.choice(L39)
            L39.remove(aa12)
        elif(str(variable12.get())=='mischap5(U 2)'):
            aa12=random.choice(L40)
            L40.remove(aa12)
        elif(str(variable12.get())=='mischap5(U 4)'):
            aa12=random.choice(L41)
            L41.remove(aa12)
        elif(str(variable12.get())=='mischap5(U 6)'):
            aa12=random.choice(L42)
            L42.remove(aa12)
        elif(str(variable12.get())=='mischap5(A 2)'):
            aa12=random.choice(L43)
            L43.remove(aa12)
        elif(str(variable12.get())=='mischap5(A 4)'):
            aa12=random.choice(L44)
            L44.remove(aa12)
        elif(str(variable12.get())=='mischap5(A 6)'):
            aa12=random.choice(L45)
            L45.remove(aa12)
    canvas.create_window((300,1020), anchor='nw', window=s)

    #Question 3 .c
    canvas.create_text((230,1060),anchor=NW, text="   c",font= (20))
    variable13 = StringVar(root)
    c14=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c14,textvariabl=variable13,state='readonly',wrap=True)
    def om14():
        global aa13
        if(str(variable13.get())=='mischap1(R 2)'):
            aa13=random.choice(L1)
            L1.remove(aa13)
        elif(str(variable13.get())=='mischap1(R 4)'):
            aa13=random.choice(L2)
            L2.remove(aa13)
        elif(str(variable13.get())=='mischap1(R 6)'):
            aa13=random.choice(L3)
            L3.remove(aa13)
        elif(str(variable13.get())=='mischap1(U 2)'):
            aa13=random.choice(L4)
            L4.remove(aa13)
        elif(str(variable13.get())=='mischap1(U 4)'):
            aa13=random.choice(L5)
            L5.remove(aa13)
        elif(str(variable13.get())=='mischap1(U 6)'):
            aa13=random.choice(L6)
            L6.remove(aa13)
        elif(str(variable13.get())=='mischap1(A 2)'):
            aa13=random.choice(L7)
            L7.remove(aa13)
        elif(str(variable13.get())=='mischap1(A 4)'):
            aa13=random.choice(L8)
            L8.remove(aa13)
        elif(str(variable13.get())=='mischap1(A 6)'):
            aa13=random.choice(L9)
            L9.remove(aa13)
        elif(str(variable13.get())=='mischap2(R 2)'):
            aa13=random.choice(L10)
            L10.remove(aa13)
        elif(str(variable13.get())=='mischap2(R 4)'):
            aa13=random.choice(L11)
            L11.remove(aa13)
        elif(str(variable13.get())=='mischap2(R 6)'):
            aa13=random.choice(L12)
            L12.remove(aa13)
        elif(str(variable13.get())=='mischap2(U 2)'):
            aa13=random.choice(L13)
            L13.remove(aa13)
        elif(str(variable13.get())=='mischap2(U 4)'):
            aa13=random.choice(L14)
            L14.remove(aa13)
        elif(str(variable13.get())=='mischap2(U 6)'):
            aa13=random.choice(L15)
            L15.remove(aa13)
        elif(str(variable13.get())=='mischap2(A 2)'):
            aa13=random.choice(L16)
            L16.remove(aa13)
        elif(str(variable13.get())=='mischap2(A 4)'):
            aa13=random.choice(L17)
            L17.remove(aa13)
        elif(str(variable13.get())=='mischap2(A 6)'):
            aa13=random.choice(L18)
            L18.remove(aa13)
        elif(str(variable13.get())=='mischap3(R 2)'):
            aa13=random.choice(L19)
            L19.remove(aa13)
        elif(str(variable13.get())=='mischap3(R 4)'):
            aa13=random.choice(L20)
            L20.remove(aa13)
        elif(str(variable13.get())=='mischap3(R 6)'):
            aa13=random.choice(L21)
            L21.remove(aa13)
        elif(str(variable13.get())=='mischap3(U 2)'):
            aa13=random.choice(L22)
            L22.remove(aa13)
        elif(str(variable13.get())=='mischap3(U 4)'):
            aa13=random.choice(L23)
            L23.remove(aa13)
        elif(str(variable13.get())=='mischap3(U 6)'):
            aa13=random.choice(L24)
            L24.remove(aa13)
        elif(str(variable13.get())=='mischap3(A 2)'):
            aa13=random.choice(L25)
            L25.remove(aa13)
        elif(str(variable13.get())=='mischap3(A 4)'):
            aa13=random.choice(L26)
            L26.remove(aa13)
        elif(str(variable13.get())=='mischap3(A 6)'):
            aa13=random.choice(L27)
            L27.remove(aa13)
        elif(str(variable13.get())=='mischap4(R 2)'):
            aa13=random.choice(L28)
            L28.remove(aa13)
        elif(str(variable13.get())=='mischap4(R 4)'):
            aa13=random.choice(L29)
            L29.remove(aa13)
        elif(str(variable13.get())=='mischap4(R 6)'):
            aa13=random.choice(L30)
            L30.remove(aa13)
        elif(str(variable13.get())=='mischap4(U 2)'):
            aa13=random.choice(L31)
            L31.remove(aa13)
        elif(str(variable13.get())=='mischap4(U 4)'):
            aa13=random.choice(L32)
            L32.remove(aa13)
        elif(str(variable13.get())=='mischap4(U 6)'):
            aa13=random.choice(L33)
            L33.remove(aa13)
        elif(str(variable13.get())=='mischap4(A 2)'):
            aa13=random.choice(L34)
            L34.remove(aa13)
        elif(str(variable13.get())=='mischap4(A 4)'):
            aa13=random.choice(L35)
            L35.remove(aa13)
        elif(str(variable13.get())=='mischap4(A 6)'):
            aa13=random.choice(L36)
            L36.remove(aa13)
        elif(str(variable13.get())=='mischap5(R 2)'):
            aa13=random.choice(L37)
            L37.remove(aa13)
        elif(str(variable13.get())=='mischap5(R 4)'):
            aa13=random.choice(L38)
            L38.remove(aa13)
        elif(str(variable13.get())=='mischap5(R 6)'):
            aa13=random.choice(L39)
            L39.remove(aa13)
        elif(str(variable13.get())=='mischap5(U 2)'):
            aa13=random.choice(L40)
            L40.remove(aa13)
        elif(str(variable13.get())=='mischap5(U 4)'):
            aa13=random.choice(L41)
            L41.remove(aa13)
        elif(str(variable13.get())=='mischap5(U 6)'):
            aa13=random.choice(L42)
            L42.remove(aa13)
        elif(str(variable13.get())=='mischap5(A 2)'):
            aa13=random.choice(L43)
            L43.remove(aa13)
        elif(str(variable13.get())=='mischap5(A 4)'):
            aa13=random.choice(L44)
            L44.remove(aa13)
        elif(str(variable13.get())=='mischap5(A 6)'):
            aa13=random.choice(L45)
            L45.remove(aa13)
    canvas.create_window((300,1060), anchor='nw', window=s)

    #Question 3 .d
    canvas.create_text((230,1100),anchor=NW, text="   d",font= (20))
    variable14 = StringVar(root)
    c15=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)","pychap6(R 2)","pychap6(R 4)","pychap6(R 6)","pychap6(U 2)","pychap6(U 4)","pychap6(U 6)","pychap6(A 2)","pychap6(A 4)","pychap6(A 6)"]
    s=Spinbox(canvas,values=c15,textvariabl=variable14,state='readonly',wrap=True)
    def om15():
        global aa14
        if(str(variable14.get())=='mischap1(R 2)'):
            aa14=random.choice(L1)
            L1.remove(aa14)
        elif(str(variable14.get())=='mischap1(R 4)'):
            aa14=random.choice(L2)
            L2.remove(aa14)
        elif(str(variable14.get())=='mischap1(R 6)'):
            aa14=random.choice(L3)
            L3.remove(aa14)
        elif(str(variable14.get())=='mischap1(U 2)'):
            aa14=random.choice(L4)
            L4.remove(aa14)
        elif(str(variable14.get())=='mischap1(U 4)'):
            aa14=random.choice(L5)
            L5.remove(aa14)
        elif(str(variable14.get())=='mischap1(U 6)'):
            aa14=random.choice(L6)
            L6.remove(aa14)
        elif(str(variable14.get())=='mischap1(A 2)'):
            aa14=random.choice(L7)
            L7.remove(aa14)
        elif(str(variable14.get())=='mischap1(A 4)'):
            aa14=random.choice(L8)
            L8.remove(aa14)
        elif(str(variable14.get())=='mischap1(A 6)'):
            aa14=random.choice(L9)
            L9.remove(aa14)
        elif(str(variable14.get())=='mischap2(R 2)'):
            aa14=random.choice(L10)
            L10.remove(aa14)
        elif(str(variable14.get())=='mischap2(R 4)'):
            aa14=random.choice(L11)
            L11.remove(aa14)
        elif(str(variable14.get())=='mischap2(R 6)'):
            aa14=random.choice(L12)
            L12.remove(aa14)
        elif(str(variable14.get())=='mischap2(U 2)'):
            aa14=random.choice(L13)
            L13.remove(aa14)
        elif(str(variable14.get())=='mischap2(U 4)'):
            aa14=random.choice(L14)
            L14.remove(aa14)
        elif(str(variable14.get())=='mischap2(U 6)'):
            aa14=random.choice(L15)
            L15.remove(aa14)
        elif(str(variable14.get())=='mischap2(A 2)'):
            aa14=random.choice(L16)
            L16.remove(aa14)
        elif(str(variable14.get())=='mischap2(A 4)'):
            aa14=random.choice(L17)
            L17.remove(aa14)
        elif(str(variable14.get())=='mischap2(A 6)'):
            aa14=random.choice(L18)
            L18.remove(aa14)
        elif(str(variable14.get())=='mischap3(R 2)'):
            aa14=random.choice(L19)
            L19.remove(aa14)
        elif(str(variable14.get())=='mischap3(R 4)'):
            aa14=random.choice(L20)
            L20.remove(aa14)
        elif(str(variable14.get())=='mischap3(R 6)'):
            aa14=random.choice(L21)
            L21.remove(aa14)
        elif(str(variable14.get())=='mischap3(U 2)'):
            aa14=random.choice(L22)
            L22.remove(aa14)
        elif(str(variable14.get())=='mischap3(U 4)'):
            aa14=random.choice(L23)
            L23.remove(aa14)
        elif(str(variable14.get())=='mischap3(U 6)'):
            aa14=random.choice(L24)
            L24.remove(aa14)
        elif(str(variable14.get())=='mischap3(A 2)'):
            aa14=random.choice(L25)
            L25.remove(aa14)
        elif(str(variable14.get())=='mischap3(A 4)'):
            aa14=random.choice(L26)
            L26.remove(aa14)
        elif(str(variable14.get())=='mischap3(A 6)'):
            aa14=random.choice(L27)
            L27.remove(aa14)
        elif(str(variable14.get())=='mischap4(R 2)'):
            aa14=random.choice(L28)
            L28.remove(aa14)
        elif(str(variable14.get())=='mischap4(R 4)'):
            aa14=random.choice(L29)
            L29.remove(aa14)
        elif(str(variable14.get())=='mischap4(R 6)'):
            aa14=random.choice(L30)
            L30.remove(aa14)
        elif(str(variable14.get())=='mischap4(U 2)'):
            aa14=random.choice(L31)
            L31.remove(aa14)
        elif(str(variable14.get())=='mischap4(U 4)'):
            aa14=random.choice(L32)
            L32.remove(aa14)
        elif(str(variable14.get())=='mischap4(U 6)'):
            aa14=random.choice(L33)
            L33.remove(aa14)
        elif(str(variable14.get())=='mischap4(A 2)'):
            aa14=random.choice(L34)
            L34.remove(aa14)
        elif(str(variable14.get())=='mischap4(A 4)'):
            aa14=random.choice(L35)
            L35.remove(aa14)
        elif(str(variable14.get())=='mischap4(A 6)'):
            aa14=random.choice(L36)
            L36.remove(aa14)
        elif(str(variable14.get())=='mischap5(R 2)'):
            aa14=random.choice(L37)
            L37.remove(aa14)
        elif(str(variable14.get())=='mischap5(R 4)'):
            aa14=random.choice(L38)
            L38.remove(aa14)
        elif(str(variable14.get())=='mischap5(R 6)'):
            aa14=random.choice(L39)
            L39.remove(aa14)
        elif(str(variable14.get())=='mischap5(U 2)'):
            aa14=random.choice(L40)
            L40.remove(aa14)
        elif(str(variable14.get())=='mischap5(U 4)'):
            aa14=random.choice(L41)
            L41.remove(aa14)
        elif(str(variable14.get())=='mischap5(U 6)'):
            aa14=random.choice(L42)
            L42.remove(aa14)
        elif(str(variable14.get())=='mischap5(A 2)'):
            aa14=random.choice(L43)
            L43.remove(aa14)
        elif(str(variable14.get())=='mischap5(A 4)'):
            aa14=random.choice(L44)
            L44.remove(aa14)
        elif(str(variable14.get())=='mischap5(A 6)'):
            aa14=random.choice(L45)
            L45.remove(aa14)

    canvas.create_window((300,1100), anchor='nw', window=s)

    #Question 3 .e
    canvas.create_text((230,1140),anchor=NW, text="   e",font= (20))
    variable15 = StringVar(root)
    c16=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c15,textvariabl=variable15,state='readonly',wrap=True)
    def om16():
        global aa15
        if(str(variable15.get())=='mischap1(R 2)'):
            aa15=random.choice(L1)
            L1.remove(aa15)
        elif(str(variable15.get())=='mischap1(R 4)'):
            aa15=random.choice(L2)
            L2.remove(aa15)
        elif(str(variable15.get())=='mischap1(R 6)'):
            aa15=random.choice(L3)
            L3.remove(aa15)
        elif(str(variable15.get())=='mischap1(U 2)'):
            aa15=random.choice(L4)
            L4.remove(aa15)
        elif(str(variable15.get())=='mischap1(U 4)'):
            aa15=random.choice(L5)
            L5.remove(aa15)
        elif(str(variable15.get())=='mischap1(U 6)'):
            aa15=random.choice(L6)
            L6.remove(aa15)
        elif(str(variable15.get())=='mischap1(A 2)'):
            aa15=random.choice(L7)
            L7.remove(aa15)
        elif(str(variable15.get())=='mischap1(A 4)'):
            aa15=random.choice(L8)
            L8.remove(aa15)
        elif(str(variable15.get())=='mischap1(A 6)'):
            aa15=random.choice(L9)
            L9.remove(aa15)
        elif(str(variable15.get())=='mischap2(R 2)'):
            aa15=random.choice(L10)
            L10.remove(aa15)
        elif(str(variable15.get())=='mischap2(R 4)'):
            aa15=random.choice(L11)
            L11.remove(aa15)
        elif(str(variable15.get())=='mischap2(R 6)'):
            aa15=random.choice(L12)
            L12.remove(aa15)
        elif(str(variable15.get())=='mischap2(U 2)'):
            aa15=random.choice(L13)
            L13.remove(aa15)
        elif(str(variable15.get())=='mischap2(U 4)'):
            aa15=random.choice(L14)
            L14.remove(aa15)
        elif(str(variable15.get())=='mischap2(U 6)'):
            aa15=random.choice(L15)
            L15.remove(aa15)
        elif(str(variable15.get())=='mischap2(A 2)'):
            aa15=random.choice(L16)
            L16.remove(aa15)
        elif(str(variable15.get())=='mischap2(A 4)'):
            aa15=random.choice(L17)
            L17.remove(aa15)
        elif(str(variable15.get())=='mischap2(A 6)'):
            aa15=random.choice(L18)
            L18.remove(aa15)
        elif(str(variable15.get())=='mischap3(R 2)'):
            aa15=random.choice(L19)
            L19.remove(aa15)
        elif(str(variable15.get())=='mischap3(R 4)'):
            aa15=random.choice(L20)
            L20.remove(aa15)
        elif(str(variable15.get())=='mischap3(R 6)'):
            aa15=random.choice(L21)
            L21.remove(aa15)
        elif(str(variable15.get())=='mischap3(U 2)'):
            aa15=random.choice(L22)
            L22.remove(aa15)
        elif(str(variable15.get())=='mischap3(U 4)'):
            aa15=random.choice(L23)
            L23.remove(aa15)
        elif(str(variable15.get())=='mischap3(U 6)'):
            aa15=random.choice(L24)
            L24.remove(aa15)
        elif(str(variable15.get())=='mischap3(A 2)'):
            aa15=random.choice(L25)
            L25.remove(aa15)
        elif(str(variable15.get())=='mischap3(A 4)'):
            aa15=random.choice(L26)
            L26.remove(aa15)
        elif(str(variable15.get())=='mischap3(A 6)'):
            aa15=random.choice(L27)
            L27.remove(aa15)
        elif(str(variable15.get())=='mischap4(R 2)'):
            aa15=random.choice(L28)
            L28.remove(aa15)
        elif(str(variable15.get())=='mischap4(R 4)'):
            aa15=random.choice(L29)
            L29.remove(aa15)
        elif(str(variable15.get())=='mischap4(R 6)'):
            aa15=random.choice(L30)
            L30.remove(aa15)
        elif(str(variable15.get())=='mischap4(U 2)'):
            aa15=random.choice(L31)
            L31.remove(aa15)
        elif(str(variable15.get())=='mischap4(U 4)'):
            aa15=random.choice(L32)
            L32.remove(aa15)
        elif(str(variable15.get())=='mischap4(U 6)'):
            aa15=random.choice(L33)
            L33.remove(aa15)
        elif(str(variable15.get())=='mischap4(A 2)'):
            aa15=random.choice(L34)
            L34.remove(aa15)
        elif(str(variable15.get())=='mischap4(A 4)'):
            aa15=random.choice(L35)
            L35.remove(aa15)
        elif(str(variable15.get())=='mischap4(A 6)'):
            aa15=random.choice(L36)
            L36.remove(aa15)
        elif(str(variable15.get())=='mischap5(R 2)'):
            aa15=random.choice(L37)
            L37.remove(aa15)
        elif(str(variable15.get())=='mischap5(R 4)'):
            aa15=random.choice(L38)
            L38.remove(aa15)
        elif(str(variable15.get())=='mischap5(R 6)'):
            aa15=random.choice(L39)
            L39.remove(aa15)
        elif(str(variable15.get())=='mischap5(U 2)'):
            aa15=random.choice(L40)
            L40.remove(aa15)
        elif(str(variable15.get())=='mischap5(U 4)'):
            aa15=random.choice(L41)
            L41.remove(aa15)
        elif(str(variable15.get())=='mischap5(U 6)'):
            aa15=random.choice(L42)
            L42.remove(aa15)
        elif(str(variable15.get())=='mischap5(A 2)'):
            aa15=random.choice(L43)
            L43.remove(aa15)
        elif(str(variable15.get())=='mischap5(A 4)'):
            aa15=random.choice(L44)
            L44.remove(aa15)
        elif(str(variable15.get())=='mischap5(A 6)'):
            aa15=random.choice(L45)
            L45.remove(aa15)
    canvas.create_window((300,1140), anchor='nw', window=s)

#-----------------------------------------------------------------------------------------------------------------------------
#                                                         Question4 Start
#-------------------------------------------------------------------------------------------------------------------------------------
    canvas.create_text((230,1180),anchor=NW, text="Q.4              Attempt any FIVE                                                                          10Marks",font= ("bold",15))
        #Question 4 .a
    canvas.create_text((230,1220),anchor=NW, text="   a",font= (20))
    variable16 = StringVar(root)
    c17=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c17,textvariabl=variable16,state='readonly',wrap=True)
    def om17():
        global aa16
        if(str(variable16.get())=='mischap1(R 2)'):
            aa16=random.choice(L1)
            L1.remove(aa16)
        elif(str(variable16.get())=='mischap1(R 4)'):
            aa16=random.choice(L2)
            L2.remove(aa16)
        elif(str(variable16.get())=='mischap1(R 6)'):
            aa16=random.choice(L3)
            L3.remove(aa16)
        elif(str(variable16.get())=='mischap1(U 2)'):
            aa16=random.choice(L4)
            L4.remove(aa16)
        elif(str(variable16.get())=='mischap1(U 4)'):
            aa16=random.choice(L5)
            L5.remove(aa16)
        elif(str(variable16.get())=='mischap1(U 6)'):
            aa16=random.choice(L6)
            L6.remove(aa16)
        elif(str(variable16.get())=='mischap1(A 2)'):
            aa16=random.choice(L7)
            L7.remove(aa16)
        elif(str(variable16.get())=='mischap1(A 4)'):
            aa16=random.choice(L8)
            L8.remove(aa16)
        elif(str(variable16.get())=='mischap1(A 6)'):
            aa16=random.choice(L9)
            L9.remove(aa16)
        elif(str(variable16.get())=='mischap2(R 2)'):
            aa16=random.choice(L10)
            L10.remove(aa16)
        elif(str(variable16.get())=='mischap2(R 4)'):
            aa16=random.choice(L11)
            L11.remove(aa16)
        elif(str(variable16.get())=='mischap2(R 6)'):
            aa16=random.choice(L12)
            L12.remove(aa16)
        elif(str(variable16.get())=='mischap2(U 2)'):
            aa16=random.choice(L13)
            L13.remove(aa16)
        elif(str(variable16.get())=='mischap2(U 4)'):
            aa16=random.choice(L14)
            L14.remove(aa16)
        elif(str(variable16.get())=='mischap2(U 6)'):
            aa16=random.choice(L15)
            L15.remove(aa16)
        elif(str(variable16.get())=='mischap2(A 2)'):
            aa16=random.choice(L16)
            L16.remove(aa16)
        elif(str(variable16.get())=='mischap2(A 4)'):
            aa16=random.choice(L17)
            L17.remove(aa16)
        elif(str(variable16.get())=='mischap2(A 6)'):
            aa16=random.choice(L18)
            L18.remove(aa16)
        elif(str(variable16.get())=='mischap3(R 2)'):
            aa16=random.choice(L19)
            L19.remove(aa16)
        elif(str(variable16.get())=='mischap3(R 4)'):
            aa16=random.choice(L20)
            L20.remove(aa16)
        elif(str(variable16.get())=='mischap3(R 6)'):
            aa16=random.choice(L21)
            L21.remove(aa16)
        elif(str(variable16.get())=='mischap3(U 2)'):
            aa16=random.choice(L22)
            L22.remove(aa16)
        elif(str(variable16.get())=='mischap3(U 4)'):
            aa16=random.choice(L23)
            L23.remove(aa16)
        elif(str(variable16.get())=='mischap3(U 6)'):
            aa16=random.choice(L24)
            L24.remove(aa16)
        elif(str(variable16.get())=='mischap3(A 2)'):
            aa16=random.choice(L25)
            L25.remove(aa16)
        elif(str(variable16.get())=='mischap3(A 4)'):
            aa16=random.choice(L26)
            L26.remove(aa16)
        elif(str(variable16.get())=='mischap3(A 6)'):
            aa16=random.choice(L27)
            L27.remove(aa16)
        elif(str(variable16.get())=='mischap4(R 2)'):
            aa16=random.choice(L28)
            L28.remove(aa16)
        elif(str(variable16.get())=='mischap4(R 4)'):
            aa16=random.choice(L29)
            L29.remove(aa16)
        elif(str(variable16.get())=='mischap4(R 6)'):
            aa16=random.choice(L30)
            L30.remove(aa16)
        elif(str(variable16.get())=='mischap4(U 2)'):
            aa16=random.choice(L31)
            L31.remove(aa16)
        elif(str(variable16.get())=='mischap4(U 4)'):
            aa16=random.choice(L32)
            L32.remove(aa16)
        elif(str(variable16.get())=='mischap4(U 6)'):
            aa16=random.choice(L33)
            L33.remove(aa16)
        elif(str(variable16.get())=='mischap4(A 2)'):
            aa16=random.choice(L34)
            L34.remove(aa16)
        elif(str(variable16.get())=='mischap4(A 4)'):
            aa16=random.choice(L35)
            L35.remove(aa16)
        elif(str(variable16.get())=='mischap4(A 6)'):
            aa16=random.choice(L36)
            L36.remove(aa16)
        elif(str(variable16.get())=='mischap5(R 2)'):
            aa16=random.choice(L37)
            L37.remove(aa16)
        elif(str(variable16.get())=='mischap5(R 4)'):
            aa16=random.choice(L38)
            L38.remove(aa16)
        elif(str(variable16.get())=='mischap5(R 6)'):
            aa16=random.choice(L39)
            L39.remove(aa16)
        elif(str(variable16.get())=='mischap5(U 2)'):
            aa16=random.choice(L40)
            L40.remove(aa16)
        elif(str(variable16.get())=='mischap5(U 4)'):
            aa16=random.choice(L41)
            L41.remove(aa16)
        elif(str(variable16.get())=='mischap5(U 6)'):
            aa16=random.choice(L42)
            L42.remove(aa16)
        elif(str(variable16.get())=='mischap5(A 2)'):
            aa16=random.choice(L43)
            L43.remove(aa16)
        elif(str(variable16.get())=='mischap5(A 4)'):
            aa16=random.choice(L44)
            L44.remove(aa16)
        elif(str(variable16.get())=='mischap5(A 6)'):
            aa16=random.choice(L45)
            L45.remove(aa16)
    canvas.create_window((300,1220), anchor='nw', window=s)

        #Question 4 .b
    canvas.create_text((230,1260),anchor=NW, text="   b",font= (20))
    variable17 = StringVar(root)
    c18=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c18,textvariabl=variable17,state='readonly',wrap=True)
    def om18():
        global aa17
        if(str(variable17.get())=='mischap1(R 2)'):
            aa17=random.choice(L1)
            L1.remove(aa17)
        elif(str(variable17.get())=='mischap1(R 4)'):
            aa17=random.choice(L2)
            L2.remove(aa17)
        elif(str(variable17.get())=='mischap1(R 6)'):
            aa17=random.choice(L3)
            L3.remove(aa17)
        elif(str(variable17.get())=='mischap1(U 2)'):
            aa17=random.choice(L4)
            L4.remove(aa17)
        elif(str(variable17.get())=='mischap1(U 4)'):
            aa17=random.choice(L5)
            L5.remove(aa17)
        elif(str(variable17.get())=='mischap1(U 6)'):
            aa17=random.choice(L6)
            L6.remove(aa17)
        elif(str(variable17.get())=='mischap1(A 2)'):
            aa17=random.choice(L7)
            L7.remove(aa17)
        elif(str(variable17.get())=='mischap1(A 4)'):
            aa17=random.choice(L8)
            L8.remove(aa17)
        elif(str(variable17.get())=='mischap1(A 6)'):
            aa17=random.choice(L9)
            L9.remove(aa17)
        elif(str(variable17.get())=='mischap2(R 2)'):
            aa17=random.choice(L10)
            L10.remove(aa17)
        elif(str(variable17.get())=='mischap2(R 4)'):
            aa17=random.choice(L11)
            L11.remove(aa17)
        elif(str(variable17.get())=='mischap2(R 6)'):
            aa17=random.choice(L12)
            L12.remove(aa17)
        elif(str(variable17.get())=='mischap2(U 2)'):
            aa17=random.choice(L13)
            L13.remove(aa17)
        elif(str(variable17.get())=='mischap2(U 4)'):
            aa17=random.choice(L14)
            L14.remove(aa17)
        elif(str(variable17.get())=='mischap2(U 6)'):
            aa17=random.choice(L15)
            L15.remove(aa17)
        elif(str(variable17.get())=='mischap2(A 2)'):
            aa17=random.choice(L16)
            L16.remove(aa17)
        elif(str(variable17.get())=='mischap2(A 4)'):
            aa17=random.choice(L17)
            L17.remove(aa17)
        elif(str(variable17.get())=='mischap2(A 6)'):
            aa17=random.choice(L18)
            L18.remove(aa17)
        elif(str(variable17.get())=='mischap3(R 2)'):
            aa17=random.choice(L19)
            L19.remove(aa17)
        elif(str(variable17.get())=='mischap3(R 4)'):
            aa17=random.choice(L20)
            L20.remove(aa17)
        elif(str(variable17.get())=='mischap3(R 6)'):
            aa17=random.choice(L21)
            L21.remove(aa17)
        elif(str(variable17.get())=='mischap3(U 2)'):
            aa17=random.choice(L22)
            L22.remove(aa17)
        elif(str(variable17.get())=='mischap3(U 4)'):
            aa17=random.choice(L23)
            L23.remove(aa17)
        elif(str(variable17.get())=='mischap3(U 6)'):
            aa17=random.choice(L24)
            L24.remove(aa17)
        elif(str(variable17.get())=='mischap3(A 2)'):
            aa17=random.choice(L25)
            L25.remove(aa17)
        elif(str(variable17.get())=='mischap3(A 4)'):
            aa17=random.choice(L26)
            L26.remove(aa17)
        elif(str(variable17.get())=='mischap3(A 6)'):
            aa17=random.choice(L27)
            L27.remove(aa17)
        elif(str(variable17.get())=='mischap4(R 2)'):
            aa17=random.choice(L28)
            L28.remove(aa17)
        elif(str(variable17.get())=='mischap4(R 4)'):
            aa17=random.choice(L29)
            L29.remove(aa17)
        elif(str(variable17.get())=='mischap4(R 6)'):
            aa17=random.choice(L30)
            L30.remove(aa17)
        elif(str(variable17.get())=='mischap4(U 2)'):
            aa17=random.choice(L31)
            L31.remove(aa17)
        elif(str(variable17.get())=='mischap4(U 4)'):
            aa17=random.choice(L32)
            L32.remove(aa17)
        elif(str(variable17.get())=='mischap4(U 6)'):
            aa17=random.choice(L33)
            L33.remove(aa17)
        elif(str(variable17.get())=='mischap4(A 2)'):
            aa17=random.choice(L34)
            L34.remove(aa17)
        elif(str(variable17.get())=='mischap4(A 4)'):
            aa17=random.choice(L35)
            L35.remove(aa17)
        elif(str(variable17.get())=='mischap4(A 6)'):
            aa17=random.choice(L36)
            L36.remove(aa17)
        elif(str(variable17.get())=='mischap5(R 2)'):
            aa17=random.choice(L37)
            L37.remove(aa17)
        elif(str(variable17.get())=='mischap5(R 4)'):
            aa17=random.choice(L38)
            L38.remove(aa17)
        elif(str(variable17.get())=='mischap5(R 6)'):
            aa17=random.choice(L39)
            L39.remove(aa17)
        elif(str(variable17.get())=='mischap5(U 2)'):
            aa17=random.choice(L40)
            L40.remove(aa17)
        elif(str(variable17.get())=='mischap5(U 4)'):
            aa17=random.choice(L41)
            L41.remove(aa17)
        elif(str(variable17.get())=='mischap5(U 6)'):
            aa17=random.choice(L42)
            L42.remove(aa17)
        elif(str(variable17.get())=='mischap5(A 2)'):
            aa17=random.choice(L43)
            L43.remove(aa17)
        elif(str(variable17.get())=='mischap5(A 4)'):
            aa17=random.choice(L44)
            L44.remove(aa17)
        elif(str(variable17.get())=='mischap5(A 6)'):
            aa17=random.choice(L45)
            L45.remove(aa17)

    canvas.create_window((300,1260), anchor='nw', window=s)

        #Question 4 .c
    canvas.create_text((230,1300),anchor=NW, text="   c",font= (20))
    variable18 = StringVar(root)
    c19=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c19,textvariabl=variable18,state='readonly',wrap=True)
    def om19():
        global aa18
        if(str(variable18.get())=='mischap1(R 2)'):
            aa18=random.choice(L1)
            L1.remove(aa18)
        elif(str(variable18.get())=='mischap1(R 4)'):
            aa18=random.choice(L2)
            L2.remove(aa18)
        elif(str(variable18.get())=='mischap1(R 6)'):
            aa18=random.choice(L3)
            L3.remove(aa18)
        elif(str(variable18.get())=='mischap1(U 2)'):
            aa18=random.choice(L4)
            L4.remove(aa18)
        elif(str(variable18.get())=='mischap1(U 4)'):
            aa18=random.choice(L5)
            L5.remove(aa18)
        elif(str(variable18.get())=='mischap1(U 6)'):
            aa18=random.choice(L6)
            L6.remove(aa18)
        elif(str(variable18.get())=='mischap1(A 2)'):
            aa18=random.choice(L7)
            L7.remove(aa18)
        elif(str(variable18.get())=='mischap1(A 4)'):
            aa18=random.choice(L8)
            L8.remove(aa18)
        elif(str(variable18.get())=='mischap1(A 6)'):
            aa18=random.choice(L9)
            L9.remove(aa18)
        elif(str(variable18.get())=='mischap2(R 2)'):
            aa18=random.choice(L10)
            L10.remove(aa18)
        elif(str(variable18.get())=='mischap2(R 4)'):
            aa18=random.choice(L11)
            L11.remove(aa18)
        elif(str(variable18.get())=='mischap2(R 6)'):
            aa18=random.choice(L12)
            L12.remove(aa18)
        elif(str(variable18.get())=='mischap2(U 2)'):
            aa18=random.choice(L13)
            L13.remove(aa18)
        elif(str(variable18.get())=='mischap2(U 4)'):
            aa18=random.choice(L14)
            L14.remove(aa18)
        elif(str(variable18.get())=='mischap2(U 6)'):
            aa18=random.choice(L15)
            L15.remove(aa18)
        elif(str(variable18.get())=='mischap2(A 2)'):
            aa18=random.choice(L16)
            L16.remove(aa18)
        elif(str(variable18.get())=='mischap2(A 4)'):
            aa18=random.choice(L17)
            L17.remove(aa18)
        elif(str(variable18.get())=='mischap2(A 6)'):
            aa18=random.choice(L18)
            L18.remove(aa18)
        elif(str(variable18.get())=='mischap3(R 2)'):
            aa18=random.choice(L19)
            L19.remove(aa18)
        elif(str(variable18.get())=='mischap3(R 4)'):
            aa18=random.choice(L20)
            L20.remove(aa18)
        elif(str(variable18.get())=='mischap3(R 6)'):
            aa18=random.choice(L21)
            L21.remove(aa18)
        elif(str(variable18.get())=='mischap3(U 2)'):
            aa18=random.choice(L22)
            L22.remove(aa18)
        elif(str(variable18.get())=='mischap3(U 4)'):
            aa18=random.choice(L23)
            L23.remove(aa18)
        elif(str(variable18.get())=='mischap3(U 6)'):
            aa18=random.choice(L24)
            L24.remove(aa18)
        elif(str(variable18.get())=='mischap3(A 2)'):
            aa18=random.choice(L25)
            L25.remove(aa18)
        elif(str(variable18.get())=='mischap3(A 4)'):
            aa18=random.choice(L26)
            L26.remove(aa18)
        elif(str(variable18.get())=='mischap3(A 6)'):
            aa18=random.choice(L27)
            L27.remove(aa18)
        elif(str(variable18.get())=='mischap4(R 2)'):
            aa18=random.choice(L28)
            L28.remove(aa18)
        elif(str(variable18.get())=='mischap4(R 4)'):
            aa18=random.choice(L29)
            L29.remove(aa18)
        elif(str(variable18.get())=='mischap4(R 6)'):
            aa18=random.choice(L30)
            L30.remove(aa18)
        elif(str(variable18.get())=='mischap4(U 2)'):
            aa18=random.choice(L31)
            L31.remove(aa18)
        elif(str(variable18.get())=='mischap4(U 4)'):
            aa18=random.choice(L32)
            L32.remove(aa18)
        elif(str(variable18.get())=='mischap4(U 6)'):
            aa18=random.choice(L33)
            L33.remove(aa18)
        elif(str(variable18.get())=='mischap4(A 2)'):
            aa18=random.choice(L34)
            L34.remove(aa18)
        elif(str(variable18.get())=='mischap4(A 4)'):
            aa18=random.choice(L35)
            L35.remove(aa18)
        elif(str(variable18.get())=='mischap4(A 6)'):
            aa18=random.choice(L36)
            L36.remove(aa18)
        elif(str(variable18.get())=='mischap5(R 2)'):
            aa18=random.choice(L37)
            L37.remove(aa18)
        elif(str(variable18.get())=='mischap5(R 4)'):
            aa18=random.choice(L38)
            L38.remove(aa18)
        elif(str(variable18.get())=='mischap5(R 6)'):
            aa18=random.choice(L39)
            L39.remove(aa18)
        elif(str(variable18.get())=='mischap5(U 2)'):
            aa18=random.choice(L40)
            L40.remove(aa18)
        elif(str(variable18.get())=='mischap5(U 4)'):
            aa18=random.choice(L41)
            L41.remove(aa18)
        elif(str(variable18.get())=='mischap5(U 6)'):
            aa18=random.choice(L42)
            L42.remove(aa18)
        elif(str(variable18.get())=='mischap5(A 2)'):
            aa18=random.choice(L43)
            L43.remove(aa18)
        elif(str(variable18.get())=='mischap5(A 4)'):
            aa18=random.choice(L44)
            L44.remove(aa18)
        elif(str(variable18.get())=='mischap5(A 6)'):
            aa18=random.choice(L45)
            L45.remove(aa18)
    canvas.create_window((300,1300), anchor='nw', window=s)

        #Question 4 .d
    canvas.create_text((230,1340),anchor=NW, text="   d",font= (20))
    variable19 = StringVar(root)
    c20=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c20,textvariabl=variable19,state='readonly',wrap=True)
    def om20():
        global aa19
        if(str(variable19.get())=='mischap1(R 2)'):
            aa19=random.choice(L1)
            L1.remove(aa19)
        elif(str(variable19.get())=='mischap1(R 4)'):
            aa19=random.choice(L2)
            L2.remove(aa19)
        elif(str(variable19.get())=='mischap1(R 6)'):
            aa19=random.choice(L3)
            L3.remove(aa19)
        elif(str(variable19.get())=='mischap1(U 2)'):
            aa19=random.choice(L4)
            L4.remove(aa19)
        elif(str(variable19.get())=='mischap1(U 4)'):
            aa19=random.choice(L5)
            L5.remove(aa19)
        elif(str(variable19.get())=='mischap1(U 6)'):
            aa19=random.choice(L6)
            L6.remove(aa19)
        elif(str(variable19.get())=='mischap1(A 2)'):
            aa19=random.choice(L7)
            L7.remove(aa19)
        elif(str(variable19.get())=='mischap1(A 4)'):
            aa19=random.choice(L8)
            L8.remove(aa19)
        elif(str(variable19.get())=='mischap1(A 6)'):
            aa19=random.choice(L9)
            L9.remove(aa19)
        elif(str(variable19.get())=='mischap2(R 2)'):
            aa19=random.choice(L10)
            L10.remove(aa19)
        elif(str(variable19.get())=='mischap2(R 4)'):
            aa19=random.choice(L11)
            L11.remove(aa19)
        elif(str(variable19.get())=='mischap2(R 6)'):
            aa19=random.choice(L12)
            L12.remove(aa19)
        elif(str(variable19.get())=='mischap2(U 2)'):
            aa19=random.choice(L13)
            L13.remove(aa19)
        elif(str(variable19.get())=='mischap2(U 4)'):
            aa19=random.choice(L14)
            L14.remove(aa19)
        elif(str(variable19.get())=='mischap2(U 6)'):
            aa19=random.choice(L15)
            L15.remove(aa19)
        elif(str(variable19.get())=='mischap2(A 2)'):
            aa19=random.choice(L16)
            L16.remove(aa19)
        elif(str(variable19.get())=='mischap2(A 4)'):
            aa19=random.choice(L17)
            L17.remove(aa19)
        elif(str(variable19.get())=='mischap2(A 6)'):
            aa19=random.choice(L18)
            L18.remove(aa19)
        elif(str(variable19.get())=='mischap3(R 2)'):
            aa19=random.choice(L19)
            L19.remove(aa19)
        elif(str(variable19.get())=='mischap3(R 4)'):
            aa19=random.choice(L20)
            L20.remove(aa19)
        elif(str(variable19.get())=='mischap3(R 6)'):
            aa19=random.choice(L21)
            L21.remove(aa19)
        elif(str(variable19.get())=='mischap3(U 2)'):
            aa19=random.choice(L22)
            L22.remove(aa19)
        elif(str(variable19.get())=='mischap3(U 4)'):
            aa19=random.choice(L23)
            L23.remove(aa19)
        elif(str(variable19.get())=='mischap3(U 6)'):
            aa19=random.choice(L24)
            L24.remove(aa19)
        elif(str(variable19.get())=='mischap3(A 2)'):
            aa19=random.choice(L25)
            L25.remove(aa19)
        elif(str(variable19.get())=='mischap3(A 4)'):
            aa19=random.choice(L26)
            L26.remove(aa19)
        elif(str(variable19.get())=='mischap3(A 6)'):
            aa19=random.choice(L27)
            L27.remove(aa19)
        elif(str(variable19.get())=='mischap4(R 2)'):
            aa19=random.choice(L28)
            L28.remove(aa19)
        elif(str(variable19.get())=='mischap4(R 4)'):
            aa19=random.choice(L29)
            L29.remove(aa19)
        elif(str(variable19.get())=='mischap4(R 6)'):
            aa19=random.choice(L30)
            L30.remove(aa19)
        elif(str(variable19.get())=='mischap4(U 2)'):
            aa19=random.choice(L31)
            L31.remove(aa19)
        elif(str(variable19.get())=='mischap4(U 4)'):
            aa19=random.choice(L32)
            L32.remove(aa19)
        elif(str(variable19.get())=='mischap4(U 6)'):
            aa19=random.choice(L33)
            L33.remove(aa19)
        elif(str(variable19.get())=='mischap4(A 2)'):
            aa19=random.choice(L34)
            L34.remove(aa19)
        elif(str(variable19.get())=='mischap4(A 4)'):
            aa19=random.choice(L35)
            L35.remove(aa19)
        elif(str(variable19.get())=='mischap4(A 6)'):
            aa19=random.choice(L36)
            L36.remove(aa19)
        elif(str(variable19.get())=='mischap5(R 2)'):
            aa19=random.choice(L37)
            L37.remove(aa19)
        elif(str(variable19.get())=='mischap5(R 4)'):
            aa19=random.choice(L38)
            L38.remove(aa19)
        elif(str(variable19.get())=='mischap5(R 6)'):
            aa19=random.choice(L39)
            L39.remove(aa19)
        elif(str(variable19.get())=='mischap5(U 2)'):
            aa19=random.choice(L40)
            L40.remove(aa19)
        elif(str(variable19.get())=='mischap5(U 4)'):
            aa19=random.choice(L41)
            L41.remove(aa19)
        elif(str(variable19.get())=='mischap5(U 6)'):
            aa19=random.choice(L42)
            L42.remove(aa19)
        elif(str(variable19.get())=='mischap5(A 2)'):
            aa19=random.choice(L43)
            L43.remove(aa19)
        elif(str(variable19.get())=='mischap5(A 4)'):
            aa19=random.choice(L44)
            L44.remove(aa19)
        elif(str(variable19.get())=='mischap5(A 6)'):
            aa19=random.choice(L45)
            L45.remove(aa19)

    canvas.create_window((300,1340), anchor='nw', window=s)

        #Question 4 .e
    canvas.create_text((230,1380),anchor=NW, text="   e",font= (20))
    variable20 = StringVar(root)
    c21=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c21,textvariabl=variable20,state='readonly',wrap=True)
    def om21():
        global aa20
        if(str(variable20.get())=='mischap1(R 2)'):
            aa20=random.choice(L1)
            L1.remove(aa20)
        elif(str(variable20.get())=='mischap1(R 4)'):
            aa20=random.choice(L2)
            L2.remove(aa20)
        elif(str(variable20.get())=='mischap1(R 6)'):
            aa20=random.choice(L3)
            L3.remove(aa20)
        elif(str(variable20.get())=='mischap1(U 2)'):
            aa20=random.choice(L4)
            L4.remove(aa20)
        elif(str(variable20.get())=='mischap1(U 4)'):
            aa20=random.choice(L5)
            L5.remove(aa20)
        elif(str(variable20.get())=='mischap1(U 6)'):
            aa20=random.choice(L6)
            L6.remove(aa20)
        elif(str(variable20.get())=='mischap1(A 2)'):
            aa20=random.choice(L7)
            L7.remove(aa20)
        elif(str(variable20.get())=='mischap1(A 4)'):
            aa20=random.choice(L8)
            L8.remove(aa20)
        elif(str(variable20.get())=='mischap1(A 6)'):
            aa20=random.choice(L9)
            L9.remove(aa20)
        elif(str(variable20.get())=='mischap2(R 2)'):
            aa20=random.choice(L10)
            L10.remove(aa20)
        elif(str(variable20.get())=='mischap2(R 4)'):
            aa20=random.choice(L11)
            L11.remove(aa20)
        elif(str(variable20.get())=='mischap2(R 6)'):
            aa20=random.choice(L12)
            L12.remove(aa20)
        elif(str(variable20.get())=='mischap2(U 2)'):
            aa20=random.choice(L13)
            L13.remove(aa20)
        elif(str(variable20.get())=='mischap2(U 4)'):
            aa20=random.choice(L14)
            L14.remove(aa20)
        elif(str(variable20.get())=='mischap2(U 6)'):
            aa20=random.choice(L15)
            L15.remove(aa20)
        elif(str(variable20.get())=='mischap2(A 2)'):
            aa20=random.choice(L16)
            L16.remove(aa20)
        elif(str(variable20.get())=='mischap2(A 4)'):
            aa20=random.choice(L17)
            L17.remove(aa20)
        elif(str(variable20.get())=='mischap2(A 6)'):
            aa20=random.choice(L18)
            L18.remove(aa20)
        elif(str(variable20.get())=='mischap3(R 2)'):
            aa20=random.choice(L19)
            L19.remove(aa20)
        elif(str(variable20.get())=='mischap3(R 4)'):
            aa20=random.choice(L20)
            L20.remove(aa20)
        elif(str(variable20.get())=='mischap3(R 6)'):
            aa20=random.choice(L21)
            L21.remove(aa20)
        elif(str(variable20.get())=='mischap3(U 2)'):
            aa20=random.choice(L22)
            L22.remove(aa20)
        elif(str(variable20.get())=='mischap3(U 4)'):
            aa20=random.choice(L23)
            L23.remove(aa20)
        elif(str(variable20.get())=='mischap3(U 6)'):
            aa20=random.choice(L24)
            L24.remove(aa20)
        elif(str(variable20.get())=='mischap3(A 2)'):
            aa20=random.choice(L25)
            L25.remove(aa20)
        elif(str(variable20.get())=='mischap3(A 4)'):
            aa20=random.choice(L26)
            L26.remove(aa20)
        elif(str(variable20.get())=='mischap3(A 6)'):
            aa20=random.choice(L27)
            L27.remove(aa20)
        elif(str(variable20.get())=='mischap4(R 2)'):
            aa20=random.choice(L28)
            L28.remove(aa20)
        elif(str(variable20.get())=='mischap4(R 4)'):
            aa20=random.choice(L29)
            L29.remove(aa20)
        elif(str(variable20.get())=='mischap4(R 6)'):
            aa20=random.choice(L30)
            L30.remove(aa20)
        elif(str(variable20.get())=='mischap4(U 2)'):
            aa20=random.choice(L31)
            L31.remove(aa20)
        elif(str(variable20.get())=='mischap4(U 4)'):
            aa20=random.choice(L32)
            L32.remove(aa20)
        elif(str(variable20.get())=='mischap4(U 6)'):
            aa20=random.choice(L33)
            L33.remove(aa20)
        elif(str(variable20.get())=='mischap4(A 2)'):
            aa20=random.choice(L34)
            L34.remove(aa20)
        elif(str(variable20.get())=='mischap4(A 4)'):
            aa20=random.choice(L35)
            L35.remove(aa20)
        elif(str(variable20.get())=='mischap4(A 6)'):
            aa20=random.choice(L36)
            L36.remove(aa20)
        elif(str(variable20.get())=='mischap5(R 2)'):
            aa20=random.choice(L37)
            L37.remove(aa20)
        elif(str(variable20.get())=='mischap5(R 4)'):
            aa20=random.choice(L38)
            L38.remove(aa20)
        elif(str(variable20.get())=='mischap5(R 6)'):
            aa20=random.choice(L39)
            L39.remove(aa20)
        elif(str(variable20.get())=='mischap5(U 2)'):
            aa20=random.choice(L40)
            L40.remove(aa20)
        elif(str(variable20.get())=='mischap5(U 4)'):
            aa20=random.choice(L41)
            L41.remove(aa20)
        elif(str(variable20.get())=='mischap5(U 6)'):
            aa20=random.choice(L42)
            L42.remove(aa20)
        elif(str(variable20.get())=='mischap5(A 2)'):
            aa20=random.choice(L43)
            L43.remove(aa20)
        elif(str(variable20.get())=='mischap5(A 4)'):
            aa20=random.choice(L44)
            L44.remove(aa20)
        elif(str(variable20.get())=='mischap5(A 6)'):
            aa20=random.choice(L45)
            L45.remove(aa20)
        elif(str(variable.get())=='pychap6(R 2)'):
            aa20=random.choice(L46)
            L46.remove(aa20)
        elif(str(variable.get())=='pychap6(R 4)'):
            aa20=random.choice(L47)
            L47.remove(aa20)
        elif(str(variable.get())=='pychap6(R 6)'):
            aa20=random.choice(L48)
            L48.remove(aa20)
        elif(str(variable.get())=='pychap6(U 2)'):
            aa20=random.choice(L49)
            L49.remove(aa20)
        elif(str(variable.get())=='pychap6(U 4)'):
            aa20=random.choice(L50)
            L50.remove(aa20)
        elif(str(variable.get())=='pychap6(U 6)'):
            aa20=random.choice(L51)
            L51.remove(aa20)
        elif(str(variable.get())=='pychap6(A 2)'):
            aa20=random.choice(L52)
            L52.remove(aa20)
        elif(str(variable.get())=='pychap6(A 4)'):
            aa20=random.choice(L53)
            L53.remove(aa20)
        elif(str(variable.get())=='pychap6(A 6)'):
            aa20=random.choice(L54)
            L54.remove(aa20)
    canvas.create_window((300,1380), anchor='nw', window=s)

        #Question 4 .f
    canvas.create_text((230,1420),anchor=NW, text="   f",font= (20))
    variable21 = StringVar(root)
    c22=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c22,textvariabl=variable21,state='readonly',wrap=True)
    def om22():
        global aa21
        if(str(variable21.get())=='mischap1(R 2)'):
            aa21=random.choice(L1)
            L1.remove(aa21)
        elif(str(variable21.get())=='mischap1(R 4)'):
            aa21=random.choice(L2)
            L2.remove(aa21)
        elif(str(variable21.get())=='mischap1(R 6)'):
            aa21=random.choice(L3)
            L3.remove(aa21)
        elif(str(variable21.get())=='mischap1(U 2)'):
            aa21=random.choice(L4)
            L4.remove(aa21)
        elif(str(variable21.get())=='mischap1(U 4)'):
            aa21=random.choice(L5)
            L5.remove(aa21)
        elif(str(variable21.get())=='mischap1(U 6)'):
            aa21=random.choice(L6)
            L6.remove(aa21)
        elif(str(variable21.get())=='mischap1(A 2)'):
            aa21=random.choice(L7)
            L7.remove(aa21)
        elif(str(variable21.get())=='mischap1(A 4)'):
            aa21=random.choice(L8)
            L8.remove(aa21)
        elif(str(variable21.get())=='mischap1(A 6)'):
            aa21=random.choice(L9)
            L9.remove(aa21)
        elif(str(variable21.get())=='mischap2(R 2)'):
            aa21=random.choice(L10)
            L10.remove(aa21)
        elif(str(variable21.get())=='mischap2(R 4)'):
            aa21=random.choice(L11)
            L11.remove(aa21)
        elif(str(variable21.get())=='mischap2(R 6)'):
            aa21=random.choice(L12)
            L12.remove(aa21)
        elif(str(variable21.get())=='mischap2(U 2)'):
            aa21=random.choice(L13)
            L13.remove(aa21)
        elif(str(variable21.get())=='mischap2(U 4)'):
            aa21=random.choice(L14)
            L14.remove(aa21)
        elif(str(variable21.get())=='mischap2(U 6)'):
            aa21=random.choice(L15)
            L15.remove(aa21)
        elif(str(variable21.get())=='mischap2(A 2)'):
            aa21=random.choice(L16)
            L16.remove(aa21)
        elif(str(variable21.get())=='mischap2(A 4)'):
            aa21=random.choice(L17)
            L17.remove(aa21)
        elif(str(variable21.get())=='mischap2(A 6)'):
            aa21=random.choice(L18)
            L18.remove(aa21)
        elif(str(variable21.get())=='mischap3(R 2)'):
            aa21=random.choice(L19)
            L19.remove(aa21)
        elif(str(variable21.get())=='mischap3(R 4)'):
            aa21=random.choice(L20)
            L20.remove(aa21)
        elif(str(variable21.get())=='mischap3(R 6)'):
            aa21=random.choice(L21)
            L21.remove(aa21)
        elif(str(variable21.get())=='mischap3(U 2)'):
            aa21=random.choice(L22)
            L22.remove(aa21)
        elif(str(variable21.get())=='mischap3(U 4)'):
            aa21=random.choice(L23)
            L23.remove(aa21)
        elif(str(variable21.get())=='mischap3(U 6)'):
            aa21=random.choice(L24)
            L24.remove(aa21)
        elif(str(variable21.get())=='mischap3(A 2)'):
            aa21=random.choice(L25)
            L25.remove(aa21)
        elif(str(variable21.get())=='mischap3(A 4)'):
            aa21=random.choice(L26)
            L26.remove(aa21)
        elif(str(variable21.get())=='mischap3(A 6)'):
            aa21=random.choice(L27)
            L27.remove(aa21)
        elif(str(variable21.get())=='mischap4(R 2)'):
            aa21=random.choice(L28)
            L28.remove(aa21)
        elif(str(variable21.get())=='mischap4(R 4)'):
            aa21=random.choice(L29)
            L29.remove(aa21)
        elif(str(variable21.get())=='mischap4(R 6)'):
            aa21=random.choice(L30)
            L30.remove(aa21)
        elif(str(variable21.get())=='mischap4(U 2)'):
            aa21=random.choice(L31)
            L31.remove(aa21)
        elif(str(variable21.get())=='mischap4(U 4)'):
            aa21=random.choice(L32)
            L32.remove(aa21)
        elif(str(variable21.get())=='mischap4(U 6)'):
            aa21=random.choice(L33)
            L33.remove(aa21)
        elif(str(variable21.get())=='mischap4(A 2)'):
            aa21=random.choice(L34)
            L34.remove(aa21)
        elif(str(variable21.get())=='mischap4(A 4)'):
            aa21=random.choice(L35)
            L35.remove(aa21)
        elif(str(variable21.get())=='mischap4(A 6)'):
            aa21=random.choice(L36)
            L36.remove(aa21)
        elif(str(variable21.get())=='mischap5(R 2)'):
            aa21=random.choice(L37)
            L37.remove(aa21)
        elif(str(variable21.get())=='mischap5(R 4)'):
            aa21=random.choice(L38)
            L38.remove(aa21)
        elif(str(variable21.get())=='mischap5(R 6)'):
            aa21=random.choice(L39)
            L39.remove(aa21)
        elif(str(variable21.get())=='mischap5(U 2)'):
            aa21=random.choice(L40)
            L40.remove(aa21)
        elif(str(variable21.get())=='mischap5(U 4)'):
            aa21=random.choice(L41)
            L41.remove(aa21)
        elif(str(variable21.get())=='mischap5(U 6)'):
            aa21=random.choice(L42)
            L42.remove(aa21)
        elif(str(variable21.get())=='mischap5(A 2)'):
            aa21=random.choice(L43)
            L43.remove(aa21)
        elif(str(variable21.get())=='mischap5(A 4)'):
            aa21=random.choice(L44)
            L44.remove(aa21)
        elif(str(variable21.get())=='mischap5(A 6)'):
            aa21=random.choice(L45)
            L45.remove(aa21)
    canvas.create_window((300,1420), anchor='nw', window=s)

        #Question 4 .g
    canvas.create_text((230,1460),anchor=NW, text="   g",font= (20))
    variable22 = StringVar(root)
    c23=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c23,textvariabl=variable22,state='readonly',wrap=True)
    def om23():
        global aa22
        if(str(variable22.get())=='mischap1(R 2)'):
            aa22=random.choice(L1)
            L1.remove(aa22)
        elif(str(variable22.get())=='mischap1(R 4)'):
            aa22=random.choice(L2)
            L2.remove(aa22)
        elif(str(variable22.get())=='mischap1(R 6)'):
            aa22=random.choice(L3)
            L3.remove(aa22)
        elif(str(variable22.get())=='mischap1(U 2)'):
            aa22=random.choice(L4)
            L4.remove(aa22)
        elif(str(variable22.get())=='mischap1(U 4)'):
            aa22=random.choice(L5)
            L5.remove(aa22)
        elif(str(variable22.get())=='mischap1(U 6)'):
            aa22=random.choice(L6)
            L6.remove(aa22)
        elif(str(variable22.get())=='mischap1(A 2)'):
            aa22=random.choice(L7)
            L7.remove(aa22)
        elif(str(variable22.get())=='mischap1(A 4)'):
            aa22=random.choice(L8)
            L8.remove(aa22)
        elif(str(variable22.get())=='mischap1(A 6)'):
            aa22=random.choice(L9)
            L9.remove(aa22)
        elif(str(variable22.get())=='mischap2(R 2)'):
            aa22=random.choice(L10)
            L10.remove(aa22)
        elif(str(variable22.get())=='mischap2(R 4)'):
            aa22=random.choice(L11)
            L11.remove(aa22)
        elif(str(variable22.get())=='mischap2(R 6)'):
            aa22=random.choice(L12)
            L12.remove(aa22)
        elif(str(variable22.get())=='mischap2(U 2)'):
            aa22=random.choice(L13)
            L13.remove(aa22)
        elif(str(variable22.get())=='mischap2(U 4)'):
            aa22=random.choice(L14)
            L14.remove(aa22)
        elif(str(variable22.get())=='mischap2(U 6)'):
            aa22=random.choice(L15)
            L15.remove(aa22)
        elif(str(variable22.get())=='mischap2(A 2)'):
            aa22=random.choice(L16)
            L16.remove(aa22)
        elif(str(variable22.get())=='mischap2(A 4)'):
            aa22=random.choice(L17)
            L17.remove(aa22)
        elif(str(variable22.get())=='mischap2(A 6)'):
            aa22=random.choice(L18)
            L18.remove(aa22)
        elif(str(variable22.get())=='mischap3(R 2)'):
            aa22=random.choice(L19)
            L19.remove(aa22)
        elif(str(variable22.get())=='mischap3(R 4)'):
            aa22=random.choice(L20)
            L20.remove(aa22)
        elif(str(variable22.get())=='mischap3(R 6)'):
            aa22=random.choice(L21)
            L21.remove(aa22)
        elif(str(variable22.get())=='mischap3(U 2)'):
            aa22=random.choice(L22)
            L22.remove(aa22)
        elif(str(variable22.get())=='mischap3(U 4)'):
            aa22=random.choice(L23)
            L23.remove(aa22)
        elif(str(variable22.get())=='mischap3(U 6)'):
            aa22=random.choice(L24)
            L24.remove(aa22)
        elif(str(variable22.get())=='mischap3(A 2)'):
            aa22=random.choice(L25)
            L25.remove(aa22)
        elif(str(variable22.get())=='mischap3(A 4)'):
            aa22=random.choice(L26)
            L26.remove(aa22)
        elif(str(variable22.get())=='mischap3(A 6)'):
            aa22=random.choice(L27)
            L27.remove(aa22)
        elif(str(variable22.get())=='mischap4(R 2)'):
            aa22=random.choice(L28)
            L28.remove(aa22)
        elif(str(variable22.get())=='mischap4(R 4)'):
            aa22=random.choice(L29)
            L29.remove(aa22)
        elif(str(variable22.get())=='mischap4(R 6)'):
            aa22=random.choice(L30)
            L30.remove(aa22)
        elif(str(variable22.get())=='mischap4(U 2)'):
            aa22=random.choice(L31)
            L31.remove(aa22)
        elif(str(variable22.get())=='mischap4(U 4)'):
            aa22=random.choice(L32)
            L32.remove(aa22)
        elif(str(variable22.get())=='mischap4(U 6)'):
            aa22=random.choice(L33)
            L33.remove(aa22)
        elif(str(variable22.get())=='mischap4(A 2)'):
            aa22=random.choice(L34)
            L34.remove(aa22)
        elif(str(variable22.get())=='mischap4(A 4)'):
            aa22=random.choice(L35)
            L35.remove(aa22)
        elif(str(variable22.get())=='mischap4(A 6)'):
            aa22=random.choice(L36)
            L36.remove(aa22)
        elif(str(variable22.get())=='mischap5(R 2)'):
            aa22=random.choice(L37)
            L37.remove(aa22)
        elif(str(variable22.get())=='mischap5(R 4)'):
            aa22=random.choice(L38)
            L38.remove(aa22)
        elif(str(variable22.get())=='mischap5(R 6)'):
            aa22=random.choice(L39)
            L39.remove(aa22)
        elif(str(variable22.get())=='mischap5(U 2)'):
            aa22=random.choice(L40)
            L40.remove(aa22)
        elif(str(variable22.get())=='mischap5(U 4)'):
            aa22=random.choice(L41)
            L41.remove(aa22)
        elif(str(variable22.get())=='mischap5(U 6)'):
            aa22=random.choice(L42)
            L42.remove(aa22)
        elif(str(variable22.get())=='mischap5(A 2)'):
            aa22=random.choice(L43)
            L43.remove(aa22)
        elif(str(variable22.get())=='mischap5(A 4)'):
            aa22=random.choice(L44)
            L44.remove(aa22)
        elif(str(variable22.get())=='mischap5(A 6)'):
            aa22=random.choice(L45)
            L45.remove(aa22)
    canvas.create_window((300,1460), anchor='nw', window=s)

#-----------------------------------------------------------------------------------------------------------------------------
#                                                         Question5 Start
#-------------------------------------------------------------------------------------------------------------------------------------
    canvas.create_text((230,1500),anchor=NW, text="Q.5              Attempt any THREE                                                                          12Marks",font= ("bold",15))

      #Question 5 .a
    canvas.create_text((230,1540),anchor=NW, text="   a",font= (20))
    variable23 = StringVar(root)
    c24=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c24,textvariabl=variable23,state='readonly',wrap=True)
    def om24():
        global aa23
        if(str(variable23.get())=='mischap1(R 2)'):
            aa23=random.choice(L1)
            L1.remove(aa23)
        elif(str(variable23.get())=='mischap1(R 4)'):
            aa23=random.choice(L2)
            L2.remove(aa23)
        elif(str(variable23.get())=='mischap1(R 6)'):
            aa23=random.choice(L3)
            L3.remove(aa23)
        elif(str(variable23.get())=='mischap1(U 2)'):
            aa23=random.choice(L4)
            L4.remove(aa23)
        elif(str(variable23.get())=='mischap1(U 4)'):
            aa23=random.choice(L5)
            L5.remove(aa23)
        elif(str(variable23.get())=='mischap1(U 6)'):
            aa23=random.choice(L6)
            L6.remove(aa23)
        elif(str(variable23.get())=='mischap1(A 2)'):
            aa23=random.choice(L7)
            L7.remove(aa23)
        elif(str(variable23.get())=='mischap1(A 4)'):
            aa23=random.choice(L8)
            L8.remove(aa23)
        elif(str(variable23.get())=='mischap1(A 6)'):
            aa23=random.choice(L9)
            L9.remove(aa23)
        elif(str(variable23.get())=='mischap2(R 2)'):
            aa23=random.choice(L10)
            L10.remove(aa23)
        elif(str(variable23.get())=='mischap2(R 4)'):
            aa23=random.choice(L11)
            L11.remove(aa23)
        elif(str(variable23.get())=='mischap2(R 6)'):
            aa23=random.choice(L12)
            L12.remove(aa23)
        elif(str(variable23.get())=='mischap2(U 2)'):
            aa23=random.choice(L13)
            L13.remove(aa23)
        elif(str(variable23.get())=='mischap2(U 4)'):
            aa23=random.choice(L14)
            L14.remove(aa23)
        elif(str(variable23.get())=='mischap2(U 6)'):
            aa23=random.choice(L15)
            L15.remove(aa23)
        elif(str(variable23.get())=='mischap2(A 2)'):
            aa23=random.choice(L16)
            L16.remove(aa23)
        elif(str(variable23.get())=='mischap2(A 4)'):
            aa23=random.choice(L17)
            L17.remove(aa23)
        elif(str(variable23.get())=='mischap2(A 6)'):
            aa23=random.choice(L18)
            L18.remove(aa23)
        elif(str(variable23.get())=='mischap3(R 2)'):
            aa23=random.choice(L19)
            L19.remove(aa23)
        elif(str(variable23.get())=='mischap3(R 4)'):
            aa23=random.choice(L20)
            L20.remove(aa23)
        elif(str(variable23.get())=='mischap3(R 6)'):
            aa23=random.choice(L21)
            L21.remove(aa23)
        elif(str(variable23.get())=='mischap3(U 2)'):
            aa23=random.choice(L22)
            L22.remove(aa23)
        elif(str(variable23.get())=='mischap3(U 4)'):
            aa23=random.choice(L23)
            L23.remove(aa23)
        elif(str(variable23.get())=='mischap3(U 6)'):
            aa23=random.choice(L24)
            L24.remove(aa23)
        elif(str(variable23.get())=='mischap3(A 2)'):
            aa23=random.choice(L25)
            L25.remove(aa23)
        elif(str(variable23.get())=='mischap3(A 4)'):
            aa23=random.choice(L26)
            L26.remove(aa23)
        elif(str(variable23.get())=='mischap3(A 6)'):
            aa23=random.choice(L27)
            L27.remove(aa23)
        elif(str(variable23.get())=='mischap4(R 2)'):
            aa23=random.choice(L28)
            L28.remove(aa23)
        elif(str(variable23.get())=='mischap4(R 4)'):
            aa23=random.choice(L29)
            L29.remove(aa23)
        elif(str(variable23.get())=='mischap4(R 6)'):
            aa23=random.choice(L30)
            L30.remove(aa23)
        elif(str(variable23.get())=='mischap4(U 2)'):
            aa23=random.choice(L31)
            L31.remove(aa23)
        elif(str(variable23.get())=='mischap4(U 4)'):
            aa23=random.choice(L32)
            L32.remove(aa23)
        elif(str(variable23.get())=='mischap4(U 6)'):
            aa23=random.choice(L33)
            L33.remove(aa23)
        elif(str(variable23.get())=='mischap4(A 2)'):
            aa23=random.choice(L34)
            L34.remove(aa23)
        elif(str(variable23.get())=='mischap4(A 4)'):
            aa23=random.choice(L35)
            L35.remove(aa23)
        elif(str(variable23.get())=='mischap4(A 6)'):
            aa23=random.choice(L36)
            L36.remove(aa23)
        elif(str(variable23.get())=='mischap5(R 2)'):
            aa23=random.choice(L37)
            L37.remove(aa23)
        elif(str(variable23.get())=='mischap5(R 4)'):
            aa23=random.choice(L38)
            L38.remove(aa23)
        elif(str(variable23.get())=='mischap5(R 6)'):
            aa23=random.choice(L39)
            L39.remove(aa23)
        elif(str(variable23.get())=='mischap5(U 2)'):
            aa23=random.choice(L40)
            L40.remove(aa23)
        elif(str(variable23.get())=='mischap5(U 4)'):
            aa23=random.choice(L41)
            L41.remove(aa23)
        elif(str(variable23.get())=='mischap5(U 6)'):
            aa23=random.choice(L42)
            L42.remove(aa23)
        elif(str(variable23.get())=='mischap5(A 2)'):
            aa23=random.choice(L43)
            L43.remove(aa23)
        elif(str(variable23.get())=='mischap5(A 4)'):
            aa23=random.choice(L44)
            L44.remove(aa23)
        elif(str(variable23.get())=='mischap5(A 6)'):
            aa23=random.choice(L45)
            L45.remove(aa23)
    canvas.create_window((300,1540), anchor='nw', window=s)

      #Question 5 .b
    canvas.create_text((230,1580),anchor=NW, text="   b",font= (20))
    variable24 = StringVar(root)
    c25=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c25,textvariabl=variable24,state='readonly',wrap=True)
    def om25():
        global aa24
        if(str(variable24.get())=='mischap1(R 2)'):
            aa24=random.choice(L1)
            L1.remove(aa24)
        elif(str(variable24.get())=='mischap1(R 4)'):
            aa24=random.choice(L2)
            L2.remove(aa24)
        elif(str(variable24.get())=='mischap1(R 6)'):
            aa24=random.choice(L3)
            L3.remove(aa24)
        elif(str(variable24.get())=='mischap1(U 2)'):
            aa24=random.choice(L4)
            L4.remove(aa24)
        elif(str(variable24.get())=='mischap1(U 4)'):
            aa24=random.choice(L5)
            L5.remove(aa24)
        elif(str(variable24.get())=='mischap1(U 6)'):
            aa24=random.choice(L6)
            L6.remove(aa24)
        elif(str(variable24.get())=='mischap1(A 2)'):
            aa24=random.choice(L7)
            L7.remove(aa24)
        elif(str(variable24.get())=='mischap1(A 4)'):
            aa24=random.choice(L8)
            L8.remove(aa24)
        elif(str(variable24.get())=='mischap1(A 6)'):
            aa24=random.choice(L9)
            L9.remove(aa24)
        elif(str(variable24.get())=='mischap2(R 2)'):
            aa24=random.choice(L10)
            L10.remove(aa24)
        elif(str(variable24.get())=='mischap2(R 4)'):
            aa24=random.choice(L11)
            L11.remove(aa24)
        elif(str(variable24.get())=='mischap2(R 6)'):
            aa24=random.choice(L12)
            L12.remove(aa24)
        elif(str(variable24.get())=='mischap2(U 2)'):
            aa24=random.choice(L13)
            L13.remove(aa24)
        elif(str(variable24.get())=='mischap2(U 4)'):
            aa24=random.choice(L14)
            L14.remove(aa24)
        elif(str(variable24.get())=='mischap2(U 6)'):
            aa24=random.choice(L15)
            L15.remove(aa24)
        elif(str(variable24.get())=='mischap2(A 2)'):
            aa24=random.choice(L16)
            L16.remove(aa24)
        elif(str(variable24.get())=='mischap2(A 4)'):
            aa24=random.choice(L17)
            L17.remove(aa24)
        elif(str(variable24.get())=='mischap2(A 6)'):
            aa24=random.choice(L18)
            L18.remove(aa24)
        elif(str(variable24.get())=='mischap3(R 2)'):
            aa24=random.choice(L19)
            L19.remove(aa24)
        elif(str(variable24.get())=='mischap3(R 4)'):
            aa24=random.choice(L20)
            L20.remove(aa24)
        elif(str(variable24.get())=='mischap3(R 6)'):
            aa24=random.choice(L21)
            L21.remove(aa24)
        elif(str(variable24.get())=='mischap3(U 2)'):
            aa24=random.choice(L22)
            L22.remove(aa24)
        elif(str(variable24.get())=='mischap3(U 4)'):
            aa24=random.choice(L23)
            L23.remove(aa24)
        elif(str(variable24.get())=='mischap3(U 6)'):
            aa24=random.choice(L24)
            L24.remove(aa24)
        elif(str(variable24.get())=='mischap3(A 2)'):
            aa24=random.choice(L25)
            L25.remove(aa24)
        elif(str(variable24.get())=='mischap3(A 4)'):
            aa24=random.choice(L26)
            L26.remove(aa24)
        elif(str(variable24.get())=='mischap3(A 6)'):
            aa24=random.choice(L27)
            L27.remove(aa24)
        elif(str(variable24.get())=='mischap4(R 2)'):
            aa24=random.choice(L28)
            L28.remove(aa24)
        elif(str(variable24.get())=='mischap4(R 4)'):
            aa24=random.choice(L29)
            L29.remove(aa24)
        elif(str(variable24.get())=='mischap4(R 6)'):
            aa24=random.choice(L30)
            L30.remove(aa24)
        elif(str(variable24.get())=='mischap4(U 2)'):
            aa24=random.choice(L31)
            L31.remove(aa24)
        elif(str(variable24.get())=='mischap4(U 4)'):
            aa24=random.choice(L32)
            L32.remove(aa24)
        elif(str(variable24.get())=='mischap4(U 6)'):
            aa24=random.choice(L33)
            L33.remove(aa24)
        elif(str(variable24.get())=='mischap4(A 2)'):
            aa24=random.choice(L34)
            L34.remove(aa24)
        elif(str(variable24.get())=='mischap4(A 4)'):
            aa24=random.choice(L35)
            L35.remove(aa24)
        elif(str(variable24.get())=='mischap4(A 6)'):
            aa24=random.choice(L36)
            L36.remove(aa24)
        elif(str(variable24.get())=='mischap5(R 2)'):
            aa24=random.choice(L37)
            L37.remove(aa24)
        elif(str(variable24.get())=='mischap5(R 4)'):
            aa24=random.choice(L38)
            L38.remove(aa24)
        elif(str(variable24.get())=='mischap5(R 6)'):
            aa24=random.choice(L39)
            L39.remove(aa24)
        elif(str(variable24.get())=='mischap5(U 2)'):
            aa24=random.choice(L40)
            L40.remove(aa24)
        elif(str(variable24.get())=='mischap5(U 4)'):
            aa24=random.choice(L41)
            L41.remove(aa24)
        elif(str(variable24.get())=='mischap5(U 6)'):
            aa24=random.choice(L42)
            L42.remove(aa24)
        elif(str(variable24.get())=='mischap5(A 2)'):
            aa24=random.choice(L43)
            L43.remove(aa24)
        elif(str(variable24.get())=='mischap5(A 4)'):
            aa24=random.choice(L44)
            L44.remove(aa24)
        elif(str(variable24.get())=='mischap5(A 6)'):
            aa24=random.choice(L45)
            L45.remove(aa24)

    canvas.create_window((300,1580), anchor='nw', window=s)

      #Question 5 .c
    canvas.create_text((230,1620),anchor=NW, text="   c",font= (20))
    variable25 = StringVar(root)
    c26=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)","pychap6(R 2)","pychap6(R 4)","pychap6(R 6)","pychap6(U 2)","pychap6(U 4)","pychap6(U 6)","pychap6(A 2)","pychap6(A 4)","pychap6(A 6)"]
    s=Spinbox(canvas,values=c26,textvariabl=variable25,state='readonly',wrap=True)
    def om26():
        global aa25
        if(str(variable25.get())=='mischap1(R 2)'):
            aa25=random.choice(L1)
            L1.remove(aa25)
        elif(str(variable25.get())=='mischap1(R 4)'):
            aa25=random.choice(L2)
            L2.remove(aa25)
        elif(str(variable25.get())=='mischap1(R 6)'):
            aa25=random.choice(L3)
            L3.remove(aa25)
        elif(str(variable25.get())=='mischap1(U 2)'):
            aa25=random.choice(L4)
            L4.remove(aa25)
        elif(str(variable25.get())=='mischap1(U 4)'):
            aa25=random.choice(L5)
            L5.remove(aa25)
        elif(str(variable25.get())=='mischap1(U 6)'):
            aa25=random.choice(L6)
            L6.remove(aa25)
        elif(str(variable25.get())=='mischap1(A 2)'):
            aa25=random.choice(L7)
            L7.remove(aa25)
        elif(str(variable25.get())=='mischap1(A 4)'):
            aa25=random.choice(L8)
            L8.remove(aa25)
        elif(str(variable25.get())=='mischap1(A 6)'):
            aa25=random.choice(L9)
            L9.remove(aa25)
        elif(str(variable25.get())=='mischap2(R 2)'):
            aa25=random.choice(L10)
            L10.remove(aa25)
        elif(str(variable25.get())=='mischap2(R 4)'):
            aa25=random.choice(L11)
            L11.remove(aa25)
        elif(str(variable25.get())=='mischap2(R 6)'):
            aa25=random.choice(L12)
            L12.remove(aa25)
        elif(str(variable25.get())=='mischap2(U 2)'):
            aa25=random.choice(L13)
            L13.remove(aa25)
        elif(str(variable25.get())=='mischap2(U 4)'):
            aa25=random.choice(L14)
            L14.remove(aa25)
        elif(str(variable25.get())=='mischap2(U 6)'):
            aa25=random.choice(L15)
            L15.remove(aa25)
        elif(str(variable25.get())=='mischap2(A 2)'):
            aa25=random.choice(L16)
            L16.remove(aa25)
        elif(str(variable25.get())=='mischap2(A 4)'):
            aa25=random.choice(L17)
            L17.remove(aa25)
        elif(str(variable25.get())=='mischap2(A 6)'):
            aa25=random.choice(L18)
            L18.remove(aa25)
        elif(str(variable25.get())=='mischap3(R 2)'):
            aa25=random.choice(L19)
            L19.remove(aa25)
        elif(str(variable25.get())=='mischap3(R 4)'):
            aa25=random.choice(L20)
            L20.remove(aa25)
        elif(str(variable25.get())=='mischap3(R 6)'):
            aa25=random.choice(L21)
            L21.remove(aa25)
        elif(str(variable25.get())=='mischap3(U 2)'):
            aa25=random.choice(L22)
            L22.remove(aa25)
        elif(str(variable25.get())=='mischap3(U 4)'):
            aa25=random.choice(L23)
            L23.remove(aa25)
        elif(str(variable25.get())=='mischap3(U 6)'):
            aa25=random.choice(L24)
            L24.remove(aa25)
        elif(str(variable25.get())=='mischap3(A 2)'):
            aa25=random.choice(L25)
            L25.remove(aa25)
        elif(str(variable25.get())=='mischap3(A 4)'):
            aa25=random.choice(L26)
            L26.remove(aa25)
        elif(str(variable25.get())=='mischap3(A 6)'):
            aa25=random.choice(L27)
            L27.remove(aa25)
        elif(str(variable25.get())=='mischap4(R 2)'):
            aa25=random.choice(L28)
            L28.remove(aa25)
        elif(str(variable25.get())=='mischap4(R 4)'):
            aa25=random.choice(L29)
            L29.remove(aa25)
        elif(str(variable25.get())=='mischap4(R 6)'):
            aa25=random.choice(L30)
            L30.remove(aa25)
        elif(str(variable25.get())=='mischap4(U 2)'):
            aa25=random.choice(L31)
            L31.remove(aa25)
        elif(str(variable25.get())=='mischap4(U 4)'):
            aa25=random.choice(L32)
            L32.remove(aa25)
        elif(str(variable25.get())=='mischap4(U 6)'):
            aa25=random.choice(L33)
            L33.remove(aa25)
        elif(str(variable25.get())=='mischap4(A 2)'):
            aa25=random.choice(L34)
            L34.remove(aa25)
        elif(str(variable25.get())=='mischap4(A 4)'):
            aa25=random.choice(L35)
            L35.remove(aa25)
        elif(str(variable25.get())=='mischap4(A 6)'):
            aa25=random.choice(L36)
            L36.remove(aa25)
        elif(str(variable25.get())=='mischap5(R 2)'):
            aa25=random.choice(L37)
            L37.remove(aa25)
        elif(str(variable25.get())=='mischap5(R 4)'):
            aa25=random.choice(L38)
            L38.remove(aa25)
        elif(str(variable25.get())=='mischap5(R 6)'):
            aa25=random.choice(L39)
            L39.remove(aa25)
        elif(str(variable25.get())=='mischap5(U 2)'):
            aa25=random.choice(L40)
            L40.remove(aa25)
        elif(str(variable25.get())=='mischap5(U 4)'):
            aa25=random.choice(L41)
            L41.remove(aa25)
        elif(str(variable25.get())=='mischap5(U 6)'):
            aa25=random.choice(L42)
            L42.remove(aa25)
        elif(str(variable25.get())=='mischap5(A 2)'):
            aa25=random.choice(L43)
            L43.remove(aa25)
        elif(str(variable25.get())=='mischap5(A 4)'):
            aa25=random.choice(L44)
            L44.remove(aa25)
        elif(str(variable25.get())=='mischap5(A 6)'):
            aa25=random.choice(L45)
            L45.remove(aa25)

    canvas.create_window((300,1620), anchor='nw', window=s)

      #Question 5 .d
    canvas.create_text((230,1660),anchor=NW, text="   d",font= (20))
    variable26 = StringVar(root)
    c27=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)","pychap6(R 2)","pychap6(R 4)","pychap6(R 6)","pychap6(U 2)","pychap6(U 4)","pychap6(U 6)","pychap6(A 2)","pychap6(A 4)","pychap6(A 6)"]
    s=Spinbox(canvas,values=c27,textvariabl=variable26,state='readonly',wrap=True)
    def om27():
        global aa26
        if(str(variable26.get())=='mischap1(R 2)'):
            aa26=random.choice(L1)
            L1.remove(aa26)
        elif(str(variable26.get())=='mischap1(R 4)'):
            aa26=random.choice(L2)
            L2.remove(aa26)
        elif(str(variable26.get())=='mischap1(R 6)'):
            aa26=random.choice(L3)
            L3.remove(aa26)
        elif(str(variable26.get())=='mischap1(U 2)'):
            aa26=random.choice(L4)
            L4.remove(aa26)
        elif(str(variable26.get())=='mischap1(U 4)'):
            aa26=random.choice(L5)
            L5.remove(aa26)
        elif(str(variable26.get())=='mischap1(U 6)'):
            aa26=random.choice(L6)
            L6.remove(aa26)
        elif(str(variable26.get())=='mischap1(A 2)'):
            aa26=random.choice(L7)
            L7.remove(aa26)
        elif(str(variable26.get())=='mischap1(A 4)'):
            aa26=random.choice(L8)
            L8.remove(aa26)
        elif(str(variable26.get())=='mischap1(A 6)'):
            aa26=random.choice(L9)
            L9.remove(aa26)
        elif(str(variable26.get())=='mischap2(R 2)'):
            aa26=random.choice(L10)
            L10.remove(aa26)
        elif(str(variable26.get())=='mischap2(R 4)'):
            aa26=random.choice(L11)
            L11.remove(aa26)
        elif(str(variable26.get())=='mischap2(R 6)'):
            aa26=random.choice(L12)
            L12.remove(aa26)
        elif(str(variable26.get())=='mischap2(U 2)'):
            aa26=random.choice(L13)
            L13.remove(aa26)
        elif(str(variable26.get())=='mischap2(U 4)'):
            aa26=random.choice(L14)
            L14.remove(aa26)
        elif(str(variable26.get())=='mischap2(U 6)'):
            aa26=random.choice(L15)
            L15.remove(aa26)
        elif(str(variable26.get())=='mischap2(A 2)'):
            aa26=random.choice(L16)
            L16.remove(aa26)
        elif(str(variable26.get())=='mischap2(A 4)'):
            aa26=random.choice(L17)
            L17.remove(aa26)
        elif(str(variable26.get())=='mischap2(A 6)'):
            aa26=random.choice(L18)
            L18.remove(aa26)
        elif(str(variable26.get())=='mischap3(R 2)'):
            aa26=random.choice(L19)
            L19.remove(aa26)
        elif(str(variable26.get())=='mischap3(R 4)'):
            aa26=random.choice(L20)
            L20.remove(aa26)
        elif(str(variable26.get())=='mischap3(R 6)'):
            aa26=random.choice(L21)
            L21.remove(aa26)
        elif(str(variable26.get())=='mischap3(U 2)'):
            aa26=random.choice(L22)
            L22.remove(aa26)
        elif(str(variable26.get())=='mischap3(U 4)'):
            aa26=random.choice(L23)
            L23.remove(aa26)
        elif(str(variable26.get())=='mischap3(U 6)'):
            aa26=random.choice(L24)
            L24.remove(aa26)
        elif(str(variable26.get())=='mischap3(A 2)'):
            aa26=random.choice(L25)
            L25.remove(aa26)
        elif(str(variable26.get())=='mischap3(A 4)'):
            aa26=random.choice(L26)
            L26.remove(aa26)
        elif(str(variable26.get())=='mischap3(A 6)'):
            aa26=random.choice(L27)
            L27.remove(aa26)
        elif(str(variable26.get())=='mischap4(R 2)'):
            aa26=random.choice(L28)
            L28.remove(aa26)
        elif(str(variable26.get())=='mischap4(R 4)'):
            aa26=random.choice(L29)
            L29.remove(aa26)
        elif(str(variable26.get())=='mischap4(R 6)'):
            aa26=random.choice(L30)
            L30.remove(aa26)
        elif(str(variable26.get())=='mischap4(U 2)'):
            aa26=random.choice(L31)
            L31.remove(aa26)
        elif(str(variable26.get())=='mischap4(U 4)'):
            aa26=random.choice(L32)
            L32.remove(aa26)
        elif(str(variable26.get())=='mischap4(U 6)'):
            aa26=random.choice(L33)
            L33.remove(aa26)
        elif(str(variable26.get())=='mischap4(A 2)'):
            aa26=random.choice(L34)
            L34.remove(aa26)
        elif(str(variable26.get())=='mischap4(A 4)'):
            aa26=random.choice(L35)
            L35.remove(aa26)
        elif(str(variable26.get())=='mischap4(A 6)'):
            aa26=random.choice(L36)
            L36.remove(aa26)
        elif(str(variable26.get())=='mischap5(R 2)'):
            aa26=random.choice(L37)
            L37.remove(aa26)
        elif(str(variable26.get())=='mischap5(R 4)'):
            aa26=random.choice(L38)
            L38.remove(aa26)
        elif(str(variable26.get())=='mischap5(R 6)'):
            aa26=random.choice(L39)
            L39.remove(aa26)
        elif(str(variable26.get())=='mischap5(U 2)'):
            aa26=random.choice(L40)
            L40.remove(aa26)
        elif(str(variable26.get())=='mischap5(U 4)'):
            aa26=random.choice(L41)
            L41.remove(aa26)
        elif(str(variable26.get())=='mischap5(U 6)'):
            aa26=random.choice(L42)
            L42.remove(aa26)
        elif(str(variable26.get())=='mischap5(A 2)'):
            aa26=random.choice(L43)
            L43.remove(aa26)
        elif(str(variable26.get())=='mischap5(A 4)'):
            aa26=random.choice(L44)
            L44.remove(aa26)
        elif(str(variable26.get())=='mischap5(A 6)'):
            aa26=random.choice(L45)
            L45.remove(aa26)

    canvas.create_window((300,1660), anchor='nw', window=s)

      #Question 5 .e
    canvas.create_text((230,1700),anchor=NW, text="   e",font= (20))
    variable27 = StringVar(root)
    c28=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c28,textvariabl=variable27,state='readonly',wrap=True)
    def om28():
        global aa27
        if(str(variable27.get())=='mischap1(R 2)'):
            aa27=random.choice(L1)
            L1.remove(aa27)
        elif(str(variable27.get())=='mischap1(R 4)'):
            aa27=random.choice(L2)
            L2.remove(aa27)
        elif(str(variable27.get())=='mischap1(R 6)'):
            aa27=random.choice(L3)
            L3.remove(aa27)
        elif(str(variable27.get())=='mischap1(U 2)'):
            aa27=random.choice(L4)
            L4.remove(aa27)
        elif(str(variable27.get())=='mischap1(U 4)'):
            aa27=random.choice(L5)
            L5.remove(aa27)
        elif(str(variable27.get())=='mischap1(U 6)'):
            aa27=random.choice(L6)
            L6.remove(aa27)
        elif(str(variable27.get())=='mischap1(A 2)'):
            aa27=random.choice(L7)
            L7.remove(aa27)
        elif(str(variable27.get())=='mischap1(A 4)'):
            aa27=random.choice(L8)
            L8.remove(aa27)
        elif(str(variable27.get())=='mischap1(A 6)'):
            aa27=random.choice(L9)
            L9.remove(aa27)
        elif(str(variable27.get())=='mischap2(R 2)'):
            aa27=random.choice(L10)
            L10.remove(aa27)
        elif(str(variable27.get())=='mischap2(R 4)'):
            aa27=random.choice(L11)
            L11.remove(aa27)
        elif(str(variable27.get())=='mischap2(R 6)'):
            aa27=random.choice(L12)
            L12.remove(aa27)
        elif(str(variable27.get())=='mischap2(U 2)'):
            aa27=random.choice(L13)
            L13.remove(aa27)
        elif(str(variable27.get())=='mischap2(U 4)'):
            aa27=random.choice(L14)
            L14.remove(aa27)
        elif(str(variable27.get())=='mischap2(U 6)'):
            aa27=random.choice(L15)
            L15.remove(aa27)
        elif(str(variable27.get())=='mischap2(A 2)'):
            aa27=random.choice(L16)
            L16.remove(aa27)
        elif(str(variable27.get())=='mischap2(A 4)'):
            aa27=random.choice(L17)
            L17.remove(aa27)
        elif(str(variable27.get())=='mischap2(A 6)'):
            aa27=random.choice(L18)
            L18.remove(aa27)
        elif(str(variable27.get())=='mischap3(R 2)'):
            aa27=random.choice(L19)
            L19.remove(aa27)
        elif(str(variable27.get())=='mischap3(R 4)'):
            aa27=random.choice(L20)
            L20.remove(aa27)
        elif(str(variable27.get())=='mischap3(R 6)'):
            aa27=random.choice(L21)
            L21.remove(aa27)
        elif(str(variable27.get())=='mischap3(U 2)'):
            aa27=random.choice(L22)
            L22.remove(aa27)
        elif(str(variable27.get())=='mischap3(U 4)'):
            aa27=random.choice(L23)
            L23.remove(aa27)
        elif(str(variable27.get())=='mischap3(U 6)'):
            aa27=random.choice(L24)
            L24.remove(aa27)
        elif(str(variable27.get())=='mischap3(A 2)'):
            aa27=random.choice(L25)
            L25.remove(aa27)
        elif(str(variable27.get())=='mischap3(A 4)'):
            aa27=random.choice(L26)
            L26.remove(aa27)
        elif(str(variable27.get())=='mischap3(A 6)'):
            aa27=random.choice(L27)
            L27.remove(aa27)
        elif(str(variable27.get())=='mischap4(R 2)'):
            aa27=random.choice(L28)
            L28.remove(aa27)
        elif(str(variable27.get())=='mischap4(R 4)'):
            aa27=random.choice(L29)
            L29.remove(aa27)
        elif(str(variable27.get())=='mischap4(R 6)'):
            aa27=random.choice(L30)
            L30.remove(aa27)
        elif(str(variable27.get())=='mischap4(U 2)'):
            aa27=random.choice(L31)
            L31.remove(aa27)
        elif(str(variable27.get())=='mischap4(U 4)'):
            aa27=random.choice(L32)
            L32.remove(aa27)
        elif(str(variable27.get())=='mischap4(U 6)'):
            aa27=random.choice(L33)
            L33.remove(aa27)
        elif(str(variable27.get())=='mischap4(A 2)'):
            aa27=random.choice(L34)
            L34.remove(aa27)
        elif(str(variable27.get())=='mischap4(A 4)'):
            aa27=random.choice(L35)
            L35.remove(aa27)
        elif(str(variable27.get())=='mischap4(A 6)'):
            aa27=random.choice(L36)
            L36.remove(aa27)
        elif(str(variable27.get())=='mischap5(R 2)'):
            aa27=random.choice(L37)
            L37.remove(aa27)
        elif(str(variable27.get())=='mischap5(R 4)'):
            aa27=random.choice(L38)
            L38.remove(aa27)
        elif(str(variable27.get())=='mischap5(R 6)'):
            aa27=random.choice(L39)
            L39.remove(aa27)
        elif(str(variable27.get())=='mischap5(U 2)'):
            aa27=random.choice(L40)
            L40.remove(aa27)
        elif(str(variable27.get())=='mischap5(U 4)'):
            aa27=random.choice(L41)
            L41.remove(aa27)
        elif(str(variable27.get())=='mischap5(U 6)'):
            aa27=random.choice(L42)
            L42.remove(aa27)
        elif(str(variable27.get())=='mischap5(A 2)'):
            aa27=random.choice(L43)
            L43.remove(aa27)
        elif(str(variable27.get())=='mischap5(A 4)'):
            aa27=random.choice(L44)
            L44.remove(aa27)
        elif(str(variable27.get())=='mischap5(A 6)'):
            aa27=random.choice(L45)
            L45.remove(aa27)

    canvas.create_window((300,1700), anchor='nw', window=s)

#-----------------------------------------------------------------------------------------------------------------------------
#                                                         Question6 Start
#-------------------------------------------------------------------------------------------------------------------------------------
    canvas.create_text((230,1740),anchor=NW, text="Q.6              Attempt any TWO                                                                          12Marks",font= ("bold",15))

      #Question 6 .a
    canvas.create_text((230,1780),anchor=NW, text="   a",font= (20))
    variable28 = StringVar(root)
    c29=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c29,textvariabl=variable28,state='readonly',wrap=True)
    def om29():
        global aa28
        if(str(variable28.get())=='mischap1(R 2)'):
            aa28=random.choice(L1)
            L1.remove(aa28)
        elif(str(variable28.get())=='mischap1(R 4)'):
            aa28=random.choice(L2)
            L2.remove(aa28)
        elif(str(variable28.get())=='mischap1(R 6)'):
            aa28=random.choice(L3)
            L3.remove(aa28)
        elif(str(variable28.get())=='mischap1(U 2)'):
            aa28=random.choice(L4)
            L4.remove(aa28)
        elif(str(variable28.get())=='mischap1(U 4)'):
            aa28=random.choice(L5)
            L5.remove(aa28)
        elif(str(variable28.get())=='mischap1(U 6)'):
            aa28=random.choice(L6)
            L6.remove(aa28)
        elif(str(variable28.get())=='mischap1(A 2)'):
            aa28=random.choice(L7)
            L7.remove(aa28)
        elif(str(variable28.get())=='mischap1(A 4)'):
            aa28=random.choice(L8)
            L8.remove(aa28)
        elif(str(variable28.get())=='mischap1(A 6)'):
            aa28=random.choice(L9)
            L9.remove(aa28)
        elif(str(variable28.get())=='mischap2(R 2)'):
            aa28=random.choice(L10)
            L10.remove(aa28)
        elif(str(variable28.get())=='mischap2(R 4)'):
            aa28=random.choice(L11)
            L11.remove(aa28)
        elif(str(variable28.get())=='mischap2(R 6)'):
            aa28=random.choice(L12)
            L12.remove(aa28)
        elif(str(variable28.get())=='mischap2(U 2)'):
            aa28=random.choice(L13)
            L13.remove(aa28)
        elif(str(variable28.get())=='mischap2(U 4)'):
            aa28=random.choice(L14)
            L14.remove(aa28)
        elif(str(variable28.get())=='mischap2(U 6)'):
            aa28=random.choice(L15)
            L15.remove(aa28)
        elif(str(variable28.get())=='mischap2(A 2)'):
            aa28=random.choice(L16)
            L16.remove(aa28)
        elif(str(variable28.get())=='mischap2(A 4)'):
            aa28=random.choice(L17)
            L17.remove(aa28)
        elif(str(variable28.get())=='mischap2(A 6)'):
            aa28=random.choice(L18)
            L18.remove(aa28)
        elif(str(variable28.get())=='mischap3(R 2)'):
            aa28=random.choice(L19)
            L19.remove(aa28)
        elif(str(variable28.get())=='mischap3(R 4)'):
            aa28=random.choice(L20)
            L20.remove(aa28)
        elif(str(variable28.get())=='mischap3(R 6)'):
            aa28=random.choice(L21)
            L21.remove(aa28)
        elif(str(variable28.get())=='mischap3(U 2)'):
            aa28=random.choice(L22)
            L22.remove(aa28)
        elif(str(variable28.get())=='mischap3(U 4)'):
            aa28=random.choice(L23)
            L23.remove(aa28)
        elif(str(variable28.get())=='mischap3(U 6)'):
            aa28=random.choice(L24)
            L24.remove(aa28)
        elif(str(variable28.get())=='mischap3(A 2)'):
            aa28=random.choice(L25)
            L25.remove(aa28)
        elif(str(variable28.get())=='mischap3(A 4)'):
            aa28=random.choice(L26)
            L26.remove(aa28)
        elif(str(variable28.get())=='mischap3(A 6)'):
            aa28=random.choice(L27)
            L27.remove(aa28)
        elif(str(variable28.get())=='mischap4(R 2)'):
            aa28=random.choice(L28)
            L28.remove(aa28)
        elif(str(variable28.get())=='mischap4(R 4)'):
            aa28=random.choice(L29)
            L29.remove(aa28)
        elif(str(variable28.get())=='mischap4(R 6)'):
            aa28=random.choice(L30)
            L30.remove(aa28)
        elif(str(variable28.get())=='mischap4(U 2)'):
            aa28=random.choice(L31)
            L31.remove(aa28)
        elif(str(variable28.get())=='mischap4(U 4)'):
            aa28=random.choice(L32)
            L32.remove(aa28)
        elif(str(variable28.get())=='mischap4(U 6)'):
            aa28=random.choice(L33)
            L33.remove(aa28)
        elif(str(variable28.get())=='mischap4(A 2)'):
            aa28=random.choice(L34)
            L34.remove(aa28)
        elif(str(variable28.get())=='mischap4(A 4)'):
            aa28=random.choice(L35)
            L35.remove(aa28)
        elif(str(variable28.get())=='mischap4(A 6)'):
            aa28=random.choice(L36)
            L36.remove(aa28)
        elif(str(variable28.get())=='mischap5(R 2)'):
            aa28=random.choice(L37)
            L37.remove(aa28)
        elif(str(variable28.get())=='mischap5(R 4)'):
            aa28=random.choice(L38)
            L38.remove(aa28)
        elif(str(variable28.get())=='mischap5(R 6)'):
            aa28=random.choice(L39)
            L39.remove(aa28)
        elif(str(variable28.get())=='mischap5(U 2)'):
            aa28=random.choice(L40)
            L40.remove(aa28)
        elif(str(variable28.get())=='mischap5(U 4)'):
            aa28=random.choice(L41)
            L41.remove(aa28)
        elif(str(variable28.get())=='mischap5(U 6)'):
            aa28=random.choice(L42)
            L42.remove(aa28)
        elif(str(variable28.get())=='mischap5(A 2)'):
            aa28=random.choice(L43)
            L43.remove(aa28)
        elif(str(variable28.get())=='mischap5(A 4)'):
            aa28=random.choice(L44)
            L44.remove(aa28)
        elif(str(variable28.get())=='mischap5(A 6)'):
            aa28=random.choice(L45)
            L45.remove(aa28)
    canvas.create_window((300,1780), anchor='nw', window=s)

      #Question 6 .b
    canvas.create_text((230,1820),anchor=NW, text="   b",font= (20))
    variable29 = StringVar(root)
    c30=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c30,textvariabl=variable29,state='readonly',wrap=True)
    def om30():
        global aa29
        if(str(variable29.get())=='mischap1(R 2)'):
            aa29=random.choice(L1)
            L1.remove(aa29)
        elif(str(variable29.get())=='mischap1(R 4)'):
            aa29=random.choice(L2)
            L2.remove(aa29)
        elif(str(variable29.get())=='mischap1(R 6)'):
            aa29=random.choice(L3)
            L3.remove(aa29)
        elif(str(variable29.get())=='mischap1(U 2)'):
            aa29=random.choice(L4)
            L4.remove(aa29)
        elif(str(variable29.get())=='mischap1(U 4)'):
            aa29=random.choice(L5)
            L5.remove(aa29)
        elif(str(variable29.get())=='mischap1(U 6)'):
            aa29=random.choice(L6)
            L6.remove(aa29)
        elif(str(variable29.get())=='mischap1(A 2)'):
            aa29=random.choice(L7)
            L7.remove(aa29)
        elif(str(variable29.get())=='mischap1(A 4)'):
            aa29=random.choice(L8)
            L8.remove(aa29)
        elif(str(variable29.get())=='mischap1(A 6)'):
            aa29=random.choice(L9)
            L9.remove(aa29)
        elif(str(variable29.get())=='mischap2(R 2)'):
            aa29=random.choice(L10)
            L10.remove(aa29)
        elif(str(variable29.get())=='mischap2(R 4)'):
            aa29=random.choice(L11)
            L11.remove(aa29)
        elif(str(variable29.get())=='mischap2(R 6)'):
            aa29=random.choice(L12)
            L12.remove(aa29)
        elif(str(variable29.get())=='mischap2(U 2)'):
            aa29=random.choice(L13)
            L13.remove(aa29)
        elif(str(variable29.get())=='mischap2(U 4)'):
            aa29=random.choice(L14)
            L14.remove(aa29)
        elif(str(variable29.get())=='mischap2(U 6)'):
            aa29=random.choice(L15)
            L15.remove(aa29)
        elif(str(variable29.get())=='mischap2(A 2)'):
            aa29=random.choice(L16)
            L16.remove(aa29)
        elif(str(variable29.get())=='mischap2(A 4)'):
            aa29=random.choice(L17)
            L17.remove(aa29)
        elif(str(variable29.get())=='mischap2(A 6)'):
            aa29=random.choice(L18)
            L18.remove(aa29)
        elif(str(variable29.get())=='mischap3(R 2)'):
            aa29=random.choice(L19)
            L19.remove(aa29)
        elif(str(variable29.get())=='mischap3(R 4)'):
            aa29=random.choice(L20)
            L20.remove(aa29)
        elif(str(variable29.get())=='mischap3(R 6)'):
            aa29=random.choice(L21)
            L21.remove(aa29)
        elif(str(variable29.get())=='mischap3(U 2)'):
            aa29=random.choice(L22)
            L22.remove(aa29)
        elif(str(variable29.get())=='mischap3(U 4)'):
            aa29=random.choice(L23)
            L23.remove(aa29)
        elif(str(variable29.get())=='mischap3(U 6)'):
            aa29=random.choice(L24)
            L24.remove(aa29)
        elif(str(variable29.get())=='mischap3(A 2)'):
            aa29=random.choice(L25)
            L25.remove(aa29)
        elif(str(variable29.get())=='mischap3(A 4)'):
            aa29=random.choice(L26)
            L26.remove(aa29)
        elif(str(variable29.get())=='mischap3(A 6)'):
            aa29=random.choice(L27)
            L27.remove(aa29)
        elif(str(variable29.get())=='mischap4(R 2)'):
            aa29=random.choice(L28)
            L28.remove(aa29)
        elif(str(variable29.get())=='mischap4(R 4)'):
            aa29=random.choice(L29)
            L29.remove(aa29)
        elif(str(variable29.get())=='mischap4(R 6)'):
            aa29=random.choice(L30)
            L30.remove(aa29)
        elif(str(variable29.get())=='mischap4(U 2)'):
            aa29=random.choice(L31)
            L31.remove(aa29)
        elif(str(variable29.get())=='mischap4(U 4)'):
            aa29=random.choice(L32)
            L32.remove(aa29)
        elif(str(variable29.get())=='mischap4(U 6)'):
            aa29=random.choice(L33)
            L33.remove(aa29)
        elif(str(variable29.get())=='mischap4(A 2)'):
            aa29=random.choice(L34)
            L34.remove(aa29)
        elif(str(variable29.get())=='mischap4(A 4)'):
            aa29=random.choice(L35)
            L35.remove(aa29)
        elif(str(variable29.get())=='mischap4(A 6)'):
            aa29=random.choice(L36)
            L36.remove(aa29)
        elif(str(variable29.get())=='mischap5(R 2)'):
            aa29=random.choice(L37)
            L37.remove(aa29)
        elif(str(variable29.get())=='mischap5(R 4)'):
            aa29=random.choice(L38)
            L38.remove(aa29)
        elif(str(variable29.get())=='mischap5(R 6)'):
            aa29=random.choice(L39)
            L39.remove(aa29)
        elif(str(variable29.get())=='mischap5(U 2)'):
            aa29=random.choice(L40)
            L40.remove(aa29)
        elif(str(variable29.get())=='mischap5(U 4)'):
            aa29=random.choice(L41)
            L41.remove(aa29)
        elif(str(variable29.get())=='mischap5(U 6)'):
            aa29=random.choice(L42)
            L42.remove(aa29)
        elif(str(variable29.get())=='mischap5(A 2)'):
            aa29=random.choice(L43)
            L43.remove(aa29)
        elif(str(variable29.get())=='mischap5(A 4)'):
            aa29=random.choice(L44)
            L44.remove(aa29)
        elif(str(variable29.get())=='mischap5(A 6)'):
            aa29=random.choice(L45)
            L45.remove(aa29)
    canvas.create_window((300,1820), anchor='nw', window=s)

      #Question 6 .C
    canvas.create_text((230,1860),anchor=NW, text="   c",font= (20))
    variable30 = StringVar(root)
    c31=["mischap1(R 2)","mischap1(R 4)","mischap1(R 6)","mischap1(U 2)","mischap1(U 4)","mischap1(U 6)","mischap1(A 2)","mischap1(A 4)","mischap1(A 6)","mischap2(R 2)","mischap2(R 4)","mischap2(R 6)","mischap2(U 2)","mischap2(U 4)","mischap2(U 6)","mischap2(A 2)","mischap2(A 4)","mischap2(A 6)","mischap3(R 2)","mischap3(R 4)","mischap3(R 6)","mischap3(U 2)","mischap3(U 4)","mischap3(U 6)","mischap3(A 2)","mischap3(A 4)","mischap3(A 6)","mischap4(R 2)","mischap4(R 4)","mischap4(R 6)","mischap4(U 2)","mischap4(U 4)","mischap4(U 6)","mischap4(A 2)","mischap4(A 4)","mischap4(A 6)","mischap5(R 2)","mischap5(R 4)","mischap5(R 6)","mischap5(U 2)","mischap5(U 4)","mischap5(U 6)","mischap5(A 2)","mischap5(A 4)","mischap5(A 6)"]
    s=Spinbox(canvas,values=c31,textvariabl=variable30,state='readonly',wrap=True)
    def om31():
        global aa30
        if(str(variable30.get())=='mischap1(R 2)'):
            aa30=random.choice(L1)
            L1.remove(aa30)
        elif(str(variable30.get())=='mischap1(R 4)'):
            aa30=random.choice(L2)
            L2.remove(aa30)
        elif(str(variable30.get())=='mischap1(R 6)'):
            aa30=random.choice(L3)
            L3.remove(aa30)
        elif(str(variable30.get())=='mischap1(U 2)'):
            aa30=random.choice(L4)
            L4.remove(aa30)
        elif(str(variable30.get())=='mischap1(U 4)'):
            aa30=random.choice(L5)
            L5.remove(aa30)
        elif(str(variable30.get())=='mischap1(U 6)'):
            aa30=random.choice(L6)
            L6.remove(aa30)
        elif(str(variable30.get())=='mischap1(A 2)'):
            aa30=random.choice(L7)
            L7.remove(aa30)
        elif(str(variable30.get())=='mischap1(A 4)'):
            aa30=random.choice(L8)
            L8.remove(aa30)
        elif(str(variable30.get())=='mischap1(A 6)'):
            aa30=random.choice(L9)
            L9.remove(aa30)
        elif(str(variable30.get())=='mischap2(R 2)'):
            aa30=random.choice(L10)
            L10.remove(aa30)
        elif(str(variable30.get())=='mischap2(R 4)'):
            aa30=random.choice(L11)
            L11.remove(aa30)
        elif(str(variable30.get())=='mischap2(R 6)'):
            aa30=random.choice(L12)
            L12.remove(aa30)
        elif(str(variable30.get())=='mischap2(U 2)'):
            aa30=random.choice(L13)
            L13.remove(aa30)
        elif(str(variable30.get())=='mischap2(U 4)'):
            aa30=random.choice(L14)
            L14.remove(aa30)
        elif(str(variable30.get())=='mischap2(U 6)'):
            aa30=random.choice(L15)
            L15.remove(aa30)
        elif(str(variable30.get())=='mischap2(A 2)'):
            aa30=random.choice(L16)
            L16.remove(aa30)
        elif(str(variable30.get())=='mischap2(A 4)'):
            aa30=random.choice(L17)
            L17.remove(aa30)
        elif(str(variable30.get())=='mischap2(A 6)'):
            aa30=random.choice(L18)
            L18.remove(aa30)
        elif(str(variable30.get())=='mischap3(R 2)'):
            aa30=random.choice(L19)
            L19.remove(aa30)
        elif(str(variable30.get())=='mischap3(R 4)'):
            aa30=random.choice(L20)
            L20.remove(aa30)
        elif(str(variable30.get())=='mischap3(R 6)'):
            aa30=random.choice(L21)
            L21.remove(aa30)
        elif(str(variable30.get())=='mischap3(U 2)'):
            aa30=random.choice(L22)
            L22.remove(aa30)
        elif(str(variable30.get())=='mischap3(U 4)'):
            aa30=random.choice(L23)
            L23.remove(aa30)
        elif(str(variable30.get())=='mischap3(U 6)'):
            aa30=random.choice(L24)
            L24.remove(aa30)
        elif(str(variable30.get())=='mischap3(A 2)'):
            aa30=random.choice(L25)
            L25.remove(aa30)
        elif(str(variable30.get())=='mischap3(A 4)'):
            aa30=random.choice(L26)
            L26.remove(aa30)
        elif(str(variable30.get())=='mischap3(A 6)'):
            aa30=random.choice(L27)
            L27.remove(aa30)
        elif(str(variable30.get())=='mischap4(R 2)'):
            aa30=random.choice(L28)
            L28.remove(aa30)
        elif(str(variable30.get())=='mischap4(R 4)'):
            aa30=random.choice(L29)
            L29.remove(aa30)
        elif(str(variable30.get())=='mischap4(R 6)'):
            aa30=random.choice(L30)
            L30.remove(aa30)
        elif(str(variable30.get())=='mischap4(U 2)'):
            aa30=random.choice(L31)
            L31.remove(aa30)
        elif(str(variable30.get())=='mischap4(U 4)'):
            aa30=random.choice(L32)
            L32.remove(aa30)
        elif(str(variable30.get())=='mischap4(U 6)'):
            aa30=random.choice(L33)
            L33.remove(aa30)
        elif(str(variable30.get())=='mischap4(A 2)'):
            aa30=random.choice(L34)
            L34.remove(aa30)
        elif(str(variable30.get())=='mischap4(A 4)'):
            aa30=random.choice(L35)
            L35.remove(aa30)
        elif(str(variable30.get())=='mischap4(A 6)'):
            aa30=random.choice(L36)
            L36.remove(aa30)
        elif(str(variable30.get())=='mischap5(R 2)'):
            aa30=random.choice(L37)
            L37.remove(aa30)
        elif(str(variable30.get())=='mischap5(R 4)'):
            aa30=random.choice(L38)
            L38.remove(aa30)
        elif(str(variable30.get())=='mischap5(R 6)'):
            aa30=random.choice(L39)
            L39.remove(aa30)
        elif(str(variable30.get())=='mischap5(U 2)'):
            aa30=random.choice(L40)
            L40.remove(aa30)
        elif(str(variable30.get())=='mischap5(U 4)'):
            aa30=random.choice(L41)
            L41.remove(aa30)
        elif(str(variable30.get())=='mischap5(U 6)'):
            aa30=random.choice(L42)
            L42.remove(aa30)
        elif(str(variable30.get())=='mischap5(A 2)'):
            aa30=random.choice(L43)
            L43.remove(aa30)
        elif(str(variable30.get())=='mischap5(A 4)'):
            aa30=random.choice(L44)
            L44.remove(aa30)
        elif(str(variable30.get())=='mischap5(A 6)'):
            aa30=random.choice(L45)
            L45.remove(aa30)
    canvas.create_window((300,1860), anchor='nw', window=s)
    


    
    def om3():
        om(),om1(),om2(),om4(),om5(),om6(),om7()
        om8(),om9(),om10(),om11(),om12(),om13()
        om14(),om15(),om16(),om17(),om18(),om19(),om20(),om21()
        om22(),om23(),om24(),om25(),om26(),om27(),om28()
        om29(),om30(),om31()
        next1()
    b=Button(canvas,text="Submit",bg="lightgreen",command=om3)
    canvas.create_window((700,1900), anchor='nw', window=b)







