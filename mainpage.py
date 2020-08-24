import tkinter as tk
from tkinter import ttk
##import AdminLogin
import Admin
##import Users
#import StaffPanel
##import student_portal
import mysql.connector
from tkinter import messagebox as box
import stu_registration
import staff_reg


conn=mysql.connector.connect(host='localhost',username='root',password='12345')
cur=conn.cursor()
query1='USE school_management'
cur.execute(query1)

def signin():
    name=entry_name.get()
    password=entry_pass.get()
    if name=='Shivani' and password=='12345':
        win.destroy()
        import Admin
        Admin.ad_panel()
        
    else:
        box.showerror("Error!","Invalid admin name or password!!")
        
        
##       page()
def registration1():
    
    stu_registration.title_page()

def registration2():
    
    staff_reg.title_page()

def reset():
    entry_name.set(' ')
    entry_pass.set(' ')

def reset1():
    entry_name2.set(' ')
    entry_pass2.set(' ')

def reset3():
    entry_name3.set(' ')
    entry_pass3.set(' ')
def link3():
    return Name
def link4():
    return passs
def signin2():
    global Name
    Name=entry_name2.get()
    global passs
    passs=entry_pass2.get()
    query2='SELECT name,pass FROM teachers_info'
    cur.execute(query2)
    flag=0
    for (name,pas) in cur:
##        if entry_name2.get()==" " or entry_pass2.get()==" ":
##            box.showerror("Error!","All Fields are required!!")
        if Name==name and passs==pas:
            flag=1
            win.destroy()
            import StaffPanel
            SaffPanel.staff()
            
        
    if flag==0:
        box.showerror("Error!","Invalid staff name or password!!")

def link1():
    print(stu_Name)

def signin3():
    
    global stu_Name
    stu_Name=entry_name3.get()
    password=entry_pass3.get()
    query2='SELECT Stu_name,pass FROM student_info'
    cur.execute(query2)
    flag=0
     
    for (name,pas) in cur:
##        if entry_name2.get()==" " or entry_pass2.get()==" ":
##            box.showerror("Error!","All Fields are required!!")
        
        if stu_Name==name and password==pas:
            flag=1
            win.destroy()
            import student_portal
            student_portal.stu_portal()
        
    if flag==0:
        box.showerror("Error!","Invalid student name or password!!")

    
            
            

def us_login():
    global win1
    win1=tk.Tk()
    win1.title('User Login')
    win1.geometry('250x100+50+50')
    win1.configure(bg='lightgreen')

    

    global img1
    img=tk.PhotoImage(file='stu.png')
    img2=tk.PhotoImage(file='pass.png')
    img3=tk.PhotoImage(file='ghgh.png')

    #img=tk.Label(win1,image=img2,compound='left',font=['Arial',11,'bold','bold']).grid(row=1,column=0,rowspan=2,padx=12,pady=10)
    
    
    adminlbl=tk.Label(win1,text='Admin Name :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightgreen',pady=10,padx=10).grid(row=1,column=1)
    entry_name=tk.StringVar()
    adminentry=tk.Entry(win1,fg='green',bd=2,textvariable=entry_name).grid(row=1,column=3)

    passlbl=tk.Label(win1,text='Password     :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightgreen',pady=10,padx=10).grid(row=2,column=1)
    entry_pass=tk.StringVar()
    passentry=tk.Entry(win1,fg='green',bd=2,textvariable=entry_pass).grid(row=2,column=3)
    
    log=tk.Button(win1,text='LOGIN',bg='lightgrey',font=['Arial',10,'bold','bold'],command=signin).grid(row=3,column=1)
    log=tk.Button(win1,text='RESET',bg='lightgrey',font=['Arial',10,'bold','bold'],command=reset).grid(row=3,column=3)
    win1.mainloop()


