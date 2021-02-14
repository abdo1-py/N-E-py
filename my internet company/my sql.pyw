import mysql.connector
from tkinter import ttk
from tkinter import *
from sqtools import *

               
        
f=Tk()


f.geometry('800x600')




def emp_clear():
    empid_V.set(dbautonum('go_employee1','employee_id'))
    empn_V.set("")
    empaddress_V.set("")
    
   
def creat_table():
    
    
    try:
        
        
        
        con= mysql.connector.connect(
                host =  " localhost ",
                user ='TestDB',
                
                passwd ='123456',
                database= 'mybdpy'
                
                )

            

        cur=con.cursor()
            
        cur.execute(""" CREATE TABLE  GO_EMPLOYEE1 ( employee_id  int primary key , empolyee_name   varchar(99) ,address    varchar(180) ) """ )
    except mysql.connector.Error as e:
        print(e)
       



    



def emp_add():
    

    try:
        
        
        
        
        conadd= mysql.connector.connect(
                host =  " localhost ",
                user ='TestDB',
                
                passwd ='123456',
                database= 'mybdpy'
                
                )

            

        curadd=conadd.cursor()
        
            
        curadd.execute(""" insert into go_employee1 values  (%d,"%s","%s") """ % (empid_V.get(),empn_V.get(),empaddress_V.get()) )
        conadd.commit()
    except mysql.connector.Error as e1:
        
        print(e1)




def emp_find():
    ff=Tk()
    ok1=ttk.Label(ff,text="Employee ID:")
    ok1.pack()
    empiok_V= IntVar()
    OK=ttk.Entry(ff,textvariable=empiok_V)
    OK.pack()
    ff.geometry('200x75')
    
    
    
    
    def ok():
        
        
        try:
            
            
    
            
            
            con= mysql.connector.connect(
            host =  " localhost ",
            user ='TestDB',
                
            passwd ='123456',
            database= 'mybdpy'
            
                
            )
            

            cur=con.cursor()
           
           
            cur.execute(" SELECT * FROM GO_EMPLOYEE1 where employee_id like'%"+OK.get()+"%' " )
                                    
            for row in cur:
                
                
                print(row)
            empid_V.set(row[0])
            empn_V.set(row[1])
            empaddress_V.set(row[2])
            
            
            
                        
                
               
                        
                   
            
        
            
            
        except mysql.connector.Error as k:
            
            print(k)
        

        
            
            
        
        
        

        
        
        



        
    Button(ff,text='OK',command=ok).pack()
    ff.mainloop()
    

def emp_edit():
    #dbrun("updata go_employee1 set employee_name='" +empn_V.get()+"',address='"+empaddress_V.get()+"' where employee_id=" +str(empid_V.get()))
    #dbrun("UPDATE go_employee1 SET empolyee_name = '" +empn_V.get()+"',address='"+empaddress_V.get()+", WHERE employee_id = "+str(empid_V.get()))
    try:
        
        
    
            
           
        con= mysql.connector.connect(
        host =  " localhost ",
        user ='TestDB',
                
        passwd ='123456',
        database= 'mybdpy'
            
                
        )
            

        cur=con.cursor()
           
           
        cur.execute("UPDATE go_employee1 SET empolyee_name = '" +empn_V.get()+"',address='"+empaddress_V.get()+"' WHERE employee_id = "+str(empid_V.get()))
                         
                          
        con.commit()
        
            
              
    except mysql.connector.Error as k:
                    
                    
                    print(k)
    



def emp_del():
    
    try:
        
    
        
        
    
            
           
        con= mysql.connector.connect(
        host =  " localhost ",
        user ='TestDB',
                
        passwd ='123456',
        database= 'mybdpy'
            
                
        )
            

        cur=con.cursor()
           
           
        cur.execute("delete from go_employee1 where employee_id= " +str(empid_V.get()))
                         
                          
        con.commit()
        
            
              
    except mysql.connector.Error as k:
                    
                    
                    print(k)
    
    
    









empid_V= IntVar()
empn_V= StringVar()
empaddress_V= StringVar()


Label(f,text='Employee ID:').pack()
EI=Entry(f,textvariable=empid_V)
EI.pack()


Label(f,text='Employee Name:').pack()
EN=Entry(f,textvariable=empn_V)
EN.pack()

Label(f,text='Employee address').pack()
EA=Entry(f,textvariable=empaddress_V)
EA.pack()


Button(f,text='Creat Table',font=('25,Arail'),fg='red',command=creat_table,width=20).pack(pady = 5)

Button(f,text="Add Emplotee" ,command=emp_add,width=20).pack(pady = 5)

Button(f,text='Find Employee',command=emp_find,width=20).pack(pady = 5)

Button(f,text="Edit Empolyee",command=emp_edit,width=20).pack(pady = 5)

Button(f,text="Delete Empolyee",command=emp_del,width=20).pack(pady = 5)

Button(f,text="Clear Empolyee",command=emp_clear,width=20).pack(pady = 5)



Button(f,text="EXIT",command=f.destroy,width=20).pack(pady = 10)



f.mainloop()

    
    
    
          
        
                    
                
            
                    
        
     
            



    


