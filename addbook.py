from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('library.db')
cur = con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add Book')
        self.resizable(False, False)

        ########################Frames########################

        #Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        #Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        #heading, image
        self.topImage = PhotoImage(file='icons/add-book-big.png')
        topImageLabel = Label(self.topFrame, image=self.topImage, bg='white')
        topImageLabel.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Add Book  ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ########################Entries and Labels########################

        #name
        self.labelName = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelName.place(x=40, y=40)
        self.entryName = Entry(self.bottomFrame, width=30, bd=4)
        self.entryName.insert(0, 'Please enter a book name')
        self.entryName.place(x=150, y=45)
        #author
        self.labelAuthor = Label(self.bottomFrame, text='Author :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelAuthor.place(x=40, y=80)
        self.entryAuthor = Entry(self.bottomFrame, width=30, bd=4)
        self.entryAuthor.insert(0, 'Please enter an author name')
        self.entryAuthor.place(x=150, y=85)
        #page
        self.labelPage = Label(self.bottomFrame, text='Page :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelPage.place(x=40, y=120)
        self.entryPage = Entry(self.bottomFrame, width=30, bd=4)
        self.entryPage.insert(0, 'Please enter page size')
        self.entryPage.place(x=150, y=125)
        #language
        self.labelLanguage = Label(self.bottomFrame, text='Language :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.labelLanguage.place(x=40, y=160)
        self.entryLanguage = Entry(self.bottomFrame, width=30, bd=4)
        self.entryLanguage.insert(0, 'Please enter a language')
        self.entryLanguage.place(x=150, y=165)
        #button
        button = Button(self.bottomFrame, text='Add Book', command=self.addBook)
        button.place(x=270, y=200)

    def addBook(self):
        name = self.entryName.get()
        author = self.entryAuthor.get()
        page = self.entryPage.get()
        language = self.entryLanguage.get()

        if (name and author and page and language != ''):
            try:
                query = "INSERT INTO 'books' (book_name, book_author, book_page, book_language) VALUES(?,?,?,?)"
                cur.execute(query, (name, author, page, language))
                con.commit()
                messagebox.showinfo('Success', 'Succesfully added to database', icon='info')
            except:
                messagebox.showerror('Error', "Cannot add to database", icon='warning')
        else:
            messagebox.showerror('Error', "Fields cannot be empty", icon='warning')