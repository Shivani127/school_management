import tkinter as tk
from tkinter import ttk
import mainpage
import time

def startfun():
    win.destroy()
    mainpage.m()
    

def title_page():
    global win
    win=tk.Tk()
    win.geometry('1280x750+0+0')
    win.title('TitlePage')
    win.configure(background='lightgreen')

    title=tk.Label(win,text='STUDENTS ATTENDANCE SYSTEM',pady=50,bg='lightgreen',fg='red',font=['Arial',28,'bold','bold']).pack()

    img=tk.PhotoImage(file='stu5.png')
    a=tk.Label(win,image=img,pady=20).pack()
    title=tk.Label(win,text=' ',pady=5,bg='lightgreen',fg='red',font=['Arial',28,'bold','bold']).pack()
    
    start=ttk.Button(win,text='START',command=startfun).pack()

    win.mainloop()
title_page() 


