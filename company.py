from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Toplevel
import tkinter as tk
f=Tk()


fo = ('Arial 25  ')
bg=('lightblue')
fg=('red')
f.geometry('600x400')
f.title(' My Company')
f.configure(bg='lightblue')
fra = Frame(f,bg=bg)
fra.pack(pady=10)


def Emp():
    fe=Tk()
    
    fe.geometry('600x400')
    frae=Frame(fe)
    frae.pack(pady=10)
    
    Label(frae,text='Number:',font=fo,fg=fg).grid(row=0,column=0)
    Label(frae,text='Name:',font=fo,fg=fg).grid(row=1,column=0)
    Label(frae,text='City:',font=fo,fg=fg).grid(row=2,column=0)
    Label(frae,text='Phone:',font=fo,fg=fg).grid(row=3,column=0)
    Label(frae,text='Email:',font=fo,fg=fg).grid(row=4,column=0)
    svno=IntVar()
    svna=StringVar()
    svci=StringVar()
    svph=IntVar()
    svem=StringVar()
    def number(text):
        if str.isdigit(text):
            
            return True
        
        elif text is '':
            
            return True
        else :
            
            
            return False
        
        
    
    rug = frae.register(number)
       
        

    
    
    E1=ttk.Entry(frae,font='Arail 15',textvariable=svno,validate='key' , validatecommand=(rug,'%P'))
    E1.grid(row=0,column=1)
    E2=ttk.Entry(frae,font='Arail 15',textvariable=svna)
    E2.grid(row=1,column=1)
    E3=ttk.Entry(frae,font='Arail 15',textvariable=svci)
    E3.grid(row=2,column=1)
    E4=ttk.Entry(frae,font='Arail 15',textvariable=svph)
    E4.grid(row=3,column=1)
    E5=ttk.Entry(frae,font='Arail 15',textvariable=svem)
    E5.grid(row=4,column=1)
    def showdata():
        messagebox.showinfo('Data',{ svno.get() , svna.get(), svci.get(), svph.get(), svem.get()})
       
    
    frae2=Frame(fe)
    frae2.pack(pady=10)
    Button(frae2,text='Add: ',bg=bg,font=(fo),fg=fg,command = showdata).grid(row = 5,column=0)
    Button(frae2,text='Edit: ',bg=bg,font=(fo),fg=fg,command = showdata).grid(row = 5,column=1)
    Button(frae2,text='Delete: ',bg=bg,font=(fo),fg=fg,command = showdata).grid(row = 5,column=2)
    Button(frae2,text='Find: ',bg=bg,font=(fo),fg=fg,command = showdata).grid(row = 7,column=2,padx=10,pady=10)
    Button(frae2,text='Close: ',bg=bg,font=(fo),fg=fg,command=fe.destroy).grid(row = 7,column=1,padx=10,pady=10)
    
    

    fe.grab_set()
    return fe



def Dep():
    fd=Tk()
    
    fd.geometry('600x400')
    frad=Frame(fd)
    frad.pack(pady=10)
    
    Label(frad,text='Department Number:',font=fo,fg=fg).grid(row=0,column=0)
    Label(frad,text='Department Name:',font=fo,fg=fg).grid(row=1,column=0)
    Label(frad,text='Department location',font=fo,fg=fg).grid(row=2,column=0)
    
    svnod=IntVar()
    svnad=StringVar()
    svlod=StringVar()
    def number(text):
        if str.isdigit(text):
            
            return True
        
        elif text is '':
            
            return True
        else :
            
            
            return False
        
        
    
    rug = frad.register(number)
       
 
    
    E1=ttk.Entry(frad,font='Arail 15',textvariable=svnod,validate='key' , validatecommand=(rug,'%P'))
    E1.grid(row=0,column=1)
    E2=ttk.Entry(frad,font='Arail 15',textvariable=svnad)
    E2.grid(row=1,column=1)
    E3=ttk.Entry(frad,font='Arail 15',textvariable=svlod)
    E3.grid(row=2,column=1)
    
    def showdatad():
        messagebox.showinfo('Data',{ svnod.get() , svnad.get(), svlod.get()})
       
    
    frad2=Frame(fd)
    frad2.pack(pady=10)
    Button(frad2,text='Add: ',bg=bg,font=(fo),fg=fg,command = showdatad).grid(row = 5,column=0)
    Button(frad2,text='Edit: ',bg=bg,font=(fo),fg=fg,command = showdatad).grid(row = 5,column=1)
    Button(frad2,text='Delete: ',bg=bg,font=(fo),fg=fg,command = showdatad).grid(row = 5,column=2)
    Button(frad2,text='Find: ',bg=bg,font=(fo),fg=fg,command = showdatad).grid(row = 7,column=2,padx=10,pady=10)
    Button(frad2,text='Close: ',bg=bg,font=(fo),fg=fg,command=fd.destroy).grid(row = 7,column=1,padx=10,pady=10)
    
    

    fd.grab_set()
    return fd

