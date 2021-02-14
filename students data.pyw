from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector


f=Tk()
f.geometry('1300x1000')
bg="blue"
fo=('Arail ','25')

fg=('white')
f.title('My Data')
f.config(bg='purple')
fra=Frame(f).grid(row=0,column=0)
Label(fra,text='Student data',font=(fo),bg=bg,fg=fg).grid(row=0,column=1)



Label(fra,text='Enter Student ID:',font=('arail','20'),fg='red').grid(row=1,column=1,pady=20)
Entry(fra,bd=5,width=50).grid(row=1,column=2)

Label(fra,text='Enter Student Name:',font=('arail','20'),fg='red').grid(row=2,column=1,pady=20)
Entry(fra,bd=5,width=50).grid(row=2,column=2)


Label(fra,text='Enter Student Address:',font=('arail','20'),fg='red').grid(row=3,column=1,pady=20)
Entry(fra,bd=5,width=50).grid(row=3,column=2)

Button(fra,text='Insert:',font=('arail','20'),fg='red').grid(row=5,column=1)

Button(fra,text='Update:',font=('arail','20'),fg='red').grid(row=5,column=2)

Button(fra,text='Select:',font=('arail','20'),fg='red').grid(row=6,column=1)

Button(fra,text='Delete:',font=('arail','20'),fg='red').grid(row=6,column=2,pady=20)



f.mainloop()


















input('press enter to exit....')
