import tkinter
from tkinter import *
root=Tk()
root.title("Book Directory")
def show():
 print("hello guys")
root.resizable(True,True)
root.minsize(600,300)
root.maxsize(500,500)
la1=Label(root,text="Title" ,width=10,font=90)
la1.grid(row=0,column=0)
e1=Entry(root,width=30)
e1.grid(row=0,column=1)
la2=Label(root,text="Author",width=10,font=90)
la2.grid(row=0,column=2)
e2=Entry(root,width=30)
e2.grid(row=0,column=3)
la3=Label(root,text="Year",width=10,font=90)
la3.grid(row=1,column=0)
e3=Entry(root,width=30)
e3.grid(row=1,column=1)
la4=Label(root,text="ISBN No",width=10,font=90)
la4.grid(row=1,column=2)
e4=Entry(root,width=30)
e4.grid(row=1,column=3)

l=Listbox(root,width=60)
l.place(x=0,y=80)
root.mainloop()
