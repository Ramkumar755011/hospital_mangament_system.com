from cgitb import text
from doctest import master
import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from tokenize import String


def main():
    root=Tk()
    app=contact(root)
    root.mainloop()

class contact:
    def __init__(self,master):
        self.master=master
        self.master.title("Contact Us:")
        self.master.geometry("600x600")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Name = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.email = StringVar()


        self.LabelTitle = Label(self.frame,text = " Contact Us", font=("arial",40,"bold"),bd=10, relief= "sunken")
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.LoginFrame1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.LoginFrame2.grid(row=2,column=0,pady=15)

        # now we will define

        self.LabelName = Label(self.LoginFrame1, text="Name", font=("arial",20,"bold"),bd=3)
        self.LabelName.grid(row=0,column=0)

        self.textName = Entry(self.LoginFrame1,font=("arial",20,"bold"),bd=3,textvariable= self.Name)
        self.textName.grid(row=0,column=1,padx=40,pady=15)

        self.Labelgender = Label(self.LoginFrame1, text="gender", font=("arial",20,"bold"),bd=3)
        self.Labelgender.grid(row=1,column=0)

        self.textgender = Entry(self.LoginFrame1,font=("arial",20,"bold"),bd=3,textvariable= self.gender)
        self.textgender.grid(row=1,column=1,padx=40,pady=15)

        self.Labelcontact = Label(self.LoginFrame1, text="Contact Us", font=("arial",20,"bold"),bd=3)
        self.Labelcontact.grid(row=2,column=0)

        self.textcontact = Entry(self.LoginFrame1,font=("arial",20,"bold"),bd=3,textvariable= self.contact)
        self.textcontact.grid(row=2,column=1,padx=40,pady=15)

        self.Labelemail = Label(self.LoginFrame1, text="Email", font=("arial",20,"bold"),bd=3)
        self.Labelemail.grid(row=3,column=0)

        self.textemail = Entry(self.LoginFrame1,font=("arial",20,"bold"),bd=3,textvariable= self.email)
        self.textemail.grid(row=3,column=1,padx=40,pady=15)

        self.button_Register = Button(self.LoginFrame2, text="Register", width=20, font=("arial",18,"bold"), command= self.login_system
        )
        self.button_Register.grid(row=0, column=0,padx=10,pady=10)



        self.button_Exit = Button(self.LoginFrame2, text="Exit", width=20, font=("arial",18,"bold"),command= self.exit_btn
        )
        self.button_Exit.grid(row=0, column=6,padx=10,pady=10)
    
    def login_system(self):
        print("Registered successfully")

    def exit_btn(self):
        self.exit_btn = tkinter.messagebox.askyesno("hospital management system", "Are you sure want to exit")
        if self.exit_btn >0:

            self.master.destroy()
            return

   






















if __name__ == "__main__":
    main()
    
                