def m():
    global win
    win=tk.Tk()
    win.title('Login Page')
    win.geometry('1350x1000+0+0')
    img=tk.PhotoImage(file='stu4.png')
    win.configure(background='pink')

    #FRAME 1

    frame1=tk.LabelFrame(win,text='ADMIN LOGIN:',height=200,width=400,font=['Arial',11,'bold','bold'],bg='lightblue',fg='black').place(x=20,y=20)
    adminlbl=tk.Label(frame1,text='Admin Name :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=50)
    global entry_name
    entry_name=tk.StringVar()
    adminentry=tk.Entry(frame1,fg='green',bd=2,textvariable=entry_name).place(x=200,y=60)

    passlbl=tk.Label(frame1,text='Password     :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=100)
    global entry_pass
    entry_pass=tk.StringVar()
    passentry=tk.Entry(frame1,fg='green',bd=2,textvariable=entry_pass).place(x=200,y=110)
    
    log1=tk.Button(frame1,text='LOGIN',bg='lightgrey',font=['Arial',10,'bold','bold'],command=signin).place(x=80,y=150)
    log2=tk.Button(frame1,text='RESET',bg='lightgrey',font=['Arial',10,'bold','bold'],command=reset).place(x=200,y=150)

    #FRAME 2
    frame2=tk.LabelFrame(win,text='STAFF LOGIN:',height=200,width=400,font=['Arial',11,'bold','bold'],bg='lightblue',fg='black').place(x=20,y=240)
    adminlbl2=tk.Label(frame2,text='Staff Name :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=270)
    global entry_name2
    entry_name2=tk.StringVar()
    adminentry=tk.Entry(frame2,fg='green',bd=2,textvariable=entry_name2).place(x=200,y=280)
    global entry_pass2
    passlbl2=tk.Label(frame2,text='Password     :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=320)
    entry_pass2=tk.StringVar()
    passentry=tk.Entry(frame2,fg='green',bd=2,textvariable=entry_pass2).place(x=200,y=330)
    
    l1=tk.Button(frame2,text='LOGIN',bg='lightgrey',font=['Arial',10,'bold','bold'],command=signin2).place(x=80,y=370)
    l=tk.Button(frame2,text='RESET',bg='lightgrey',font=['Arial',10,'bold','bold'],command=reset1).place(x=200,y=370)
####
    #FRAME 3
    frame3=tk.LabelFrame(win,text='STUDENT  LOGIN:',height=200,width=400,font=['Arial',11,'bold','bold'],bg='lightblue',fg='black').place(x=20,y=460)
    adminlbl3=tk.Label(frame3,text='Student Name :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=510)
    global entry_name3
    entry_name3=tk.StringVar()
    adminentry=tk.Entry(frame3,fg='green',bd=2,textvariable=entry_name3).place(x=200,y=520)
    
    global entry_pass3
    passlbl3=tk.Label(frame3,text='Password     :',font=['Arial',11,'bold','bold'],fg='blue',bg='lightblue',pady=10,padx=10).place(x=50,y=560)
    entry_pass3=tk.StringVar()
    passentry=tk.Entry(frame3,fg='green',bd=2,textvariable=entry_pass3).place(x=200,y=570)
    
    m=tk.Button(frame3,text='LOGIN',bg='lightgrey',font=['Arial',10,'bold','bold'],command=signin3).place(x=80,y=620)
    m1=tk.Button(frame3,text='RESET',bg='lightgrey',font=['Arial',10,'bold','bold'],command=reset3).place(x=200,y=620)
####    
##
    reg1=tk.Button(win,text='New Student',bg='lightgrey',font=['Arial',11,'bold','bold'],pady=5,padx=5,command=registration1).place(x=70,y=680)
    reg2=tk.Button(win,text='New Staff',bg='lightgrey',font=['Arial',11,'bold','bold'],pady=5,padx=5,command=registration2).place(x=230,y=680)
    i=tk.Label(win,image=img).place(x=540,y=70)

    n=tk.Label(win,text='"Attend Today, and Achieve Tomorrow"',bg='lightblue',fg='green',font=['Arial',32,'bold','bold']).place(x=440,y=580)
##########################################################################################################

    
    win.mainloop()



