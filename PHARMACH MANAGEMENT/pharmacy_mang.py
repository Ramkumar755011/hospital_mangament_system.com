from atexit import register
from csv import Dialect
from logging import root
from pydoc_data import topics
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from unicodedata import name

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


        self.Username= StringVar()
        self.Password = StringVar()
        

        self.LabelTitle = Label(self.frame, text="Pharmacy Management System", font=("arial",40,"bold"),
          bd=10, relief="sunken")
        self.LabelTitle.grid(row = 0, column=0, columnspan=2, pady=20)

        self.LoginFrame1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.LoginFrame1.grid(row=1, column=0)

        
        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.LoginFrame2.grid(row=2, column=0, pady=15)

        
        self.LoginFrame3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.LoginFrame3.grid(row=6, column=0,pady=5)

        self.button_reg = Button(self.LoginFrame3,text="Patient Regristration ",state= DISABLED,font=("arial",15,"bold"),
           command= self.Registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=5)

        self.button_Hosp = Button(self.LoginFrame3,text="Hospital Registration ",state= DISABLED,font=("arial",15,"bold"),
           command= self.Hosptial_window)
        self.button_Hosp.grid(row=0,column=1,padx=10,pady=5)

        self.button_Dr_appt = Button(self.LoginFrame3,text="Doctor Management",state= DISABLED,font=("arial",15,"bold"),
           command= self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=1,column=0,padx=10,pady=5)

        self.button_med_stock = Button(self.LoginFrame3,text="Contact Us ",state= DISABLED,font=("arial",15,"bold"),
           command= self.Medicine_stock)
        self.button_med_stock.grid(row=1,column=1,padx=10,pady=5)



  #now we will make user name and pwd frame

        self.LabelUsername = Label(self.LoginFrame1,text="User Name", font=("arial",20,"bold"),bd=3)
        self.LabelUsername.grid(row=0,column=0)

        self.textUsername = Entry(self.LoginFrame1,font=("arial",20,"bold"),bd=3,textvariable=self.Username)
        self.textUsername.grid(row=0,column=1,padx=40,pady=15)

        self.LabelPassword =  Label(self.LoginFrame1,text="Password", font=("arial",20,"bold"),bd=3)
        self.LabelPassword.grid(row=1,column=0)

        self.textPassword = Entry(self.LoginFrame1,font=("arial",20,"bold"),show="*",bd=3,textvariable=self.Password)
        self.textPassword.grid(row=1,column=1,padx=40,pady=15)



        self.button_login = Button(self.LoginFrame2, text="Login", width=20, font=("arial",18,"bold"),
          command= self.login_system)
        self.button_login.grid(row=0,column=0,padx=10,pady=10)

        
        self.button_Reset = Button(self.LoginFrame2, text="Reset", width=20, font=("arial",18,"bold"),
         command= self.reset_btn )
        self.button_Reset.grid(row=0,column=3,padx=10,pady=10)

        
        self.button_Exit = Button(self.LoginFrame2, text="Exit", width=20, font=("arial",18,"bold"),
          command = self.Exit_btn )
        self.button_Exit.grid(row=0,column=6,padx=10,pady=10)

    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if(user == str("Admin") and (pswd == str("admin"))):
         self.button_reg.config(state= NORMAL)
         self.button_Hosp.config(state= NORMAL)
         self.button_Dr_appt.config(state= NORMAL)
         self.button_med_stock.config(state=NORMAL)

        else:
         tkinter.messagebox.askyesno("Pharmacy Management System", "you have entered an invalid user name or password")
         self.button_reg.config(state= DISABLED)
         self.button_Hosp.config(state= DISABLED)
         self.button_Dr_appt.config(state= DISABLED)
         self.button_med_stock.config(state= DISABLED)
         #if username or pwd is incorrect it will be in its disabled state

         self.Username.set("")
         self.Password.set("")
         self.textUsername.focus()
    
    def reset_btn(self):
         self.button_reg.config(state= NORMAL)
         self.button_Hosp.config(state= NORMAL)
         self.button_Dr_appt.config(state= NORMAL)
         self.button_med_stock.config(state=NORMAL)

         # because when we will reset still we haven't given correct user id and pwd
         self.Username.set("")
         self.Password.set("")
         self.textUsername.focus()

    def Exit_btn(self):
         self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System","Are you sure want to exist")
         if self.Exit_btn > 0:
             # we will close that master screen
             self.master.destroy()
             return
            



        


        # first we will define our window
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hosptial_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)





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
                                
                                
                                
    
class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital management system")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")
        self.frame = Frame(self.root)
        self.frame.pack()


      

    

        Ref = StringVar()
        cmbTabletsNames=StringVar()
        HospitalCode =StringVar()
        Number_of_Tablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpiryDate=StringVar()
        DailyDose=StringVar()
        SideEffects=StringVar()
        MoreInformation=StringVar()
        StorageAdvice=StringVar()
        Medication=StringVar()
        PatientID=StringVar()
        PatientNHSNo=StringVar()
        PatientName=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        prescription=StringVar()
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))



        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)


        def Prescriptionfunc():
            Reference_numfunc()
            TextPresciption.insert(END,"Patient ID: \t\t"+PatientID.get()+"\n")
            TextPresciption.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            TextPresciption.insert(END,"Tablet: \t\t"+cmbTabletsNames.get()+"\n")
            TextPresciption.insert(END,"Number of tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPresciption.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
            TextPresciption.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPresciption.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPresciption.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPresciption.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
            return

                

            
        def Prescriptiondatafunc():
            Reference_numfunc()
            TextPresciptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+
            PatientName.get()+"\t\t"+DateofBirth.get()+"\t\t"+ PatientNHSNo.get()+"\t\t"+cmbTabletsNames.get()+"\t"+
            Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
            StorageAdvice.get()+"\t"+PatientID.get()+"\n")
            return
        
            

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital management system","Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return   

        def Deletefunc():
            Ref.set("")
            cmbTabletsNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            prescription.set("")
            TextPresciption.delete("1.0",END)
            TextPresciptionData.delete("1.0",END)
            return

        def Resetfunc():
            Ref.set("")
            cmbTabletsNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            prescription.set("")
            TextPresciption.delete("1.0",END)
        
            return


                

                 
            


        title = Label(self.root,text=" Hospital management",font=("montype corsive",42,"bold"),bd=5,relief=GROOVE,bg="#2eb8b8",fg="black")
        title.pack(side=TOP,fill=X)

        manage_Frame = Frame(self.root,width=1510,height=400,bd=5,relief=RIDGE,bg="#0099cc")
        manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root,width=1510,height=55,bd=5,relief=RIDGE,bg="#328695") 
        Button_Frame.place(x=10,y=460)


        Data_Frame = LabelFrame(self.root,width=1510,height=270,bd=5,relief=RIDGE,bg="#266e73") 
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(manage_Frame,width=1050,text = "General Information",font = ("arial",20,"italic bold"), height= 390,bd=7,relief=RIDGE,bg="#0099cc")
        Data_FrameLeft.pack(side = LEFT)


        Data_FrameRight = LabelFrame(manage_Frame,width=1050,text = "Prescription ",font = ("arial",15,"italic bold"), height= 390,bd=7,relief=RIDGE,bg="#0099cc") 
        Data_FrameRight.pack(side = RIGHT)

        Data_Framedata = LabelFrame(Data_Frame ,width=1050,text = "Prescription Data",font = ("arial",12,"italic bold"), height= 390,bd=4,relief=RIDGE,bg="#3eb7bb") 
        Data_Framedata.pack(side = LEFT)


       
        Datelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Date",padx=2,bg="#0099cc")
        Datelbl.grid(row=0,column=0,padx=10,pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= Date_of_Registration)
        Datetxt.grid(row=0,column=1,padx=10,pady=5, sticky=E)


        Reflbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Reference Number",padx=2,bg="#0099cc")
        Reflbl.grid(row=1,column=0,padx=10,pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,state = DISABLED,textvariable= Ref)
        Reftxt.grid(row=1,column=1,padx=10,pady=5, sticky=E)


        patientIDlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="patient ID",padx=2,bg="#0099cc")
        patientIDlbl.grid(row=2,column=0,padx=10,pady=5, sticky=W)
        patientIDtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= PatientID)
        patientIDtxt.grid(row=2,column=1,padx=10,pady=5, sticky=E)


        PatientNamelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Patient Name",padx=2,bg="#0099cc")
        PatientNamelbl.grid(row=3,column=0,padx=10,pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= PatientName)
        PatientNametxt.grid(row=3,column=1,padx=10,pady=5, sticky=E)




        DateofBirthlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="DateofBirth",padx=2,bg="#0099cc")
        DateofBirthlbl.grid(row=4,column=0,padx=10,pady=5, sticky=W)
        DateofBirthtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= DateofBirth)
        DateofBirthtxt.grid(row=4,column=1,padx=10,pady=5, sticky=E)


        Addresslbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="PatientAddress",padx=2,bg="#0099cc")
        Addresslbl.grid(row=5,column=0,padx=10,pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= PatientAddress)
        Addresstxt.grid(row=5,column=1,padx=10,pady=5, sticky=E)


        NHSnumberlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="NHSnumber",padx=2,bg="#0099cc")
        NHSnumberlbl.grid(row=6,column=0,padx=10,pady=5, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= PatientNHSNo)
        NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5, sticky=E)


        Tabletlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Tablet",padx=2,bg="#0099cc")
        Tabletlbl.grid(row=7,column=0,padx=10,pady=5, sticky=W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft,textvariable=cmbTabletsNames,width=25,state="readonly",font=("arial",12,"bold"))
        Tabletcmb['value']=("","paracetamol","Dan-p","Dio-i One","Calpol","Amlodipine  Besylate","Nexium",
                                "Singular","Plavix","Amoxicillian","Azithromycin","Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7,column=1,padx=10,pady=5)


        NumberofTabletslbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Number os Tablets",padx=2,bg="#0099cc")
        NumberofTabletslbl.grid(row=8,column=0,padx=10,pady=5, sticky=W)
        NumberofTabletstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable= Number_of_Tablets)
        NumberofTabletstxt.grid(row=8,column=1,padx=10,pady=5, sticky=E)



        Hospitalodelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="HospitalCode",padx=2,bg="#0099cc")
        Hospitalodelbl.grid(row=0,column=2,padx=10,pady=5, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= HospitalCode)
        HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5, sticky=E)



        StorageAdvicelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="StorageAdvice",padx=2,bg="#0099cc")
        StorageAdvicelbl.grid(row=1,column=2,padx=10,pady=5, sticky=W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft,textvariable=StorageAdvice,width=23,state="readonly",font=("arial",12,"bold"))
        StorageAdvicecmb['value']=("","Under room temp","below 5*c","below 0*c","Refrigration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1,column=3,padx=10,pady=5, sticky=E)


        Lot_numberlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Lot number",padx=2,bg="#0099cc")
        Lot_numberlbl.grid(row=2,column=2,padx=10,pady=5, sticky=W)
        Lot_numbertxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= Lot)
        Lot_numbertxt.grid(row=2,column=3,padx=10,pady=5, sticky=E)


        IssuedDatelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Issue Date",padx=2,bg="#0099cc")
        IssuedDatelbl.grid(row=3,column=2,padx=10,pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= IssuedDate)
        IssuedDatetxt.grid(row=3,column=3,padx=10,pady=5, sticky=E)

        
        
        ExpiryDatelbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Expiry Date",padx=2,bg="#0099cc")
        ExpiryDatelbl.grid(row=4,column=2,padx=10,pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= ExpiryDate)
        ExpiryDatetxt.grid(row=4,column=3,padx=10,pady=5, sticky=E)

        DailyDoselbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Daily Dose",padx=2,bg="#0099cc")
        DailyDoselbl.grid(row=5,column=2,padx=10,pady=5, sticky=W)
        DailyDosetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= DailyDose)
        DailyDosetxt.grid(row=5,column=3,padx=10,pady=5, sticky=E)


        SideEffectlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Side Effect",padx=2,bg="#0099cc")
        SideEffectlbl.grid(row=6,column=2,padx=10,pady=5, sticky=W)
        SideEffecttxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= SideEffects)
        SideEffecttxt.grid(row=6,column=3,padx=10,pady=5, sticky=E)

        MoreInformationlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="MoreInformation",padx=2,bg="#0099cc")
        MoreInformationlbl.grid(row=7,column=2,padx=10,pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= MoreInformation)
        MoreInformationtxt.grid(row=7,column=3,padx=10,pady=5, sticky=E)
        
        Medicationlbl = Label(Data_FrameLeft,font= ("arial",12,"bold"), width=20,text="Medication",padx=2,bg="#0099cc")
        Medicationlbl.grid(row=8,column=2,padx=10,pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable= Medication)
        Medicationtxt.grid(row=8,column=3,padx=10,pady=5, sticky=E)


        TextPresciption = Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
        TextPresciption.grid(row=0,column=0)

        TextPresciptionData = Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=12)
        TextPresciptionData.grid(row=1,column=0)


        prescriptionbtn = Button(Button_Frame,text="Prescription",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command= Prescriptionfunc)
        prescriptionbtn.grid(row=0,column=0,padx=15)

        Receiptbtn = Button(Button_Frame,text="PrescriptionData",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=Prescriptiondatafunc)
        Receiptbtn.grid(row=0,column=1,padx=15)


        Resetbtn = Button(Button_Frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=Resetfunc)
        Resetbtn.grid(row=0,column=2,padx=15)


        Deletebtn = Button(Button_Frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=Deletefunc)
        Deletebtn.grid(row=0,column=3,padx=15)

        Exitbtn = Button(Button_Frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)


        prescriptiondatarow = Label(Data_Framedata,bg="white",font=("arial",12,"bold"),text="Data\tReference Id\tPatient Name\tData of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Data\tDaily Dose\tpatientID")
        prescriptiondatarow.grid(row=0,column=0,sticky=W)








        






