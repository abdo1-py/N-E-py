from tkinter import *
import tkinter
from tkinter import messagebox
#import pymysql


f=Tk()
f.geometry('1300x1000')
bg="blue"
fo=('Arail ','25')

fg=('white')
f.title('My Data')
f.config(bg='purple')
fra=Frame(f).grid(row=0,column=0)
Label(fra,text='Stuedent data',font=(fo),bg=bg,fg=fg).grid(row=0,column=1)



Label(fra,text='Enter Stuedent ID:',font=('arail','20'),fg='red').grid(row=1,column=1,pady=20)
Entry(fra,bd=5,width=50).grid(row=1,column=2)











f.mainloop()


















input('press enter to exit....')
