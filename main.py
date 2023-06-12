from tkinter import *
from tkinter import ttk
import sqlite3
import addbook

con = sqlite3.connect('library.db')
cur = con.cursor()

class Main(object):

    def __init__(self, master):
        self.master = master

        #frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
        #top frame
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)
        #center frame
        centerFrame = Frame(mainFrame, width=1350, relief=RIDGE, bg='#e0f0f0', height=680)
        centerFrame.pack(side=TOP)
        #center left frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerLeftFrame.pack(side=LEFT)
        #center right frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerRightFrame.pack()

        #search bar
        searchBar = LabelFrame(centerRightFrame, width=440, height=75, text='Search Box', bg='#9bc9ff')
        searchBar.pack(fill=BOTH)
        self.labelSearch = Label(searchBar, text='Search : ', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.labelSearch.grid(row=0, column=0, padx=20, pady=10)
        self.entrySearch = Entry(searchBar, width=30, bd=10)
        self.entrySearch.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btnsearch = Button(searchBar, text='Search', font='arial 12', bg='#fcc324', fg='white')
        self.btnsearch.grid(row=0, column=4, padx=20, pady=10)

        #list bar
        listBar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        listBar.pack(fill=BOTH)
        self.labelList = Label(listBar, text='Short By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        self.labelList.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(listBar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(listBar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(listBar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btnList = Button(listBar, text='List Books', bg='#2488ff', fg='white', font='arial 12')
        btnList.grid(row=1, column=3, padx=40, pady=10)

        #title and image
        imageBar = Frame(centerRightFrame, width=440, height=350)
        imageBar.pack(fill=BOTH)
        self.titleRight = Label(imageBar, text='Welcome to our Library', font='arial 16 bold')
        self.titleRight.grid(row=0)
        self.imageLibrary = PhotoImage(file='icons/library.png')
        self.labelImage = Label(imageBar, image=self.imageLibrary)
        self.labelImage.grid(row=1)

################################################## Tool Bar ##################################################
        # add book button
        self.iconbook = PhotoImage(file='icons/add-book.png')
        self.btnbook = Button(topFrame, text='   Add Book', image=self.iconbook, compound=LEFT, font='arial 12 bold', command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=0)
        # add member button
        self.iconmember = PhotoImage(file='icons/add-user.png')
        self.btnmember = Button(topFrame, text='Add Member', font='arial 12 bold', padx=10, image=self.iconmember, compound=LEFT)
        self.btnmember.pack(side=LEFT, padx=10)
        #give book button
        self.icongive = PhotoImage(file='icons/give-book.png')
        self.btngive = Button(topFrame, text='Give Book', font='arial 12 bold', padx=10, image=self.icongive, compound=LEFT)
        self.btngive.pack(side=LEFT)

################################################## Tabs ##################################################

    #tab 1
        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.tabs.pack()
        self.tab1icon = PhotoImage(file='icons/library2.png')
        self.tab2icon = PhotoImage(file='icons/statistics.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2icon, compound=LEFT)

        #list books
        self.listBooks = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.scrollbar = Scrollbar(self.tab1, orient=VERTICAL)
        self.listBooks.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.scrollbar.config(command=self.listBooks.yview)
        self.listBooks.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=0, sticky=N+S+E)
        #list details
        self.listDetails = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.listDetails.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

    #tab 2
        self.labelBookCount = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.labelBookCount.grid(row=0)
        self.labelMemberCount = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.labelMemberCount.grid(row=1, sticky=W)
        self.labelTakenCount = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.labelTakenCount.grid(row=2, sticky=W)

    def addBook(self):
        add = addbook.AddBook()


def main():
    root = Tk()
    app = Main(root)
    root.title('Shelf Master: Library Management')
    root.geometry('1350x750+350+200')
    root.iconbitmap('icons/book-open.ico')
    root.mainloop()

if __name__ == '__main__':
    main()