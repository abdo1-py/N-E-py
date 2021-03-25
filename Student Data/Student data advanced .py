import mysql.connector
import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

class connectoerDB:
    def __init__(self,root):
        self.root = root#=f this code like f=Tk() as you wrote before look at the below at the code root=Tk() #
        
        titlespace= ""
        #that is a way to make a space #
        self.root.title(102*titlespace + "MySQL Connector")
        #like writting f.title == self.root.title that is a way is understand it #
        self.root.geometry('800x700+300+0')
        #Also the same like f.geometry == self.root.geometry and so on in the rest orders#
        self.root.resizable(width=False ,height= False )
        #To know the frame for each i coloured them to identifying#

        mainFrame=Frame (self.root,bd=10,width=760 ,height= 700,relief = RIDGE ,bg='purple')
        #to know RIDGE ,the RIDGE it is something to decorate the frame on the bounderies #
        mainFrame.grid()
        
        TitleFrame = Frame(mainFrame,bd=7,width=760 ,height= 100,relief = RIDGE,bg='black')
        TitleFrame.grid(row =0,column=0)
        TopFrame3= Frame(mainFrame,bd=5,width=760 ,height= 500,relief = RIDGE,bg='green')
        TopFrame3.grid(row =1,column=0)

        
        LeftFrame= Frame(TopFrame3,bd=5,width=760 ,padx=2,height= 400,relief = RIDGE,bg='red')
        LeftFrame.pack(side=LEFT)
        LeftFrame1= Frame(LeftFrame,bd=5,width=600 ,padx=12,pady=9,height= 180,relief = RIDGE,bg='blue')
        LeftFrame1.pack(side=TOP)

        RightFrame= Frame(TopFrame3,bd=5,width=100,padx=2,height= 400,relief = RIDGE,bg='Yellow')
        RightFrame.pack(side=RIGHT)
        RightFrame1= Frame(RightFrame,bd=5,width=90 ,padx=2,pady=2,height= 300,relief = RIDGE,bg='pink')
        RightFrame1.pack(side=TOP)
        #================================================================================#
        StudentID =IntVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address =StringVar()
        Gender =StringVar()
        Mobil =StringVar()

        #========================================================================================

        def IExit():
            IExit =tkinter.messagebox.askyesno("The programm ","Confirm if you want to exit")
            if IExit > 0:
                root.destroy()
                return
                
            

        def Reset():
            self.EnStudent.delete(0,END)
            self.EnFristname.delete(0,END)
            self.EnSurname.delete(0,END)
            self.EnAddress.delete(0,END)
            self.CboGender.set('')
            self.EnMobil.delete(0,END)

        def Adddata():
            try:
                
                con= mysql.connector.connect(
                    host =  " localhost ",
                    user ='TestDB',
                
                    passwd ='123456',
                    database= 'mybdpy'
                   
                    )
                    
                

            

                cur=con.cursor()
                #Donot name the table any name related with table like Student Table . it will not work at all #
               
            
                cur.execute(""" CREATE TABLE  Studentess ( STudentID  int primary key , Firstname varchar(99) ,Address varchar(180),Gender varchar(150),Surname varchar(180),Mobil int ) """ )
                con.commit()
            except mysql.connector.Error as e:
                print(e)
            if StudentID.get()=="" or Firstname.get()=="" or Surname.get()=="":
                tkinter.messagebox.showerror("The programm ","Enter Correct Details")
            else:
            
            
                conn=mysql.connector.connect(
                     host =  " localhost ",
                     user ='TestDB',
                
                     passwd ='123456',
                     database= 'mybdpy'
                   
                     )
                
                
                
                curr=conn.cursor()
                
               
                curr.execute( 'INSERT INTO Studentess VALUES(%d,"%s","%s" ,"%s","%s","%s")'%(
                    StudentID.get(),
                    Firstname.get(),
                    Surname.get(),
                    Address.get(),
                    Gender.get(),
                    Mobil.get()
                    ))
                
                    
                    
               
                conn.commit()
                
                
                tkinter.messagebox.showinfo("The programm ","Record Entered Successfully")




        def Displaydata():
            
            conn=mysql.connector.connect(
                     host =  " localhost ",
                     user ='TestDB',
                
                     passwd ='123456',
                     database= 'mybdpy'
                     )
            curr=conn.cursor()
            curr.execute("select * from  Studentess " )
            result=curr.fetchall()
            if len(result) !=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values=row)
                conn.commit()
            conn.close()
            #tkinter.messagebox.showinfo("The programm ","The Data Showed Successfully")

        #This def becouse if you select any one of them the rest of infornmation will mainfaste#

        def TraineInfo(ev):
            viewInfo = self.student_records.focus()
            LearnData=self.student_records.item(viewInfo)
            row=LearnData['values']
            StudentID.set(row[0]),
            Firstname.set(row[1]),
            Surname.set(row[2]),
            Address.set(row[3]),
            Gender.set(row[4]),
            Mobil.set(row[5])


        def update():
            conn=mysql.connector.connect(
                     host =  " localhost ",
                     user ='TestDB',
                
                     passwd ='123456',
                     database= 'mybdpy'
                     )
            curr=conn.cursor()
            curr.execute("UPDATE Studentess  SET Firstname = '" +Firstname.get()+"',Address='"+\
                       Address.get()+"',Gender ='"+Gender.get()+"',Surname ='"+Surname.get()+"',Mobil ='"+Mobil.get()+"' WHERE STudentID = "+str(StudentID.get()))
            #curr.execute("update Studentess set Firstname= '%s', Address ='%s' ,Gender ='%s',Surname ='%s',Mobil='%s' where STudentID= %d ",(
                 
                 
               

            conn.commit()
            tkinter.messagebox.showinfo("The programm ","Record Update Successfully")


        def delete():
            
            condel=mysql.connector.connect(
            host='localhost',
            user='TestDB',
            passwd='123456',
            database='mybdpy'
            )
            curdel=condel.cursor()
            curdel.execute('Delete from Studentess where STudentID ='+str(StudentID.get()))

            condel.commit()
            tkinter.messagebox.askyesno("The programm ","Confirm If You Want To Delete It")


        def search():
            try:
                conn=mysql.connector.connect(
                    host =  " localhost ",
                    user ='TestDB',
                        
                    passwd ='123456',
                    database= 'mybdpy'
                    )
                             
                curr=conn.cursor()
                curr.execute('Select * from  Studentess where STudentID = %d'%(StudentID.get())  )
                row=curr.fetchone()
                #Take care between Fechone and Fechall above#
                
                StudentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobil.set(row[5])

                conn.commit()
            except:
                tkinter.messagebox.askyesno("The programm ","No Such Info Like This Found ")
                
                
         
            
            
                
            
                


        
            
                        
                    
            

        
                

        
         
             
            
            

                    


    
            
            



        #=====================================================================================#
        self.lbltitle=Label(TitleFrame,font=('arail',40,'bold'),text='Mystudents Data ',bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)

        
        self.lblStudent=Label(LeftFrame1,font=('arail',12,'bold'),text='Student ID',bd=7)
        self.lblStudent.grid(row=0,column=0,padx=5,sticky=W)
        self.EnStudent=Entry(LeftFrame1,font=('arail',12,'bold'),width=44,bd=5,justify='left',textvariable=StudentID)
        self.EnStudent.grid(row=0,column=1,padx=5,sticky=W)
        # W must be capital #
        #Sticky code = What to do if the cell is larger than widget. By default, with sticky='',widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.#

        self.lblFristname=Label(LeftFrame1,font=('arail',12,'bold'),text='Firstname ',bd=7)
        self.lblFristname.grid(row=1,column=0,padx=5,sticky=W)
        self.EnFristname=Entry(LeftFrame1,font=('arail',12,'bold'),width=44,bd=5,justify='left',textvariable=Firstname)
        self.EnFristname.grid(row=1,column=1,padx=5,sticky=W)

        self.lblSurname=Label(LeftFrame1,font=('arail',12,'bold'),text='Surname ',bd=7)
        self.lblSurname.grid(row=2,column=0,padx=5,sticky=W)
        self.EnSurname=Entry(LeftFrame1,font=('arail',12,'bold'),width=44,bd=5,justify='left',textvariable=Surname)
        self.EnSurname.grid(row=2,column=1,padx=5,sticky=W)

        self.lblAddress=Label(LeftFrame1,font=('arail',12,'bold'),text='Address',bd=7)
        self.lblAddress.grid(row=3,column=0,padx=5,sticky=W)
        self.EnAddress=Entry(LeftFrame1,font=('arail',12,'bold'),width=44,bd=5,justify='left',textvariable=Address)
        self.EnAddress.grid(row=3,column=1,padx=5,sticky=W)


        self.lblGender=Label(LeftFrame1,font=('arail',12,'bold'),text='Gender',bd=7)
        self.lblGender.grid(row=4,column=0,padx=5,sticky=W)
        self.CboGender=ttk.Combobox(LeftFrame1,font=('arail',12,'bold'),width=42,state ='readonly',textvariable=Gender)
        self.CboGender['values']=('','Female','Male')
        self.CboGender.current(0)
        self.CboGender.grid(row=4,column=1,padx=5)


        self.lblMobil=Label(LeftFrame1,font=('arail',12,'bold'),text='Mobil',bd=7)
        self.lblMobil.grid(row=5,column=0,padx=5,sticky=W)
        self.EnMobil=Entry(LeftFrame1,font=('arail',12,'bold'),width=44,bd=5,justify='left',textvariable=Mobil)
        self.EnMobil.grid(row=5,column=1,padx=5,sticky=W)
        #=============================================================================================#
        #To understand the code follow this #
        #First we have the code is called Scrollbar#
        #The secound code is Treeview for your labels#
        #The third is heading to put them as you see in the pro  #
        #The fourth is to put the in a column#
        Scroll_y =Scrollbar(LeftFrame,orient=VERTICAL)
        self.student_records=ttk.Treeview(LeftFrame,height=12,columns=('stadid','Firstname','Surname','Address','Gender','Mobil'),yscrollcommand=Scroll_y.set)
        Scroll_y.pack(side=RIGHT,fill=Y)

        self.student_records.heading('stadid',text='Student ID')
        self.student_records.heading('Firstname',text='Firstname')
        self.student_records.heading('Surname',text='Surname')
        self.student_records.heading('Address',text='Address')
        self.student_records.heading('Gender',text='Gender')
        self.student_records.heading('Mobil',text='Mobil')

        self.student_records['show']='headings'


        self.student_records.column('stadid',width=70)
        self.student_records.column('Firstname',width=100)
        self.student_records.column('Surname',width=100)
        self.student_records.column('Address',width=100)
        self.student_records.column('Gender',width=70)
        self.student_records.column('Mobil',width=100)


        self.student_records.pack(fill=BOTH,expand=1)
        self.student_records.bind("<ButtonRelease-1>",TraineInfo)
        #The Data will appear automatically#
        Displaydata()
        
        

        #=========================================================================================#

        self.btnAddNew=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Add New",pady=1,padx=24,command=Adddata ).grid(row=0,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Display",command =Displaydata,pady=1,padx=24).grid(row=1,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Update",pady=1,padx=24,command=update).grid(row=2,column=0,padx=1)
        self.btnDelete=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Delete",pady=1,padx=24,command=delete).grid(row=3,column=0,padx=1)
        self.btnSearch=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Search",pady=1,padx=24,command=search).grid(row=4,column=0,padx=1)
        self.btnReset=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Reset",pady=1,padx=24,command=Reset).grid(row=5,column=0,padx=1)
        self.btnExit=Button(RightFrame1,font=('arail',16,'bold'),width=8,height=2,bd=4,text="Exit",pady=1,padx=24,command=IExit).grid(row=6,column=0,padx=1)



        
        
        
        
        

        

        

        




        

if __name__ =='__main__':
    
    root=Tk()
    #f=Tk()#
    application=connectoerDB(root)
    #That is calling for the function#
    root.mainloop()
