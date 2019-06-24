from tkinter import *
from tkinter import ttk

root=Tk()

detail_flag=0
main_style=ttk.Style()
main_style.configure('Header.TLabel',font=('Arial',18,'bold'))
ttk.Label(root,text="Todo Manager",font=('Sans-serif',20)).pack()

def show_details(label):
    global detail_flag
    global show_detail_button
    if(detail_flag==0):
        label.grid(row=2)
        show_detail_button.config(text="hide detail")
        detail_flag=1
    else:
        label.grid_forget()
        show_detail_button.config(text="show detail")
        detail_flag=0


def add_todo(event):
    global main_style
    new_frame=ttk.Frame(root,width=50)
    new_frame.pack()

    def delete():
        new_frame.pack_forget()

    todo=main_entry.get()
    details=sub_entry.get()

    ttk.Label(new_frame,text=todo,style='Header.TLabel',wraplength=160).grid(row=0,column=0,stick='nw')
    detail_label=ttk.Label(new_frame,text=details,wraplength=160)
    global show_detail_button
    show_detail_button=ttk.Button(new_frame,text="show details",command=lambda :show_details(detail_label))
    show_detail_button.grid(row=0,column=1,stick='e')

    global delete_button
    delete_button=ttk.Button(new_frame,text="Delete",command=delete)
    delete_button.grid(row=0,column=2,stick='e')

    ttk.Button(new_frame,text="Delete")
    main_entry.delete(0,'end')
    sub_entry.delete(0,'end')


root.resizable(False,False)
main_entry_label=ttk.Label(root,text="Enter todo")
main_entry_label.pack(anchor='w')
main_entry=ttk.Entry(root,width=50)
main_entry.pack()

sub_entry_label=ttk.Label(root,text="Enter todo details")
sub_entry_label.pack(anchor='w')
sub_entry=ttk.Entry(root,width=50)
sub_entry.pack()

add_button=ttk.Button(root,text="Add",command=lambda:add_todo(root)).pack()

root.bind('<Return>',add_todo)

for i in root.pack_slaves():
    i.pack(padx=4,pady=4)
root.mainloop()