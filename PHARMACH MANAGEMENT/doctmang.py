from csv import Dialect
from pydoc_data import topics
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


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
        Datetxt.grid(row=0,column=3,padx=5,pady=5,sticky=E)
        
        Ptnamelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Patient Name", padx=2, bg="#789e9e")
        Ptnamelbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        Ptnametxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= PtName)
        Ptnametxt.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Aptlbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text= "Appointment Time", padx=2, bg="#789e9e")
        Aptlbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Apttxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27,textvariable= Apptime)
        Apttxt.grid(row=2,column=3,padx=5,pady=5,sticky=E)

        
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













        




        
        

        






if __name__ =="__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()