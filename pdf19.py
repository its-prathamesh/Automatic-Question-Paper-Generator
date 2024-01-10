
filename='python 19 scheme.pdf'
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import inch
from reportlab.lib import colors


def pdf(a,b,aa,aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12,aa13,aa14,aa15,aa16,aa17,aa18,aa19,aa20,aa21):
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
    pdf.drawString(30,560,'Q.1              Attempt any SEVEN                                                                     14Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,540,'      a.')
    pdf.drawString(60,540,aa)

    pdf.drawString(30,515,'      b.')
    pdf.drawString(60,515,aa1)

    pdf.drawString(30,490,'      c.')
    pdf.drawString(60,490,aa2)

    pdf.drawString(30,465,'      d.')
    pdf.drawString(60,465,aa3)

    pdf.drawString(30,440,'      e.')
    pdf.drawString(60,440,aa4)

    pdf.drawString(30,415,'      f.')
    pdf.drawString(60,415,aa5)

    pdf.drawString(30,390,'      g.')
    pdf.drawString(60,390,aa6)

    pdf.drawString(30,365,'      h.')
    pdf.drawString(60,365,aa7)

    pdf.drawString(30,340,'      i.')
    pdf.drawString(60,340,aa8)

    pdf.drawString(30,315,'      j.')
    pdf.drawString(60,315,aa9)

    
    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,290,'Q.2              Attempt any THREE                                                            12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,265,'      a.')
    pdf.drawString(60,265,aa10)

    pdf.drawString(30,240,'      b.')
    pdf.drawString(60,240,aa11)

    pdf.drawString(30,215,'      c.')
    pdf.drawString(60,215,aa12)

    pdf.drawString(30,190,'      d.')
    pdf.drawString(60,190,aa13)

    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,160,'Q.3              Attempt any THREE                                                            12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,135,'      a.')
    pdf.drawString(60,135,aa14)

    pdf.drawString(30,110,'      b.')
    pdf.drawString(60,110,aa15)

    pdf.drawString(30,85,'      c.')
    pdf.drawString(60,85,aa16)

    pdf.drawString(30,60,'      d.')
    pdf.drawString(60,60,aa17)

    pdf.drawString(30,35,'      e.')
    pdf.drawString(60,35,aa18)

    pdf.showPage()
    pdf.setFont('Times-Bold',15)
    pdf.drawString(30,800,'Q.4              Attempt any TWO                                                                12Marks')

    pdf.setFont('Times-Roman',13)
    pdf.drawString(30,775,'      a.')
    pdf.drawString(60,775,aa19)

    pdf.drawString(30,750,'      b.')
    pdf.drawString(60,750,aa20)

    pdf.drawString(30,725,'      c.')
    pdf.drawString(60,725,aa21)

    pdf.save()
    
