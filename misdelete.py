from tkinter import*
from sqlite3 import*

def drop():
    a=connect("pvp.db")
    d=a.cursor()
    d.execute("DELETE  FROM mischap1 ")
    d.execute("DELETE  FROM mischap2 ")
    d.execute("DELETE  FROM mischap3 ")
    d.execute("DELETE  FROM mischap4 ")
    d.execute("DELETE  FROM mischap5 ")
    d.execute("DELETE  FROM mischap6 ")
    d.close()
    a.commit()
    

drop()
