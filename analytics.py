import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib as mp
from matplotlib import pyplot as plt
import numpy as np
import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='12345')
cur=conn.cursor()
def anas():
    query1='USE school_management'
    cur.execute(query1)
    stu='sub1','sub2','sub3','sub4','sub5','sub6','lab1','lab2'
    import mainpage
    t=mainpage.link1()
    cur.execute('Select Enroll_no from student_info Where Stu_name=%s',(t,))
    t=cur.fetchone()
    for x in t:
        p=x

    query=('Select sub1_attendance,sub2_attendance,sub3_attendance,sub4_attendance,sub5_attendance,sub5_attendance,lab1_attendance,lab2_attendance FROM attendance_table WHERE Enroll_no=%s')
    cur.execute(query,(p,))
    rows=cur.fetchall()
    for i in rows:
        roll=i
    print(roll)

    plt.bar(stu,roll,width=0.8,color=('m','b','r','g','m','r','g','b'))
    plt.xlabel("Players")
    plt.ylabel("Goal Scored")
    plt.title('Attendance graph')
    plt.show()


