# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:45:21 2021

@author: Chad.Daud
"""
# -*- coding: utf-8 -*-

from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry, dateentry

conn = sqlite3.connect('assetman.db')
#print("Opened database successfully")

c = conn.cursor()

def datepicker():
        win= Tk()
        #Set the Geometry
        win.geometry("450x250")
        win.title("Date Picker")
        #Create a Label
        Label(win, text= "Choose a Date", background= 'blue1', foreground="grey").pack(padx=20,pady=20)
        #Create a Calendar using DateEntry
        cal = DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.pack(pady=20)
        win.mainloop()

"""
c.execute('''CREATE TABLE assetmanagement
        (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         QUANTITIES        TEXT   NOT NULL,
         DESCRIPTION    TEXT     NOT NULL,
         IDTAG          TEXT     NOT NULL,
         CATEGORY         TEXT    NOT NULL,
         LOCATION         TEXT     NOT NULL,
         PURCHASEDATE        REAL     NOT NULL,
         SUPPLIER        TEXT      NOT NULL,
         WARRANTYEXPIRATION       REAL    NOT NULL,
         UNITCOST           INT     NOT NULL,
         SERIAL          TEXT       NOT NULL,
         MODEL           TEXT     NOT NULL
         
         );''')

"""      
print ("Table created successfully")

#conn.close()

window=Tk()
window.geometry('900x850')
bg = PhotoImage(file="C:\\Users\\Chad.Daud\\Pictures\\CdLife.png")
window.title("CDLIFE - ASSET MANAGER")
label=Label(window, image = bg, font=('algerian',20,'bold'))
label.place(x=0, y=0)
# Define the labels

lb1=Label(window, text="NAME")
lb1.grid(row=0,column=0)

lb1=Label(window, text="QTY")
lb1.grid(row=0,column=2)

lb1=Label(window, text="DESCRIPTION")
lb1.grid(row=1,column=0)

lb1=Label(window, text="ID TAG")
lb1.grid(row=1,column=2)

lb1=Label(window, text="CATEGORY")
lb1.grid(row=2,column=0)

lb1=Label(window, text="LOCATION")
lb1.grid(row=2,column=2)

lb1=Label(window, text="PURCHASE DATE")
lb1.grid(row=3,column=0)

lb1=Label(window, text="SUPPLIER")
lb1.grid(row=3,column=2)

lb1=Label(window, text="WARRANTY")
DateButton = Button(window, text="Pick Date", command=datepicker).grid(row=4, column=5)  
lb1.grid(row=4,column=2)

lb1=Label(window, text="UNIT COST")
lb1.grid(row=4,column=2)

lb1=Label(window, text="SERIAL NO:")
lb1.grid(row=5,column=0)

lb1=Label(window, text="MODEL NO:")
lb1.grid(row=5,column=2)

####DATE PICKER




#define Entries
name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)


qty_text=StringVar()
e2=Entry(window,textvariable=qty_text)
e2.grid(row=0,column=3)


desc_text=StringVar()
e3=Entry(window,textvariable=desc_text)
e3.grid(row=1,column=1)

tag_text=StringVar()
e4=Entry(window,textvariable=tag_text)
e4.grid(row=1,column=3)

##Other
cat_text=StringVar()
e5=Entry(window,textvariable=cat_text)
e5.grid(row=2,column=1)


location_text=StringVar()
e6=Entry(window,textvariable=location_text)
e6.grid(row=2,column=3)


pur_text=StringVar()
e7=Entry(window,textvariable=pur_text)
e7.grid(row=3,column=1)

supplier_text=StringVar()
e8=Entry(window,textvariable=supplier_text)
e8.grid(row=3,column=3)

##Others

warranty_text=StringVar()
e9=Entry(window,textvariable=DateButton)
e9.grid(row=4,column=1)


unitcost_text=StringVar()
e10=Entry(window,textvariable=unitcost_text)
e10.grid(row=4,column=3)


serial_text=StringVar()
e11=Entry(window,textvariable=serial_text)
e11.grid(row=5,column=1)

model_text=StringVar()
e12=Entry(window,textvariable=model_text)
e12.grid(row=5,column=3)


#define ListBox
list1=Listbox(window, height=25, width=75)
list1.grid(row=12,column=1,rowspan=10, columnspan=3)


#Attach Scrollbar(window)
sb1=Scrollbar(window)
sb1.grid(row=12,column=6,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#b1=Button(window,text="View All", width=12)
#b1.grid(row=2,column=3)

b1=Button(window,text="Search Entry", width=12)
b1.grid(row=3,column=6)

b1=Button(window,text="Add Entry", width=12)
b1.grid(row=4,column=6)

b1=Button(window,text="Update", width=12)
b1.grid(row=5,column=6)

b1=Button(window,text="Delete", width=12)
b1.grid(row=6,column=6)
#b1=Button(window,text="Delete Selected", width=12)
#b1.grid(row=6,column=3)

#b1=Button(window,text="Close", width=12)
#b1.grid(row=7,column=3)

window.mainloop()



#####

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:12:16 2021

@author: Administrator
"""

#Import tkinter library
#from tkinter import *
#from tkcalendar import Calendar, DateEntry

"""
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('500x250')  
tkWindow.title('Tkinter Login Form - Trustis')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  


#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("450x250")
win.title("Date Picker")
#Create a Label
Label(win, text= "Choose a Date", background= 'blue1', foreground="grey").pack(padx=20,pady=20)
#Create a Calendar using DateEntry
cal = DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
cal.pack(pady=20)
win.mainloop()


from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()

"""