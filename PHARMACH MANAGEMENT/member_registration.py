from cProfile import label
from cgitb import text
from email.headerregistry import Address
from email.mime import application
from logging import root
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox
from tkinter.tix import COLUMN
from turtle import title

class Registration:

    def __init__(self, root):
       self.root = root
       self.root.title("Club Member Registration System:")
       self.root.geometry("1350x750+0+0")
       self.root.configure(background="black")

       DateofOrder=StringVar()
       DateofOrder.set(time.strftime("%d/%m/%y"))

       var1 = StringVar()
       var2 = StringVar()
       var3 = StringVar()
       var4 = IntVar()

       Firstname=StringVar()
       Surname=StringVar()
       Address=StringVar()
       Postcode=StringVar()
       Telephone=StringVar()
       Ref=StringVar()
    
       
       Membership= StringVar()
       Membership.set("0")

       #------Function Declared----

       def iExit():
           iExit = tkinter.messagebox.askyesno("Club Member Registration Systems", "Confirm if you want to Exit:")
           if iExit > 0:
               root.destroy()
               return

       def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboprove_of_id.current(0)
            self.cbotype_of_member.current(0)
            self.cbopm.current(0)

        
       def iResetRecord():
           iResetRecord = tkinter.messagebox.askokcancel("Club Member Registration Systems", "Confirm if you want to add a new record")
           if iResetRecord > 0:
               Reset()
           elif iResetRecord <=0:
               Reset()
               self.txtReceipt.delete("1.0",END)
               return

       def Ref_No():
            
            x = random.randint(10903,600873)
            randomRef = str(x)
            Ref.set(randomRef)

       def Receipt():
               Ref_No()
               self.txtReceipt.insert(END,"\t" + Ref.get()+ "\t\t" + Firstname.get() + "\t\t" + Surname.get()
                                      + "\t\t" +Address.get() + "\t\t" +DateofOrder.get() + "\t\t" +Telephone.get()
                                      + "\t\t" + Membership.get() +"\n")
       
       def Membership_Fees():
              

               if (var4.get() == 1):
                       self.txtMembership.configure(state=NORMAL)
                       Item1 = float(50)
                       Membership.set("$" + str(Item1))
                       
               elif(var4.get() == 0):
                       self.txtMembership.configure(state=DISABLED)
                       Membership.set("0")













       
            
            
 


            


       #=========================Frame==========================

       Mainframe=Frame(self.root)
       Mainframe.grid()

       TitleFrame=Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
       TitleFrame.pack(side=TOP,)
       
       self.lblTitle=Label(TitleFrame,font=("arial",59,"bold"), text="Member Registration System ", padx=2)
       self.lblTitle.grid()

       #-------LowerFrames-------

       MemberDetailsFrame = LabelFrame(Mainframe, width=1350,height=500,bd=20, pady=5, relief=RIDGE)
       MemberDetailsFrame.pack(side=BOTTOM)

       FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=880,  height=400,relief=RIDGE)
       FrameDetails.pack(side=LEFT)

       MemberName_F = LabelFrame(FrameDetails, bd=10, width=350, height=400,
                  font=("arial",12,"bold"), text="Customer Name", relief=RIDGE)
       MemberName_F.grid(row=0,column=0)
     
       Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
       Receipt_ButtonFrame.pack(side=RIGHT)

       #--------------------------------
       self.lblReferenceNo=Label(MemberName_F,font=("arial",14,"bold"), text=" Reference NO ", bd=7)
       self.lblReferenceNo.grid(row=0, column=0,sticky="w")
       self.txtReferenceNo=Entry(MemberName_F,font=("arial",14,"bold"), bd=7,textvariable=Ref,state=DISABLED, insertwidth=2)
       self.txtReferenceNo.grid(row=0,column=1,sticky="w")

       self.lblfn=Label(MemberName_F,font=("arial",14,"bold"), text=" Firstname ", bd=7)
       self.lblfn.grid(row=1, column=0,sticky="w")
       self.txtfn=Entry(MemberName_F,font=("arial",14,"bold"), bd=7, textvariable=Firstname, insertwidth=2)
       self.txtfn.grid(row=1,column=1,sticky="w")

       self.lblsur=Label(MemberName_F,font=("arial",14,"bold"), text=" Surname ", bd=7)
       self.lblsur.grid(row=2, column=0,sticky="w")
       self.txtsur=Entry(MemberName_F,font=("arial",14,"bold"), bd=7, textvariable=Surname,insertwidth=2)
       self.txtsur.grid(row=2,column=1,sticky="w")

       self.lblad=Label(MemberName_F,font=("arial",14,"bold"), text=" Address ", bd=7)
       self.lblad.grid(row=3, column=0,sticky="w")
       self.txtad=Entry(MemberName_F,font=("arial",14,"bold"), bd=7,textvariable=Address, insertwidth=2)
       self.txtad.grid(row=3,column=1,sticky="w")
 
       self.lblps=Label(MemberName_F,font=("arial",14,"bold"), text=" PostCode ", bd=7)
       self.lblps.grid(row=4, column=0,sticky="w")
       self.txtps=Entry(MemberName_F,font=("arial",14,"bold"), bd=7, textvariable=Postcode, insertwidth=2)
       self.txtps.grid(row=4,column=1,sticky="w")

       self.lbltel=Label(MemberName_F,font=("arial",14,"bold"), text=" Telephone ", bd=7)
       self.lbltel.grid(row=5, column=0,sticky="w")
       self.txttel=Entry(MemberName_F,font=("arial",14,"bold"), bd=7, textvariable=Telephone,  insertwidth=2)
       self.txttel.grid(row=5,column=1,sticky="w")

       self.lbld=Label(MemberName_F,font=("arial",14,"bold"), text=" Date ", bd=7)
       self.lbld.grid(row=6, column=0,sticky="w")
       self.txtd=Entry(MemberName_F,font=("arial",14,"bold"), bd=7,textvariable=DateofOrder, insertwidth=2)
       self.txtd.grid(row=6,column=1,sticky="w")
    
       #----------------------Member function----
       self.lblprove_of_id= Label(MemberName_F,font=("arial",14,"bold"),text="Prove of ID", bd=7)
       self.lblprove_of_id.grid(row=7,column=0,sticky="w")

       self.cboprove_of_id= ttk.Combobox(MemberName_F,textvariable=var1,state="readonly",
                  font=("arial",14,"bold"),width=19)
       self.cboprove_of_id['value']=('','Licence','Driving Licence','Passport','student ID')
       self.cboprove_of_id.current(0)
       self.cboprove_of_id.grid(row=7,column=1)

       self.lbltype_of_member= Label(MemberName_F,font=("arial",14,"bold"),text="Type of Member", bd=7)
       self.lbltype_of_member.grid(row=8,column=0,sticky="w")
       
       self.cbotype_of_member= ttk.Combobox(MemberName_F,textvariable=var2,state="readonly",
                  font=("arial",14,"bold"),width=19)
       self.cbotype_of_member['value']=('','Full Member','Annual MemberShip','Pay As You Go','Honarary Member')
       self.cbotype_of_member.current(0)
       self.cbotype_of_member.grid(row=8,column=1)

       self.lblpm= Label(MemberName_F,font=("arial",14,"bold"),text="Method of Payment", bd=7)
       self.lblpm.grid(row=9,column=0,sticky="w")
       
       self.cbopm= ttk.Combobox(MemberName_F,textvariable=var3,state="readonly",
                  font=("arial",14,"bold"),width=19)
       self.cbopm['value']=('','Visa Card','Master Card','Debit Card','Cod')
       self.cbopm.current(0)
       self.cbopm.grid(row=9,column=1)

       #------------ check button-----

       self.chkMembership = Checkbutton(MemberName_F, text="Membership Fees", variable=var4, onvalue=1,
       offvalue=0,font=("arial",14,"bold"), command= Membership_Fees).grid(row=10,column=0,sticky="w")

       self.txtMembership = Entry(MemberName_F, font=("arial",14,"bold"), textvariable=Membership,bd=7,
               insertwidth=2,state=DISABLED,justify=RIGHT)
       self.txtMembership.grid(row=10,column=1)
       #---------------Receipt 
       self.lblLabel = Label(Receipt_ButtonFrame, font=("arial",10,"bold"),pady=10,
       text="Member Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\t Member Paid", bd=7)
       self.lblLabel.grid(row=0,column=0,columnspan=4)
       
       self.txtReceipt = Text(Receipt_ButtonFrame,width=112,height=22, font=("arial",10,"bold"))
       self.txtReceipt.grid(row=1,column=0,columnspan=4)

       #-------Buttons

       self.btnReceipt=Button(Receipt_ButtonFrame, padx=18, bd=7, font=("arial",10,"bold"), width=13,
               text="Receipt", command=Receipt).grid(row=2,column=0)

       self.btnReset=Button(Receipt_ButtonFrame, padx=18, bd=7, font=("arial",10,"bold"), width=13,
               text="Reset", command=iResetRecord).grid(row=2,column=1)

       self.btnExit=Button(Receipt_ButtonFrame, padx=18, bd=7, font=("arial",10,"bold"), width=13,
               text="Exit", command=iExit).grid(row=2,column=2)
                                
                                
                                
       
       
      













       #-------------------------
    

if __name__=='__main__':
    root = Tk()
    application = Registration (root)
    root.mainloop()





