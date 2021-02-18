from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import mysql.connector



f=tkinter.Tk()
f.geometry('1300x1000')
bg="blue"
fo=('Arail ','25')

fg=('white')
f.title('My Data')
f.config(bg='purple')
fra=Frame(f).grid(row=0,column=0)
Label(fra,text='Student data',font=(fo),bg=bg,fg=fg).grid(row=0,column=1)

svid=IntVar()
svna=StringVar()
svadd=StringVar()
svcon=StringVar()

L1=Label(fra,text='Enter Student ID:',font=('arail','20'),fg='red')
L1.grid(row=1,column=1,pady=20)
E1=Entry(fra,bd=5,width=50,textvariable=svid)
E1.grid(row=1,column=2)
         

Label(fra,text='Enter Student Name:',font=('arail','20'),fg='red').grid(row=2,column=1,pady=20)
Ena=Entry(fra,bd=5,width=50,textvariable=svna)
Ena.grid(row=2,column=2)


Label(fra,text='Enter Student Address:',font=('arail','20'),fg='red').grid(row=3,column=1,pady=20)
Ead=Entry(fra,bd=5,width=50,textvariable=svadd)
Ead.grid(row=3,column=2)

Label(fra,text='Enter Student Condition :',font=('arail','20'),fg='red').grid(row=4,column=1,pady=20)
Eco=Entry(fra,bd=5,width=50,textvariable=svcon)
Eco.grid(row=4,column=2)


def mybuton(selection):
    print("Student id is :", E1.get())
    print("Student name is :" ,Ena.get())
    print("Student address is :", Ead.get())
    print("Student Condition is :", Eco.get())
    try:
        con=mysql.connector.connect(
            host='localhost',
            user='Student Data',
            passwd='123456',
            database='  Student Data'
            )
                
                
        cur=con.cursor()
        #cur.execute('select version()')
        #data=cur.fetchone()
        #print('Mysql Database version ',data)
        query= (""" CREATE TABLE  Student_Data ( Student_id  int primary key , Student_name   varchar(99) ,\
                                  Student_address    varchar(180),Student_Condition varchar(150) ) """ )
        cur.execute(query)
        con.commit()
        con.close()
        con.rollback()
          
    except mysql.connector.Error as e:
        print(e)
        
            
            
                   
            
    try:
           
        conn=mysql.connector.connect(
            host='localhost',
            user='Student Data',
            passwd="123456",
            database='Student Data'
            )
                
        curr=conn.cursor()
        curr.execute(""" insert into   Student_Data values (%d,"%s","%s","%s") """ % (svid.get(),svna.get(),svadd.get(),svcon.get()) )
        conn.commit()
        conn.close()         
               

    except mysql.connector.Error as d:
        print(d)
            
                    
        
            
             
def update():
    
    
    try:
        
            
        conup=mysql.connector.connect(
                host='localhost',
                user='Student Data',
                passwd="123456",
                database='Student Data'
                )

        curup=conup.cursor()
        curup.execute("UPDATE Student_Data  SET Student_name = '" +svna.get()+"',Student_address='"+\
                      svadd.get()+"',Student_Condition ='"+svcon.get()+"' WHERE Student_id = "+str(svid.get()))
        # it did not work curup.execute("update Student_Data set Student_name = \
        #'" +svna.get() + '",Student_address = "' + svadd.get()+ "' where Student_id = " + str(svid.get()))
        conup.commit()
        conup.close()
        conup.rollback()
        
    except mysql.connector.Error as up:
        print(up)
    print("The update is succefully worked")
           
def delete():
    try:
        condel=mysql.connector.connect(
            host='localhost',
            user='Student Data',
            passwd='123456',
            database='Student Data'
            )
        curdel=condel.cursor()
        curdel.execute('Delete from Student_Data where Student_id ='+str(svid.get()))

        condel.commit()

    except mysql.connector.Error as De:
        print(De)
    print("The delete is succefully worked")

        
def select():
    try:
        conse=mysql.connector.connect(
            host='localhost',
            user='Student Data',
            passwd='123456',
            database='Student Data'
            )
        curse=conse.cursor()
        curse.execute("SELECT * FROM Student_Data WHERE Student_id ='%s'"%(svid.get()))
        for row in curse:
            svid.set(row[0])
            svna.set(row[1])
            svadd.set(row[2])
            svcon.set(row[3])
         
        conse.commit()
        conse.close()
        print("The selection  is succefully worked")
    except mysql.connector.Error as s:
        print(s)
        conse.close()
    
            
            
                
                
            
          
        

    
    
                
        
    
Button(fra,text='Insert:',font=('arail','20'),fg='red',command= lambda :mybuton('Insert')).grid(row=5,column=1)

Button(fra,text='Update:',font=('arail','20'),fg='red',command= update).grid(row=5,column=2)

Button(fra,text='Delete:',font=('arail','20'),fg='red',command= delete).grid(row=6,column=2,pady=20)

Button(fra,text='Exit:',font=('arail','20'),fg='red',command=f.destroy).grid(row=7,column=2,pady=20)

Button(fra,text='Select:',font=('arail','20'),fg='red',command=select).grid(row=6,column=1)








f.mainloop()


















input('press enter to exit....')
