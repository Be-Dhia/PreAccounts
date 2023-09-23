from tkinter import *
from Func import Fun
class Gui:

    def __init__(self , root):
        root.geometry('500x500+400+100')

        #defining Resizable window resizable(bool , bool) width , height
        root.resizable(False , False )

        #Change Window Title 
        root.title("Cookies Installer :) ")

        #changing background Color
        root.config(background='white')

        #changing icon
        root.iconbitmap('ico\icons8_broken_computer.ico')


        #set minimum or max Size for the Form
        #root.minsize(200,200) | root.maxsize(width , height)

        #declare new hidden form to show it later (we can use , normal , iconic , ...)
        #root2 = Tk()
        #root2.state('withdrawn')

        #Declare new Frame (!! not a form)
        fr1 = Frame(width='500',height='100',bg='gray')
        fr1.place(x=0 , y=100)

        #declare a button Button(frame , option)
        bt1 = Button(fr1 , text='Netflix' , fg='Red' , bg='White',width='30',font='Arial',command=Fun.onClick)
        bt1.place(x=90 , y=30)

        #Declare a Label
        lb1 = Label(root , text='Hello World !' , fg='Red' ,bg='white',font=32)
        lb1.place(x=190,y=20)