
filename='python.pdf'
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import inch
from reportlab.lib import colors
import os


def pdf(a,b,aa,aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12,aa13,aa14,aa15,aa16,aa17,aa18,aa19,aa20,aa21,aa22,aa23,aa24,aa25,aa26,aa27,aa28,aa29,aa30):
    pdf = canvas.Canvas(filename)
    pdf.setTitle('python')
    pdf.setFont('Times-Bold',22)
    pdf.drawString(80,810,'GOVERNMENT POLYTECHNIC MUMBAI')
    pdf.setFont('Times-Bold',20)
    pdf.drawString(170,790,'TERM END EXAMINATION')
    pdf.setFont('Times-Bold',12)
    pdf.drawString(30,760,'Programme      :')
    pdf.setFont('Times-Bold',12)
    pdf.drawString(120,760,'IT')
    pdf.setFont('Times-Bold',12)
    pdf.drawString(30,740,'Course Title     :')
    pdf.setFont('Times-Bold',12)
    pdf.drawString(120,740,'Python')
    pdf.setFont('Times-Roman',12)
    pdf.drawString(30,720,'03Hours/70marks')
    pdf.setFont('Times-Roman',12)
    pdf.drawString(200,720,'Enrolment No.')
    pdf.rect(280,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(305,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(330,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(355,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(380,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(405,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(430,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(455,715,width=25,height=20,stroke=1,fill=0)
    pdf.rect(480,715,width=25,height=20,stroke=1,fill=0)
    pdf.line(30,700,530,700)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,680,'Instructions:')
    pdf.setFont('Times-Roman',12)
    pdf.drawString(30,660,'1.  Attempt all the questions.')
    pdf.drawString(30,645,'2.  Illustrate your answer with near sketches wherever necessary.')
    pdf.drawString(30,630,'3.  Use of Mathematical Tables,Steam Table and Pocket Calculator(non-programmable) is permissible.')
    pdf.drawString(30,615,'4.  Marks on Right Hand Side indicate full marks for the question.')
    pdf.drawString(30,600,'5.  Assume suitable additional data,if necessary.')

    pdf.line(30,580,530,580)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,560,'Q.1              Attempt any SIX                                                                     12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,540,'      a.')
    pdf.drawString(60,540,aa)

    pdf.drawString(30,520,'      b.')
    pdf.drawString(60,520,aa1)

    pdf.drawString(30,500,'      c.')
    pdf.drawString(60,500,aa2)

    pdf.drawString(30,480,'      d.')
    pdf.drawString(60,480,aa3)

    pdf.drawString(30,460,'      e.')
    pdf.drawString(60,460,aa4)

    pdf.drawString(30,440,'      f.')
    pdf.drawString(60,440,aa5)

    pdf.drawString(30,420,'      g.')
    pdf.drawString(60,420,aa6)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,390,'Q.2              Attempt any THREE                                                            12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,370,'      a.')
    pdf.drawString(60,370,aa7)

    pdf.drawString(30,350,'      b.')
    pdf.drawString(60,350,aa8)

    pdf.drawString(30,330,'      c.')
    pdf.drawString(60,330,aa9)

    pdf.drawString(30,310,'      d.')
    pdf.drawString(60,310,aa10)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,290,'Q.3              Attempt any THREE                                                            12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,270,'      a.')
    pdf.drawString(60,270,aa11)

    pdf.drawString(30,250,'      b.')
    pdf.drawString(60,250,aa12)

    pdf.drawString(30,230,'      c.')
    pdf.drawString(60,230,aa13)

    pdf.drawString(30,210,'      d.')
    pdf.drawString(60,210,aa14)

    pdf.drawString(30,190,'      e.')
    pdf.drawString(60,190,aa15)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,170,'Q.4              Attempt any FIVE                                                                10Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,150,'      a.')
    pdf.drawString(60,150,aa16)

    pdf.drawString(30,130,'      b.')
    pdf.drawString(60,130,aa17)

    pdf.drawString(30,110,'      c.')
    pdf.drawString(60,110,aa18)

    pdf.drawString(30,90,'      d.')
    pdf.drawString(60,90,aa19)

    pdf.drawString(30,70,'      e.')
    pdf.drawString(60,70,aa20)

    pdf.drawString(30,50,'      f.')
    pdf.drawString(60,50,aa21)

    pdf.drawString(30,30,'      g.')
    pdf.drawString(60,30,aa22)

    pdf.showPage()

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,800,'Q.5              Attempt any THREE                                                            12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,770,'      a.')
    pdf.drawString(60,770,aa23)

    pdf.drawString(30,750,'      b.')
    pdf.drawString(60,750,aa24)

    pdf.drawString(30,730,'      c.')
    pdf.drawString(60,730,aa25)

    pdf.drawString(30,710,'      d.')
    pdf.drawString(60,710,aa26)

    pdf.drawString(30,690,'      e.')
    pdf.drawString(60,690,aa27)


    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,670,'Q.6              Attempt any TWO                                                                12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,640,'      a.')
    pdf.drawString(60,640,aa28)

    pdf.drawString(30,620,'      b.')
    pdf.drawString(60,620,aa29)

    pdf.drawString(30,600,'      c.')
    pdf.drawString(60,600,aa30)


    pdf.save()
    

