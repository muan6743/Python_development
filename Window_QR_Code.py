import qrcode
from tkinter import *
from tkinter import messagebox

#Creating the window
wn = Tk()
wn.title('DataFlair QR Code Generator')
wn.geometry('700x700')
wn.config(bg='SteelBlue3')

#Label for the window
headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code with DataFlair", bg='azure', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)