from tkinter import *
from tkinter import ttk

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
        #list bar
        listBar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        listBar.pack(fill=BOTH)
        # add book button
        self.iconbook = PhotoImage(file='icons/add-book.png')
        self.btnbook = Button(topFrame, text='   Add Book', image=self.iconbook, compound=LEFT, font='arial 12 bold')
        self.btnbook.pack(side=LEFT, padx=10)
        # add member button
        self.iconmember = PhotoImage(file='icons/add-user.png')
        self.btnmember = Button(topFrame, text='Add Member', font='arial 12 bold', padx=10)
        self.btnmember.configure(image=self.iconmember, compound=LEFT)
        self.btnmember.pack(side=LEFT)


def main():
    root = Tk()
    app = Main(root)
    root.title('Shelf Master: Library Management')
    root.geometry('1350x750+350+200')
    root.iconbitmap('icons/book-open.ico')
    root.mainloop()

if __name__ == '__main__':
    main()