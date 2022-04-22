# Developer: Jack Bowman
# Program: treeview_students
# Date: 04/05/2022

from tkinter import *
from tkinter import ttk

# create root window
root = Tk()
root.title('Status Board')
root.geometry('500x500')
root['bg'] = '#AC99F2'

# create frames to house info
students_frame = Frame(root)
students_frame.pack()

# scrollbars
students_scroll = Scrollbar(students_frame)
students_scroll.pack(side=RIGHT, fill=Y)

students_scroll = Scrollbar(students_frame, orient='horizontal')
students_scroll.pack(side=BOTTOM, fill=X)

# Create table frame
students = ttk.Treeview(students_frame, yscrollcommand=students_scroll.set, xscrollcommand=students_scroll.set)

students.pack()

students_scroll.config(command=students.yview)
students_scroll.config(command=students.xview)

# define columns
students['columns'] = ('stuID', 'firstName', 'lastName', 'GPA')

# Format columns
students.column("#0", width=0, stretch=NO)
students.column("stuID", anchor=CENTER, width=80)
students.column("firstName", anchor=CENTER, width=80)
students.column("lastName", anchor=CENTER, width=80)
students.column("GPA", anchor=CENTER, width=80)


# Create Headings
students.heading("#0", text="", anchor=CENTER)
students.heading("stuID", text="ID", anchor=CENTER)
students.heading("firstName", text="FName", anchor=CENTER)
students.heading("lastName", text="LName", anchor=CENTER)
students.heading("GPA", text="GPA", anchor=CENTER)


# Insert teams
students.insert(parent='', index='end', iid=0, text='',
                values=('101', 'John', 'Williams', '2.5'))
students.insert(parent='', index='end', iid=1, text='',
                values=('102', 'Billy', 'Johnson', '3.4'))
students.insert(parent='', index='end', iid=2, text='',
                values=('103', 'Robert', 'Clemens', '4.0'))
students.insert(parent='', index='end', iid=3, text='',
                values=('104', 'Nolan', 'Arenado', '3.1'))
students.insert(parent='', index='end', iid=4, text='',
                values=('105', 'Manny', 'Machado', '1.6'))
students.insert(parent='', index='end', iid=5, text='',
                values=('106', 'Miguel', 'Sano', '2.8'))
students.insert(parent='', index='end', iid=6, text='',
                values=('107', 'Joey', 'Votto', '3.7'))
students.insert(parent='', index='end', iid=7, text='',
                values=('108', 'Bryce', 'Harper', '2.2'))
students.insert(parent='', index='end', iid=8, text='',
                values=('109', 'Andrew', 'McCutchen', '3.0'))
students.insert(parent='', index='end', iid=9, text='',
                values=('110', 'Willhelm', 'Klink', '2.8'))
students.insert(parent='', index='end', iid=10, text='',
                values=('111', 'Adrian', 'Beltre', '4.0'))
students.pack()

frame = Frame(root)
frame.pack(pady=20)

# Labels
stuID = Label(frame, text="stuID")
stuID.grid(row=0, column=0)

stuFName = Label(frame, text="firstName")
stuFName.grid(row=0, column=1)

stuLName = Label(frame, text="lastName")
stuLName.grid(row=0, column=2)

stuGPA = Label(frame, text="GPA")
stuGPA.grid(row=0, column=3)

# Entry boxes: ID, FName, LName, GPA
stuIDEntry = Entry(frame)
stuIDEntry.grid(row=1, column=0)

stuFNameEntry = Entry(frame)
stuFNameEntry.grid(row=1, column=1)

stuLNameEntry = Entry(frame)
stuLNameEntry.grid(row=1, column=2)

GPAEntry = Entry(frame)
GPAEntry.grid(row=1, column=3)


# Select Record
def select_record():
    # clear entry boxes
    stuIDEntry.delete(0, END)
    stuFNameEntry.delete(0, END)
    stuLNameEntry.delete(0, END)
    GPAEntry.delete(0, END)

    # Get row that has focus
    selected = students.focus()

    # grab record values
    values = students.item(selected, 'values')

    # Insert focus row in entry boxes
    stuIDEntry.insert(0, values[0])
    stuFNameEntry.insert(0, values[1])
    stuLNameEntry.insert(0, values[2])
    GPAEntry.insert(0, values[3])


# Update Record
def update_record():
    selected = students.focus()
    # save new data
    students.item(selected, text="", values=(stuIDEntry.get(), stuFNameEntry.get(), stuLNameEntry.get(), GPAEntry.get()))

    # clear entry boxes
    stuIDEntry.delete(0, END)
    stuFNameEntry.delete(0, END)
    stuLNameEntry.delete(0, END)
    GPAEntry.delete(0, END)


# Buttons
select_button = Button(root, text="Select Record", command=select_record)
select_button.pack(pady=10)

refresh_button = Button(root, text="Refresh Record", command=update_record)
refresh_button.pack(pady=10)

temp_label = Label(root, text="")
temp_label.pack()

root.mainloop()