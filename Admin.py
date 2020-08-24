import tkinter as tk
from tkinter import ttk
import mysql.connector
##import attendance
##import teachers_information
##import student_information
import mainpage
##import analytics

#import cv2

conn=mysql.connector.connect(host='localhost',username='root',password='12345')
cur=conn.cursor()

query1='USE school_management'
cur.execute(query1)

query2='SELECT Class_name,Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Lab1,Lab2 FROM class_subjects'
cur.execute(query2)
rows=cur.fetchall()

def atten():
    win2.destroy()
    attendance.cs()

def teachers():
    win2.destroy()
    teachers_information.teach()

def students():
    win2.destroy()
    student_information.stu()
    

def home():
    win2.destroy()
    mainpage.m()

def analy():
    analytics.anas()
    

    

def add():
    c_name=evar1.get()
    sub1=evar2.get()
    #print(sub1,c_name)
    sub2=evar3.get()
    sub3=evar4.get()
    sub4=evar5.get()
    sub5=evar6.get()
    sub6=evar7.get()
    lab1=evar8.get()
    lab2=evar9.get()
    cur.execute('INSERT INTO class_subjects(Class_name,Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Lab1,Lab2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(c_name,sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2))
    conn.commit()
    query5='SELECT Class_name,Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Lab1,Lab2 FROM class_subjects'
    cur.execute(query5)
    row=cur.fetchall()
    for i in v.get_children():
        v.delete(i)
                
    for i in row:
        v.insert('','end',values=i)


def mod():
    c_name=evar1.get()
    sub1=evar2.get()
    print(sub1,c_name)
    sub2=evar3.get()
    sub3=evar4.get()
    sub4=evar5.get()
    sub5=evar6.get()
    sub6=evar7.get()
    lab1=evar8.get()
    lab2=evar9.get()
    cur.execute('UPDATE class_subjects SET Sub1=%s,Sub2=%s,Sub3=%s,Sub4=%s,Sub5=%s,Sub6=%s,Lab1=%s,Lab2=%s WHERE Class_name=%s',(sub1,sub2,sub3,sub4,sub5,sub6,lab1,lab2,c_name))
    conn.commit()
    query5='SELECT Class_name,Sub1,Sub2,Sub3,Sub4,Sub5,Sub6,Lab1,Lab2 FROM class_subjects'
    cur.execute(query5)
    row=cur.fetchall()
    for i in v.get_children():
        v.delete(i)
                
    for i in row:
        v.insert('','end',values=i)



    
    
def ad_panel():
    global win2
    win2=tk.Tk()
    win2.geometry('1270x1000+0+0')
    win2.configure(bg='lightgreen')
    win2.title('Admin Panel')

    main_menu=tk.Menu(win2)

    BACK=tk.Menu(main_menu,tearoff=0)
    BACK.add_command(label='login Page',command=home)
    main_menu.add_cascade(label='BACK',menu=BACK)

##    WATCH=tk.Menu(main_menu,tearoff=0)
##    WATCH.add_command(label='Attendance Info.',command=atten)
##    WATCH.add_command(label='Teachers Info.',command=teachers)
##    WATCH.add_command(label='Students Info.',command=students)
##    main_menu.add_cascade(label='WATCH',menu=WATCH)

    analysis=tk.Menu(main_menu,tearoff=0)
    analysis.add_command(label='Attendance',command=analy)
    main_menu.add_cascade(label='Analysis',menu=analysis)

    

    
    

    img=tk.PhotoImage(file='stu3.png')
    
##    label=tk.Label(win2,text=' ',pady=5,bg='lightgreen').place(x=20,y=20)

    label=tk.Label(win2,image=img,pady=50).place(x=20,y=100)

    
    label=tk.Label(win2,text='Class Information => ',pady=10,font=['Arial',26,'bold','bold'],bg='lightgreen',fg='purple').place(x=480,y=20)

    global v
    v=ttk.Treeview(win2,columns=(1,2,3,4,5,6,7,8,9),show='headings',height=10)
    v.place(x=2,y=580)
    v.column(1,width=50)
    v.heading(1,text='Class')
    v.column(2,width=150)
    v.heading(2,text='Subject 1')
    v.column(3,width=150)
    v.heading(3,text='Subject 2')
    v.column(4,width=150)
    v.heading(4,text='Subject3')
    v.column(5,width=150)
    v.heading(5,text='Subject4')
    v.column(6,width=150)
    v.heading(6,text='Subject5')
    v.column(7,width=180)
    v.heading(7,text='Subject6')
    v.column(8,width=150)
    v.heading(8,text='Lab1')
    v.column(9,width=150)
    v.heading(9,text='Lab2')
    for i in rows:
        v.insert('','end',values=i)

    frame1=tk.LabelFrame(win2,text='Add Class',bg='pink',fg='purple',height=400,width=650,font=['Arial',16,'bold','bold']).place(x=600,y=80)
    l1=tk.Label(frame1,text='Class Name:',font=['Arial',14,'bold','bold'],bg='pink',fg='green').place(x=680,y=120)
    l2=tk.Label(frame1,text='Subject 1:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=160)
    l3=tk.Label(frame1,text='Subject 2:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=200)
    l4=tk.Label(frame1,text='Subject 3:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=240)
    l5=tk.Label(frame1,text='Subject 4:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=280)
    l6=tk.Label(frame1,text='Subject 5:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=320)
    l7=tk.Label(frame1,text='Subject 6:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=360)
    l8=tk.Label(frame1,text='Lab 1:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=400)
    l9=tk.Label(frame1,text='Lab 2:',font=['Arial',12,'bold','bold'],bg='pink',fg='green').place(x=630,y=440)


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
    
    e1=tk.Entry(frame1,fg='Green',font=['Arial',14,'italic','italic'],textvariable=evar1).place(x=850,y=120)
    e2=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar2).place(x=830,y=160)
    e3=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar3).place(x=830,y=200)
    e4=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar4).place(x=830,y=240)
    e5=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar5).place(x=830,y=280)
    e6=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar6).place(x=830,y=320)
    e7=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar7).place(x=830,y=360)
    e8=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar8).place(x=830,y=400)
    e9=tk.Entry(frame1,fg='Green',font=['Arial',12,'italic','italic'],textvariable=evar9).place(x=830,y=440)

    add_btn=tk.Button(win2,text='ADD NEW CLASS',bg='lightgrey',padx=35,pady=5,fg='blue',bd=5,font=['Arial',10,'bold','bold']).place(x=600,y=500)
    modify=tk.Button(win2,text='MODIFY EXISTING CLASS',bg='lightgrey',padx=10,pady=5,fg='blue',bd=5,font=['Arial',10,'bold','bold']).place(x=850,y=500)
   # delete=tk.Button(win2,text='DELETE',bg='lightgrey',command=add,padx=10,pady=5,fg='blue',bd=5,font=['Arial',10,'bold','bold']).place(x=1080,y=600)
    
    
    win2.configure(menu=main_menu)
    win2.resizable(False,False)
    win2.mainloop()
   
conn.close()

    

    

    

    
    