def It():
    ft=Tk()
    
    ft.geometry('600x400')
    frat=Frame(ft)
    frat.pack(pady=10)
    
    Label(frat,text='Item Number:',font=fo,fg=fg).grid(row=0,column=0)
    Label(frat,text='Item Name:',font=fo,fg=fg).grid(row=1,column=0)
    Label(frat,text='Price',font=fo,fg=fg).grid(row=2,column=0)
    
    svnot=IntVar()
    svnat=StringVar()
    svpri=StringVar()

    def number(text):
        if int.isdigit(text):
            
            return True
        
        elif text is '':
            
            return True
        else :
            
            
            return False
        
        
    
    rug = frat.register(number)
       
 
    
    E1=ttk.Entry(frat,font='Arail 15',textvariable=svnot,validate='key' , validatecommand=(rug,'%P'))
    E1.grid(row=0,column=1)
    E2=ttk.Entry(frat,font='Arail 15',textvariable=svnat)
    E2.grid(row=1,column=1)
    E3=ttk.Entry(frat,font='Arail 15',textvariable=svpri)
    E3.grid(row=2,column=1)
    
    def showdatat():
        messagebox.showinfo('Data',{ svnot.get() , svnat.get(), svpri.get()})
       
    
    frat2=Frame(ft)
    frat2.pack(pady=10)
    Button(frat2,text='Add: ',bg=bg,font=(fo),fg=fg,command = showdatat).grid(row = 5,column=0)
    Button(frat2,text='Edit: ',bg=bg,font=(fo),fg=fg,command = showdatat).grid(row = 5,column=1)
    Button(frat2,text='Delete: ',bg=bg,font=(fo),fg=fg,command = showdatat).grid(row = 5,column=2)
    Button(frat2,text='Find: ',bg=bg,font=(fo),fg=fg,command = showdatat).grid(row = 7,column=2,padx=10,pady=10)
    Button(frat2,text='Close: ',bg=bg,font=(fo),fg=fg,command=ft.destroy).grid(row = 7,column=1,padx=10,pady=10)
    
    

    ft.grab_set()
    return ft




Label(fra,text=('-___________________________________________________________________-')).grid(row=0,column=0,pady=10)

Label(fra,text=('Company program'),bg=bg,font=fo,fg='black').grid(row=1,column=0,pady=10)

def play(name):
    f=None
    if name=='emp':f=Emp()
    if name=='dept':f=Dep()
    if name=='item':f=It()
    frr.grab_set()



Button(fra,text='Employment',bg=bg,font=fo,command =Emp ,fg=fg).grid(row=2,column=0,pady=10)
Button(fra,text='Department',bg=bg,font=fo, fg=fg,command = Dep).grid(row=3,column=0,pady=10)
Button(fra,text='Item',bg=bg,font=(fo),fg=fg,command =It).grid(row=4,column=0,pady=10)
Button(fra,text='Exit',bg=bg,font=(fo),fg=fg,command=f.destroy).grid(row=5,column=0,pady=10)
Label(fra,text=('-___________________________________________________________________-')).grid(row=6,column=0,pady=10)







f.mainloop()

input('press enter to exit....')
