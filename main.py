from tkinter import *
from tkinter import ttk
import sqlite3
import addbook, addmember

con = sqlite3.connect('library.db')
cur = con.cursor()

class Main(object):
    def __init__(self, master):
        self.master = master

        def displayStatistics(evt):
            count_books = cur.execute('SELECT count(book_id) FROM books').fetchall()
            count_members = cur.execute('SELECT count(member_id) FROM members').fetchall()
            taken_books = cur.execute('SELECT count(status) FROM books WHERE status=1').fetchall()
            self.lbl_book_count.config(text='Total : ' + str(count_books[0][0]) + ' books in library')
            self.lbl_member_count.config(text='Total Members : ' + str(count_members[0][0]))
            self.lbl_taken_count.config(text='Taken Books : ' + str(taken_books[0][0]))
            displayBooks(self)

        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            self.list_books.delete(0, END)
            for book in books:
                self.list_books.insert(count, str(book[0])+'-'+book[1])
                count += 1
            def bookInfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute('SELECT * FROM books WHERE book_id=?', (id,))
                book_info = book.fetchall()
                self.list_details.delete(0, END)
                self.list_details.insert(0, 'Book Name : '+book_info[0][1])
                self.list_details.insert(1, 'Author : '+book_info[0][2])
                self.list_details.insert(2, 'Page : '+book_info[0][3])
                self.list_details.insert(3, 'Language : '+book_info[0][4])
                if book_info[0][5] == 0:
                    self.list_details.insert(4, 'Status : Available')
                else:
                    self.list_details.insert(4, 'Status : Unavailable')
            self.list_books.bind('<<ListboxSelect>>', bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)
            #self.tabs.bind('<ButtonRelease-1>', displayBooks)

        #frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
        #top frame
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)
        #center frame
        centerFrame = Frame(mainFrame, width=1350, height=680, relief=RIDGE, bg='#e0f0f0')
        centerFrame.pack(side=TOP)
        #center left frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        #center right frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack()

        #search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=75, text='Search Box', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar, text='Search : ', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white', command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=20, pady=10)

        #list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Sort By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List Books', bg='#2488ff', fg='white', font='arial 12', command=self.listBooks)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        #title and image
        image_bar = Frame(centerRightFrame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='Welcome to our Library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = PhotoImage(file='icons/library.png')
        self.lblImg = Label(image_bar, image=self.img_library)
        self.lblImg.grid(row=1)

################################## Tool Bar ####################################
        # add book
        self.iconbook = PhotoImage(file='icons/add-book.png')
        self.btnbook = Button(topFrame, text='   Add Book', image=self.iconbook, compound=LEFT, font='arial 12 bold', command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=2.5)
        # add member
        self.iconmember = PhotoImage(file='icons/add-user.png')
        self.btnmember = Button(topFrame, text='Add Member', image=self.iconmember, compound=LEFT, font='arial 12 bold', padx=10, command=self.addMember)
        self.btnmember.pack(side=LEFT, padx=2.5)
        #give book
        self.icongive = PhotoImage(file='icons/give-book.png')
        self.btngive = Button(topFrame, text='Give Book', image=self.icongive, compound=LEFT, font='arial 12 bold', padx=10)
        self.btngive.pack(side=LEFT, padx=2.5)

################################ Tabs ##########################################
        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/library2.png')
        self.tab2_icon = PhotoImage(file='icons/statistics.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)
    ##################### Tab 1 ####################
        #list book
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N+S+E)
        #list details
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)
    ##################### Tab 2 ####################
        self.lbl_book_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text='', pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

###################### Functions ##############################
        displayBooks(self)
        displayStatistics(self)

    def addBook(self):
        add = addbook.AddBook()

    def addMember(self):
        member = addmember.AddMember()
    
    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute('SELECT * FROM books WHERE book_name LIKE  ?', ('%'+value+'%',)).fetchall()
        self.list_books.delete(0, END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0])+'-'+book[1])
            count += 1
    
    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks = cur.execute('SELECT * FROM books').fetchall()
            self.list_books.delete(0, END)
            count = 0
            for book in allbooks:
                self.list_books.insert(count, str(book[0])+'-'+book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute('SELECT * FROM books WHERE status=?', (0,)).fetchall()
            self.list_books.delete(0, END)
            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0])+'-'+book[1])
                count += 1
        else:
            taken_books = cur.execute('SELECT * FROM books WHERE status=?', (1,)).fetchall()
            self.list_books.delete(0, END)
            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0])+'-'+book[1])
                count += 1

def main():
    root = Tk()
    app = Main(root)
    root.title("Shelf Master: Library Management")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/book-open.ico')
    root.mainloop()

if __name__ == '__main__':
    main()