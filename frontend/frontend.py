import tkinter
from tkinter import *
import backend
def add_command():
    backend.insert(e1.get(),
                   e2.get(),
                   e3.get(),
                   e4.get())
    l.delete(0,END)
    l.insert(END,
             (e1.get(),
              e2.get(),
              e3.get(),
              e4.get()))
def view_command():
    l.delete(0,END)
    for row in backend.view():
        l.insert(END,row)
def update_command():
    backend.update1(selected_tuple[0],
                   e1.get(),
                   e2.get(),
                   e3.get(),
                   e4.get())
def delete_command():
    backend.delete(selected_tuple[0])
def search_command():
    l.delete(0,END)
    row = None
    for row in backend.search(e1.get(),
                              e2.get(),
                              e3.get(),
                              e4.get()):
        l.insert(END,row)
def get_selected_row(event):
    global selected_tuple
    index=l.curselection()
    print(index[0])
    selected_tuple=l.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])

    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

root=Tk()
root.title("Book Directory")

root.resizable(True,True)
root.minsize(650,200)
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
l=Listbox(root,height=6,width=60)
l.grid(row=2,column=0,rowspan=6,columnspan=2)
s=Scrollbar(root)
s.grid(row=2,column=2,rowspan=6)
l.configure(yscrollcommand=s.set)
s.configure(command=l.yview)
l.bind('<<ListboxSelect>>',get_selected_row)
b1=Button(root,text="View All",command=view_command,width=15)
b1.grid(row=2,column=3)
b2=Button(root,text="Sreach Entry",command=search_command,width=15)
b2.grid(row=3,column=3)
b3=Button(root,text="Add Entry",command=add_command,width=15)
b3.grid(row=4,column=3)
b4=Button(root,text="Update Selected",command=update_command,width=15)
b4.grid(row=5,column=3)
b5=Button(root,text="Delete Selected",command=delete_command,width=15)
b5.grid(row=6,column=3)
b6=Button(root,text="close",width=15,command=exit)
b6.grid(row=7,column=3)
root.mainloop()

