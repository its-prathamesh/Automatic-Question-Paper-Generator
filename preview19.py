from tkinter import *
from sqlite3 import*
from tkinter.filedialog import asksaveasfile


root=Tk()
root.title("Login Page")
root.geometry("2000x15000")



def preview19(acc,bc,aa,aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12,aa13,aa14,aa15,aa16,aa17,aa18,aa19,aa20,aa21):
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.maxsize(w,h)


    canvas=Canvas(root,height=h,width=w,bd=7,relief=RIDGE,scrollregion=(0,0,0,2200),highlightcolor="#016193")
    canvas.place(x=0,y=0)
    scroll=Scrollbar(canvas,orient=VERTICAL)
    scroll.place(x=1335,y=10,relheight=0.965)
    scroll.config(command = canvas.yview )
    canvas.configure(yscrollcommand = scroll.set)


    canvas.create_text((780,15),anchor=NW, text="Course Code:",font= ("bold",13))
    ac=StringVar()
    e=Entry(canvas,textvariable=ac)
    canvas.create_window((900,17),anchor=NW,window=e)
    
    def next1():
        from pdf19 import pdf
        pdf(a,b,aa,aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12,aa13,aa14,aa15,aa16,aa17,aa18,aa19,aa20,aa21)





    canvas.create_text((300,40),anchor=NW, text="GOVERNMENT POLYTECHNIC MUMBAI",font= ("bold",25))
    canvas.create_text((350,80),anchor=NW, text="TERM END EXAMINATION",font= ("bold",25))
    global a,b

    canvas.create_text((230,130),anchor=NW, text="Programme:",font= ("bold",15))
    a=acc.get()
    canvas.create_text((350,136),anchor=NW, text=a,font= ("bold",13))

    canvas.create_text((230,170),anchor=NW, text="Course Title:",font= ("bold",15))
    b=bc.get()
    canvas.create_text((350,170),anchor=NW, text=b,font= ("bold",13))




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
    

    canvas.create_text((230,420),anchor=NW, text="Q.1              Attempt any SIX                                                                          12Marks",font= ("bold",15))
    canvas.create_text((230,460),anchor=NW, text="      a.",font= ("bold",13))
    canvas.create_text((300,460),anchor=NW, text=aa,font= ("bold",13))

    canvas.create_text((230,500),anchor=NW, text="      b.",font= ("bold",13))
    canvas.create_text((300,500),anchor=NW, text=aa1,font= ("bold",13))

    canvas.create_text((230,540),anchor=NW, text="      c.",font= ("bold",13))
    canvas.create_text((300,540),anchor=NW, text=aa2,font= ("bold",13))

    canvas.create_text((230,580),anchor=NW, text="      d.",font= ("bold",13))
    canvas.create_text((300,580),anchor=NW, text=aa3,font= ("bold",13))

    canvas.create_text((230,620),anchor=NW, text="      e.",font= ("bold",13))
    canvas.create_text((300,620),anchor=NW, text=aa4,font= ("bold",13))

    canvas.create_text((230,660),anchor=NW, text="      f.",font= ("bold",13))
    canvas.create_text((300,660),anchor=NW, text=aa5,font= ("bold",13))

    canvas.create_text((230,700),anchor=NW, text="      g.",font= ("bold",13))
    canvas.create_text((300,700),anchor=NW, text=aa6,font= ("bold",13))

    canvas.create_text((230,740),anchor=NW, text="      h.",font= ("bold",13))
    canvas.create_text((300,740),anchor=NW, text=aa7,font= ("bold",13))

    canvas.create_text((230,780),anchor=NW, text="      i.",font= ("bold",13))
    canvas.create_text((300,780),anchor=NW, text=aa8,font= ("bold",13))

    canvas.create_text((230,820),anchor=NW, text="      j.",font= ("bold",13))
    canvas.create_text((300,820),anchor=NW, text=aa9,font= ("bold",13))

    canvas.create_text((230,860),anchor=NW, text="Q.2              Attempt any THREE                                                                      12Marks",font= ("bold",15))

    canvas.create_text((230,900),anchor=NW, text="      a.",font= ("bold",13))
    canvas.create_text((300,900),anchor=NW, text=aa10,font= ("bold",13))

    canvas.create_text((230,940),anchor=NW, text="      b.",font= ("bold",13))
    canvas.create_text((300,940),anchor=NW, text=aa11,font= ("bold",13))

    canvas.create_text((230,980),anchor=NW, text="      c.",font= ("bold",13))
    canvas.create_text((300,980),anchor=NW, text=aa12,font= ("bold",13))

    canvas.create_text((230,1020),anchor=NW, text="      d.",font= ("bold",13))
    canvas.create_text((300,1020),anchor=NW, text=aa13,font= ("bold",13))

    canvas.create_text((230,1060),anchor=NW, text="Q.3              Attempt any THREE                                                                       12Marks",font= ("bold",15))

    canvas.create_text((230,1100),anchor=NW, text="      a.",font= ("bold",13))
    canvas.create_text((300,1100),anchor=NW, text=aa14,font= ("bold",13))

    canvas.create_text((230,1140),anchor=NW, text="      b.",font= ("bold",13))
    canvas.create_text((300,1140),anchor=NW, text=aa15,font= ("bold",13))

    canvas.create_text((230,1180),anchor=NW, text="      c.",font= ("bold",13))
    canvas.create_text((300,1180),anchor=NW, text=aa16,font= ("bold",13))

    canvas.create_text((230,1220),anchor=NW, text="      d.",font= ("bold",13))
    canvas.create_text((300,1220),anchor=NW, text=aa17,font= ("bold",13))

    canvas.create_text((230,1260),anchor=NW, text="      e.",font= ("bold",13))
    canvas.create_text((300,1260),anchor=NW, text=aa18,font= ("bold",13))

    canvas.create_text((230,1300),anchor=NW, text="Q.4              Attempt any TWO                                                                       12Marks",font= ("bold",15))

    canvas.create_text((230,1340),anchor=NW, text="      a.",font= ("bold",13))
    canvas.create_text((300,1340),anchor=NW, text=aa19,font= ("bold",13))

    canvas.create_text((230,1380),anchor=NW, text="      b.",font= ("bold",13))
    canvas.create_text((300,1380),anchor=NW, text=aa20,font= ("bold",13))

    canvas.create_text((230,1420),anchor=NW, text="      c.",font= ("bold",13))
    canvas.create_text((300,1420),anchor=NW, text=aa21,font= ("bold",13))

    
    button=Button(canvas,text="Save",bg="lightgreen",command=next1)
    canvas.create_window((300,1500), anchor='nw', window=button)

