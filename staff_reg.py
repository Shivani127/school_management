import tkinter as tk
from tkinter import ttk
import mainpage
import time
import mysql.connector
from tkcalendar import *
from tkinter import messagebox as box

##def startfun():
##    win.destroy()
##    mainpage.m()
##

conn=mysql.connector.connect(host='localhost',username='root',password='12345')
cur=conn.cursor()
query1='USE school_management'
cur.execute(query1)
def reset():
    evar1.set(' ')
    evar2.set(' ')
    evar3.set(' ')
    evar4.set(' ')
    evar5.set(' ')
    evar6.set(' ')
    evar7.set(' ')
    evar8.set(' ')
    

def sub():
    name=evar1.get()
    age=evar2.get()
    sal=evar3.get()
    add=evar4.get()
    ph=evar5.get()
    cl_code=evar6.get()
    passs=evar7.get()
    passs2=evar8.get()
    if age.isnumeric()==False or sal.isnumeric()==False or ph.isnumeric()==False:
        box.showerror("Error!","Age, Salary and Phone should be numeric!!")
        
    elif len(ph)!=10:
        box.showerror("Error!","Phone must be of 10 digits !!")
    elif len(passs)!=6:
        box.showerror("Error!","Password must contain 6 characters!!")
    elif passs!=passs2:
        box.showerror("Error!","Password is not matching!!")
    else:
        cur.execute('INSERT INTO teachers_info(Name,Age,Salary,Address,Phone,Class_code,pass) VALUES(%s,%s,%s,%s,%s,(Select class_code from class_subjects where class_name=%s),%s)',(name,age,sal,add,ph,cl_code,passs))
        conn.commit()
        box.showerror("Successful!","Successfully Inserted!!")
        win.destroy()
    
    
    
    
def title_page():
    global win
    win=tk.Tk()
    win.geometry('640x500+50+50')
    win.title('Staff Registration')
    win.configure(background='orange')

    title=tk.Label(win,text='STAFF REGISTRATION',pady=20,bg='orange',fg='green',font=['Arial',18,'bold','bold']).pack()

##    img=tk.PhotoImage(file='items.png')
##    a=tk.Label(win,image=img,pady=20).pack()
    name=tk.Label(win,text='Staff Name : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=100)
    
    age=tk.Label(win,text='Age           : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=140)
    sal=tk.Label(win,text='Salary           : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=180)
    add=tk.Label(win,text='Address    : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=220)
    phone=tk.Label(win,text='Phone     : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=260)
    classs=tk.Label(win,text='Class      : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=300)
    passs=tk.Label(win,text='Password   : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=340)
    passs2=tk.Label(win,text='Confirm Password : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=380)
    submit=tk.Button(win,text='SUBMIT',font=['Arial',12,'bold','bold'],pady=5,padx=5,command=sub).place(x=100,y=440)
    re=tk.Button(win,text='RESET',font=['Arial',12,'bold','bold'],pady=5,padx=5,command=reset).place(x=400,y=440)

    global evar1,evar2,evar3,evar4,evar5,evar6,evar7,evar8
    evar1=tk.StringVar()
    evar2=tk.StringVar()
    evar3=tk.StringVar()
    evar4=tk.StringVar()
    evar5=tk.StringVar()
    evar6=tk.StringVar()
    evar7=tk.StringVar()
    evar8=tk.StringVar()
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar1).place(x=300,y=100)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar2).place(x=300,y=140)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar3).place(x=300,y=180)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar4).place(x=300,y=220)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar5).place(x=300,y=260)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar6).place(x=300,y=300)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar7).place(x=300,y=340)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar8).place(x=300,y=380)
    
    
    
    
##    start=ttk.Button(win,text='START',command=startfun).pack()

    win.mainloop()

conn.close()
