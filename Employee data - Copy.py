
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

frm =Tk()
fo = ('None 25 bold')
bg='#ffffff'
bgtxt='#ffffff'
fg = '#000000'
fw=1000
fh=500
pad = 10
x = (frm.winfo_screenwidth()-fw)/2
y = (frm.winfo_screenheight()-fh)/2-50

frm.geometry('%dx%d+%d+%d' % (fw,fh,x,y))
frm.title('Empolyee File Data')
frm.configure(bg=bg)

Label(frm , text = " Employs Data" ,font = (fo) , bg='navy' , fg ='lightblue' ).pack(pady=pad)
fra = Frame(frm,bg=bg)
fra.pack(pady=pad)
Label(fra,text="Name:",bg=bg,fg=fg,font=fo).grid(row=0,column=0)
Label(fra,text="Adress:",bg=bg,fg=fg,font=fo).grid(row=1,column=0)
Label(fra,text="Phone:",bg=bg,fg=fg,font=fo).grid(row=2,column=0)
svcode= StringVar()
svname= StringVar()
svaddress= StringVar()
Tcode=Entry(fra,bg=bg,fg=fg,font=(fo), textvariable=svcode)
Tname=Entry(fra,bg=bg,fg=fg,font=(fo), textvariable=svname)
Taddress=Entry(fra,bg=bg,fg=fg,font=(fo), textvariable=svaddress)
Tcode.grid(row=0,column=1,pady=pad)
Tname.grid(row=1,column=1,pady=pad)
Taddress.grid(row=2,column=1,pady=pad)
def create():
    if svcode.get().strip()=='':
        messagebox.showinfo('','Code is empty')
        Tcode.focus()

    elif svname.get().strip()=='':
        
        messagebox.showinfo('','Name is empty')
        Tname.focus()

    elif svaddress.get().strip()=='':
        messagebox.showinfo('','Adress is empty')
        Taddress.focus()

    else:
        file= svcode.get() + '-' + svname.get() + '.txt'

        f=open(file,'w+')
        f.write('Name:'+ svcode.get()+'\n')
        f.write('Address:'+ svname.get()+'\n')
        f.write('Phone:'+ svaddress.get()+'\n')
        f.close()
        messagebox.showinfo('' ,'Employs file created.')
btns = ttk.Style()
btns.configure('TButton' ,font = (fo) ,pady=pad )
ttk.Button(frm,text='Create employee file data',command=create).pack()
ttk.Button(frm,text= 'Exit now ',command=frm.destroy).pack()

frm.mainloop()


input("press enter to exit.....")
