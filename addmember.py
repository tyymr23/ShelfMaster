from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('library.db')
cur = con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add Member')
        self.resizable(False, False)

        ########################Frames########################

        #Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        #Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        #heading, image
        self.topImage = PhotoImage(file='icons/add-user-big.png')
        topImageLabel = Label(self.topFrame, image=self.topImage, bg='white')
        topImageLabel.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Add Member  ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ########################Entries and Labels########################

        #name
        self.labelName = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelName.place(x=40, y=40)
        self.entryName = Entry(self.bottomFrame, width=30, bd=4)
        self.entryName.insert(0, 'Please enter a name')
        self.entryName.place(x=150, y=45)
        #phone
        self.labelPhone = Label(self.bottomFrame, text='Phone :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelPhone.place(x=40, y=80)
        self.entryPhone = Entry(self.bottomFrame, width=30, bd=4)
        self.entryPhone.insert(0, 'Please enter phone number')
        self.entryPhone.place(x=150, y=85)
        #button
        button = Button(self.bottomFrame, text='Add Member', command=self.addMember)
        button.place(x=270, y=120)

    def addMember(self):
        name = self.entryName.get()
        phone = self.entryPhone.get()

        if (name and phone != ''):
            try:
                query = "INSERT INTO 'members' (member_name, member_phone) VALUES(?,?)"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo('Success', 'Succesfully added to database', icon='info')
            except:
                messagebox.showerror('Error', "Cannot add to database", icon='warning')
        else:
            messagebox.showerror('Error', "Fields cannot be empty", icon='warning')