from tkinter import*
from sqlite3 import*

def drop():
    a=connect("pvp.db")
    d=a.cursor()
    d.execute("DELETE  FROM ccchap1 ")
    d.execute("DELETE  FROM ccchap2 ")
    d.execute("DELETE  FROM ccchap3 ")
    d.execute("DELETE  FROM ccchap4 ")
    d.execute("DELETE  FROM ccchap5 ")

    d.close()
    a.commit()
    

drop()
