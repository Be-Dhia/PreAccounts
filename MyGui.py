from tkinter import *
from Func import Fun
from PIL import ImageTk , Image

class Gui:

    def __init__(self , root):
        root.geometry('500x600+400+100')

        #defining Resizable window resizable(bool , bool) width , height
        root.resizable(True , True )

        #Change Window Title 
        root.title("Cookies Installer :) ")

        #changing background Color
        root.config(background='white')

        #changing icon
        root.iconbitmap('ico\icons8_broken_computer.ico')

    # Create a photoimage object of the image in the path
        image1 = Image.open("ico\\netflix-new-logo.png").convert("RGB")
        image1 = image1.resize((300,100))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(width='500',height='100', bg='white' , image=test)
        label1.image = test
        # Position image
        label1.place(x=0, y=0)

        # Create a photoimage object of the image in the path
        image1 = Image.open("ico\\shahid.png").convert("RGB")
        image1 = image1.resize((300,200))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(width='500',height='200', bg='white' , image=test)
        label1.image = test
        # Position image
        label1.place(x=0, y=200)
        #set minimum or max Size for the Form
        #root.minsize(200,200) | root.maxsize(width , height)

        #declare new hidden form to show it later (we can use , normal , iconic , ...)
        #root2 = Tk()
        #root2.state('withdrawn')

        #Declare new Frame (!! not a form)
        fr1 = Frame(width='500',height='100' ,bg='white')
        fr1.place(x=0 , y=100)

        #declare a button Button(frame , option)
        bt1 = Button(fr1 , text='Netflix' , fg='Red' , bg='White',width='30',font='Arial',command=Fun.onClick)
        bt1.place(x=90 , y=30)

        bt2 = Button(root , text='Shahid Vip' , fg='Green' , bg='White',width='30',font='Arial',command=Fun.shahid)
        bt2.place(x=90 , y=400)

        bt3 = Button(root , text='Contact Me' , fg='black' , bg='White',width='30',font='Arial',command=Fun.contact)
        bt3.place(x=90 , y=500)

        #Declare a Label
        #lb1 = Label(root , text='Hello World !' , fg='Red' ,bg='white',font=32)
        #lb1.place(x=190,y=20)