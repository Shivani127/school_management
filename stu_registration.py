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

def cal_func():
    def calval():
        top.destroy()
        evar4.set(cal.get_date())
    top=tk.Toplevel(win)
    top.geometry('180x180+600+230')
    top.title('Select')
    
    cal=Calendar(top,font='Arial 6',selectmode='day',date_pattern='yyyy-mm-dd',year=2019,month=5,day=17)
    cal.pack(fill='both',expand=True)
    btn3=tk.Button(top,text='OK',bg='grey',fg='blue',command=calval).pack()
def date_func():
    pass

def reset():
    evar1.set(' ')
    evar2.set(' ')
    evar3.set(' ')
    evar4.set(' ')
    evar5.set(' ')
    evar6.set(' ')
    evar7.set(' ')
    evar8.set(' ')
    evar9.set(' ')


def sub():
    name=evar1.get()
    F_name=evar2.get()
    M_name=evar3.get()
    dob=evar4.get()
    add=evar5.get()
    ph=evar6.get()
    cl_code=evar7.get()
    passs=evar8.get()
    passs2=evar9.get()
    if ph.isnumeric()==False:
        box.showerror("Error!","Age, Salary and Phone should be numeric!!")
        
    elif len(ph)!=10:
        box.showerror("Error!","Phone must be of 10 digits !!")
    elif len(passs)!=6:
        box.showerror("Error!","Password must contain 6 characters!!")
    elif passs!=passs2:
        box.showerror("Error!","Password is not matching!!")

    
    cur.execute('INSERT INTO student_info(Stu_name,Father_name,Mother_name,DOB,Address,Phone,Class_code,pass) VALUES(%s,%s,%s,%s,%s,%s,(Select class_code from class_subjects where class_name=%s),%s)',(name,F_name,M_name,dob,add,ph,cl_code,passs))
    conn.commit()
    box.showerror("Successful!","Successfully Inserted!!")
    win.destroy()
    
    
def title_page():
    global win
    win=tk.Tk()
    win.geometry('640x550+50+50')
    win.title('Student Registration')
    win.configure(background='orange')

    title=tk.Label(win,text='STUDENT REGISTRATION',pady=20,bg='orange',fg='green',font=['Arial',18,'bold','bold']).pack()

##    img=tk.PhotoImage(file='items.png')
##    a=tk.Label(win,image=img,pady=20).pack()
    name=tk.Label(win,text='Student Name : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=100)
    name2=tk.Label(win,text='Father Name  : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=140)
    name3=tk.Label(win,text='Mother Name : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=180)
    dob=tk.Label(win,text='DOB           : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=220)
    dd=tk.Button(win,text='',font=['Arial',10,'bold','bold'],bg='orange',command=date_func).place(x=500,y=215)
    sel=tk.Button(win,text='Select',font=['Arial',11,'bold','bold'],command=cal_func).place(x=550,y=220)
    add=tk.Label(win,text='Address    : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=260)
    phone=tk.Label(win,text='Phone     : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=300)
    classs=tk.Label(win,text='Class      : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=340)
    passs=tk.Label(win,text='Password   : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=380)
    passs2=tk.Label(win,text='Confirm Password   : ',pady=5,bg='orange',fg='blue',font=['Arial',14,'bold','bold']).place(x=50,y=420) 

    submit=tk.Button(win,text='SUBMIT',font=['Arial',12,'bold','bold'],command=sub,padx=5,pady=5).place(x=80,y=480)
    re=tk.Button(win,text='RESET',font=['Arial',12,'bold','bold'],command=reset,padx=5,pady=5).place(x=400,y=480)

    global evar1,evar2,evar3,evar4,evar5,evar6,evar7,evar8,evar9
    evar1=tk.StringVar()
    evar2=tk.StringVar()
    evar3=tk.StringVar()
    evar4=tk.StringVar()
    evar5=tk.StringVar()
    evar6=tk.StringVar()
    evar7=tk.StringVar()
    evar8=tk.StringVar()
    evar9=tk.StringVar()
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar1).place(x=300,y=100)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar2).place(x=300,y=140)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar3).place(x=300,y=180)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar4).place(x=300,y=220)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar5).place(x=300,y=260)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar6).place(x=300,y=300)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar7).place(x=300,y=340)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar8).place(x=300,y=380)
    e1=tk.Entry(win,fg='blue',font=['Arial',14,'bold','bold'],textvariable=evar9).place(x=300,y=420)
    
    
    
##    start=ttk.Button(win,text='START',command=startfun).pack()

    win.mainloop()

conn.close()