class Doctor:
    def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        #### we will Declare all functions together
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId = StringVar()
        DrName = StringVar()
        DateofBirth =  StringVar()
        Spes =  StringVar()
        GovtPri =  StringVar()
        Surgeries =  StringVar()
        Experiences =  StringVar()
        Nurses =  StringVar()
        DrMobile =  StringVar()
        PtName =  StringVar()
        Apptime =  StringVar()
        ptAge =  StringVar()
        patientAddress =  StringVar()
        ptMobile =  StringVar()
        Disease =  StringVar()
        Case =  StringVar()
        BenefitCard =  StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Management System", "Are you sure want to want to exit ?")
            if exitbtn > 0:
                root.destroy()
            return

        def resetfunc():
            DrName.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            ptAge.set("")
            patientAddress.set("")
            ptMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return

        def deletefunc():
             DrName.set("")
             DateofBirth.set("")
             Spes.set("")
             GovtPri.set("")
             Surgeries.set("")
             Experiences.set("")
             Nurses.set("")
             DrMobile.set("")
             PtName.set("")
             Apptime.set("")
             ptAge.set("")
             patientAddress.set("")
             ptMobile.set("")
             Disease.set("")
             Case.set("")
             BenefitCard.set("")
             TextPrescription.delete("1.0",END)
             TextPrescriptionData.delete("1.0",END)
             return

        def Patient_idfunc():
             ranumber = random.randint(100000,999999)
             randomnumber = str(ranumber)
             DrId.set(randomnumber)

        def Prescriptiondatafunc():
            Patient_idfunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"
            +DrName.get()+"\t\t"+DateofBirth.get()+"\t\t"+Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+
            Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
            PtName.get()+"\t\t"+Case.get()+"\t"+ptAge.get()+"\n")
            return

        def Prescriptionfunc():
            Patient_idfunc()
            TextPrescription.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END,"Patient Name: \t\t"+PtName.get()+"\n")
            TextPrescription.insert(END,"Appointment Time: \t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END,"Age: \t\t"+ptAge.get()+"\n")
            TextPrescription.insert(END,"Address: \t\t"+patientAddress.get()+"\n")
            TextPrescription.insert(END,"Disease: \t\t"+Disease.get()+"\n")
            TextPrescription.insert(END,"Case: \t\t"+Case.get()+"\n")
            TextPrescription.insert(END,"Benefit Card: \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END,"To meet Dr: \t\t"+DrName.get.get()+"\n")
            TextPrescription.insert(END,"Dr. Mobile No.: \t\t"+DrMobile.get()+"\n")
            return

            

            return

        # Title
        title = Label(self.root , text = "Doctor Management System", font=("monotype corsiva",42,"bold"),bd=5,
             relief= GROOVE, bg = "#b7d8d6", fg ="black")
        title.pack(side= TOP, fill = X)

        #Frame
        Manage_Frame = Frame(self.root,width=1510,height=400,bd=5,relief= RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10,y=80)

        Buttons_Frame = Frame(self.root,width=1510,height=55,bd=4,relief= RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10,y=460)

        Data_Frame = LabelFrame(self.root,width=1510,height=270,bd=4,relief= RIDGE, bg="#266E73")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",
        font=("arial",20,"italic bold"), height=390, bd=7, pady=1, relief= RIDGE, bg="#789e9e")
        Data_FrameLeft.pack(side = LEFT)

        
        Data_FrameRight = LabelFrame(Manage_Frame, width=450, text="Patient's Information",
        font=("arial",15,"italic bold"), height=390, bd=7,  relief= RIDGE, bg="#789ede")
        Data_FrameRight.pack(side = RIGHT)


        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Doctor's Detials",
        font=("arial",12,"italic bold"), height=390, bd=4, bg="#4d6466",  relief= RIDGE, fg="#b7d8d6")
        Data_Framedata.pack(side = LEFT)
        


        DrIdlbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Doctor's ID", bg="#789e9e")
        DrIdlbl.grid(row=0, column=0,padx=10,pady=5,sticky=W)
        DrIdtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, state=DISABLED,textvariable=DrId)
        DrIdtxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

        DrNamelbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Doctor's Name", bg="#789e9e")
        DrNamelbl.grid(row=1, column=0,padx=10,pady=5,sticky=W)
        DrNametxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=DrName)
        DrNametxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)
        
        Dateofbirthlbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Date of Birth", bg="#789e9e")
        Dateofbirthlbl.grid(row=2, column=0,padx=10,pady=5,sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=DateofBirth)
        Dateofbirthtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)

        speslbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Specialisation", bg="#789e9e")
        speslbl.grid(row=3, column=0,padx=10,pady=5,sticky=W)
        spestxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=Spes)
        spestxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)
        
        GovtPrilbl = Label(Data_FrameLeft , font=("arial",12,"bold"), width=20,text="Govt/Private",bg="#789e9e")
        GovtPrilbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable=GovtPri, width=25, state="readonly",
        font=("arial",12,"bold"))
        GovtPricmb['values'] = ("","Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        surglbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="TotalSurgeries", bg="#789e9e")
        surglbl.grid(row=5, column=0,padx=10,pady=5,sticky=W)
        surgtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=Surgeries)
        surgtxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        Exlbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Experience in Years", bg="#789e9e")
        Exlbl.grid(row=6, column=0,padx=10,pady=5,sticky=W)
        Extxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=Experiences)
        Extxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

        nurselbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Nurses under Dr", bg="#789e9e")
        nurselbl.grid(row=7, column=0,padx=10,pady=5,sticky=W)
        nursetxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=Nurses)
        nursetxt.grid(row=7,column=1,padx=10,pady=5,sticky=E)

        moblbl = Label(Data_FrameLeft ,font=("arial",12,"bold"), width=20, text="Doctor Mobile No.", bg="#789e9e")
        moblbl.grid(row=8, column=0,padx=10,pady=5,sticky=W)
        mobtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"), width=27, textvariable=DrMobile)
        mobtxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)

        Datelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Date", padx=2, bg="#789e9e")
        Datelbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= Date_of_Registration)
        Datetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)
        
        Ptnamelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Name", padx=2, bg="#789e9e")
        Ptnamelbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        Ptnametxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= PtName)
        Ptnametxt.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Aptlbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Appointment Time", padx=2, bg="#789e9e")
        Aptlbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Apttxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= Apptime)
        Apttxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        
        Ptagelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Age", padx=2, bg="#789e9e")
        Ptagelbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        Ptagetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= ptAge)
        Ptagetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        
        Ptaddlbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Address", padx=2, bg="#789e9e")
        Ptaddlbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        Ptaddtxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= patientAddress)
        Ptaddtxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        
        Ptmoblbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Mobile No", padx=2, bg="#789e9e")
        Ptmoblbl.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        Ptmobtxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= ptMobile)
        Ptmobtxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        dislbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Disease", padx=2, bg="#789e9e")
        dislbl.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        distxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= Disease)
        distxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        Caselbl = Label(Data_FrameLeft , font=("arial",12,"bold"), width=20,text="Case",padx=2,bg="#789e9e")
        Caselbl.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable= Case, width=25, state="readonly",
        font=("arial",12,"bold"))
        Casecmb['values'] = ("","New Case","Old Case")
        Casecmb.current(0)
        Casecmb.grid(row=7,column=3,padx=10,pady=5,sticky=E)

        
        Caslbl = Label(Data_FrameLeft , font=("arial",12,"bold"), width=20,padx=10,text="Benefit Card",bg="#789e9e")
        Caslbl.grid(row=8,column=2,sticky=W)
        Cascmb = ttk.Combobox(Data_FrameLeft, textvariable= BenefitCard, width=25, state="readonly",
        font=("arial",12,"bold"))
        Cascmb['values'] = ("","Ayushman card","Health Insurance","Senior Citizen","Army Card")
        Cascmb.current(0)
        Cascmb.grid(row=8,column=3,padx=10,sticky=E)

        #prescription

        TextPrescription = Text(Data_FrameRight, font=("arial",12,"bold"), width=55, height=17,padx=3,
        pady=5)
        TextPrescription.grid(row=0,column=0)
        TextPrescriptionData = Text(Data_Framedata, font=("arial",12,"bold"), width=203, height=12)
        TextPrescriptionData.grid(row=1,column=0)

        #button
        Prescriptionbtn = Button(Buttons_Frame, text="Patient Information", bg="#fe615a", activebackground="#cc6686",
        font=("arial",13,"bold"),width=22, command=Prescriptionfunc)
        Prescriptionbtn.grid(row=0,column=0,padx=15)

        docbtn = Button(Buttons_Frame, text="Doctor's Details", bg="#fe615a", activebackground="#cc6686",
        font=("arial",13,"bold"),width=22, command=Prescriptiondatafunc)
        docbtn.grid(row=0,column=1,padx=15)

        delbtn = Button(Buttons_Frame, text="Reset", bg="#fe615a", activebackground="#cc6686",
        font=("arial",13,"bold"),width=22, command=resetfunc)
        delbtn.grid(row=0,column=2,padx=15)

        delebtn = Button(Buttons_Frame, text="Delete", bg="#fe615a", activebackground="#cc6686",
        font=("arial",13,"bold"),width=22, command=deletefunc)
        delebtn.grid(row=0,column=3,padx=15)

        deleebtn = Button(Buttons_Frame, text="Exit", bg="#fe615a", activebackground="#cc6686",
        font=("arial",13,"bold"),width=22, command= exitbtn)
        deleebtn.grid(row=0,column=4,padx=15)


        Prescriptiondatarow = Label(Data_Framedata, bg="white", font=("arial",12,"bold"),
        text="Data\tDoctor IdDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)


        

class windows5:
    def __init__(self,master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geometry('600x540')
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

   















    
        

if __name__ =="__main__":
    main()