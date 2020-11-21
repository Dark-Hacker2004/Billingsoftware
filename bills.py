from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("AIMS BILL-SOFTWARE")
        bg_color = "#074463"

        title = Label(self.root,text=" ARYA JAN SEVA KENDRA BILLING-SOFTWARE", bd=10, relief=GROOVE, bg=bg_color, fg="Yellow",font=("time new roman", 30, "bold"), pady=0).pack(fill=X)
        #=============Varibale==========
        #=============B/W Copy==========
        self.Copy=IntVar()
        self.PhotoGrapy=IntVar()
        self.Color=IntVar()
        self.Online=IntVar()
        self.Offline=IntVar()
        self.Scan=IntVar()
        #=============Online Works ===========
        self.Ration_Card=IntVar()
        self.Adhaar_Card=IntVar()
        self.Pan_Card=IntVar()
        self.onprnt_lbl=IntVar()
        self.Adhaar_Money=IntVar()
        self.Mail_lbl=IntVar()
        #==========Total Product & Tax Variable=========
        self.Copy_price=StringVar()
        self.Online_price=StringVar()
        self.Money_Transfer=StringVar()

        self.Copys_Tax=StringVar()
        self.Online_Tax=StringVar()
        self.Money_Transfer_Tax=StringVar()
        
        #============Customer================

        self.c_name=StringVar()
        self.c_phone=StringVar()        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.bill_search=StringVar()

        #===============Customer Detail Frame
        F1=LabelFrame(self.root,text="Customer Detail",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)    
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color, fg="white",font=("time new roman",18,"bold")).grid(row=0,column=0,padx=1,pady=5)
        cname_txt=Entry(F1,width=10,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Mob.No",bg=bg_color, fg="white",font=("time new roman",18,"bold")).grid(row=0,column=2,padx=1,pady=5)
        cphn_txt=Entry(F1,width=10,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill_Number",bg=bg_color, fg="white",font=("time new roman",18,"bold")).grid(row=0,column=4,padx=1,pady=5)
        c_bill_txt=Entry(F1,width=10,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)

        #==============All-Photocopy============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Black-White Copy",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)    
        F2.place(x=5 ,y=180,width=325,height=380)
        
        copy_lbl=Label(F2,text="B/W  copy",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        copy_txt=Entry(F2,width=8,textvariable=self.Copy,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        Hcopy_lbl=Label(F2,text="PhotoGrapy",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Hcopy_txt=Entry(F2,width=8,textvariable=self.PhotoGrapy,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        copy_lbl=Label(F2,text="Color-copy",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=8,textvariable=self.Color,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        onprnt_lbl=Label(F2,text="Online-print",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        onprnt_txt=Entry(F2,width=8,textvariable=self.Online,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        ofprnt_lbl=Label(F2,text="offline-print",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        ofprnt_txt=Entry(F2,width=8,textvariable=self.Offline,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        BooK_lbl=Label(F2,text="Scan Doc",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        BooK_txt=Entry(F2,width=8,textvariable=self.Scan , font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #=============Online Works==============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Online Works",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)    
        F3.place(x=340 ,y=180,width=325,height=380)
        
        copy_lbl=Label(F3,text="Ration Card",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        copy_txt=Entry(F3,width=8,textvariable=self.Ration_Card,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        Hcopy_lbl=Label(F3,text="Adhaar Card",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Hcopy_txt=Entry(F3,width=8, textvariable=self.Adhaar_Card,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        copy_lbl=Label(F3,text="Pan Card",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F3,width=8,textvariable=self.Pan_Card,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        onprnt_lbl=Label(F3,text="I/C/D Certificate",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        onprnt_txt=Entry(F3,width=8,textvariable=self.onprnt_lbl,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Adhr_lbl=Label(F3,text="Adhaar Money",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Adhr_txt=Entry(F3,width=8,textvariable=self.Adhaar_Money,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Mail_lbl=Label(F3,text="Mail Documents",font=("time new roman",16,"bold"),bg=bg_color ,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Mail_txt=Entry(F3,width=8, textvariable=self.Mail_lbl, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============BIll Area================

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=670,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area ",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #==========ButtonFrame============

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)    
        F6.place(x=0,y=560,relwidth=1,height=130)

        m1=Label(F6,text="Total Copy Price",bg=bg_color,fg="red",font=("times new roman ",10,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=12, textvariable=self.Copy_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Online Work Price",bg=bg_color,fg="red",font=("times new roman ",10,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=12,textvariable=self.Online_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

       
        m6=Label(F6,text="Created By:Anshu Gurjar",bg=bg_color,width=22,fg="yellow",font=("times new roman ",10,"bold")).grid(row=2,column=0,padx=4,pady=1,sticky="w")
        # m6_Lable=Entry(F6,width=10,textvariable=self.Money_Transfer,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1) 
        #=================Tax======================

        m3=Label(F6,text="Copys Tax:",bg=bg_color,fg="red",font=("times new roman ",10,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=10,textvariable=self.Copys_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=8,pady=1)

        m4=Label(F6,text="Online Work Tax:",bg=bg_color,fg="red",font=("times new roman ",10,"bold")).grid(row=1,column=2,padx=10,pady=1,sticky="w")
        m4_txt=Entry(F6,width=10,textvariable=self.Online_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)
        
        m7=Label(F6,text="AIMS Industries ",width=15,bg=bg_color,fg="yellow",font=("times new roman ",10,"bold")).grid(row=2,column=2,padx=10,pady=1,sticky="w")
       
        # ====================== Button Frame================

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=570,width=430,height=85)
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="Black",pady=15,bd=5,width=11, font="arial 9 bold").grid(row=0, column=0,padx=5,pady=5)

        Bill_btn=Button(btn_F,command=self.bill_area,text="Genrate Bill",bg="cadetblue",fg="Black",pady=15,bd=5,width=11, font="arial 9 bold").grid(row=0, column=1,padx=5,pady=5)

        Clear_btn=Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="Black",pady=15,bd=5,width=11, font="arial 9 bold").grid(row=0, column=2,padx=5,pady=5)

        Exit_btn=Button(btn_F,command=self.Exit_app, text="Exit",bg="cadetblue",fg="Black",pady=15,bd=5 ,width=11, font="arial 9 bold").grid(row=0, column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_p_p=self.Copy.get()*2
        self.p_g_p=self.PhotoGrapy.get()*30
        self.c_l_p=self.Color.get()*10
        self.o_l_p=self.Online.get()*10
        self.o_f_p=self.Offline.get()*10
        self.s_g_p=self.Scan.get()*10

        self.total_Copy_price=float(
                    self.c_p_p+
                    self.p_g_p+
                    self.c_l_p+
                    self.o_l_p+
                    self.o_f_p+
                    self.s_g_p
                    )

        self.Copy_price.set("Rs."+str(self.total_Copy_price)) 
        self.C_Tax=round((self.total_Copy_price*0.03),2)                    
        self.Copys_Tax.set("Rs."+str(self.C_Tax))

      
        self.o_r_p=self.Ration_Card.get()*100
        self.o_a_p=self.Adhaar_Card.get()*60
        self.o_p_p=self.Pan_Card.get()*200
        self.o_l_p=self.onprnt_lbl.get()*100
        self.o_a_p=self.Adhaar_Money.get()*30
        self.o_m_p=self.Mail_lbl.get()*10 

        self.total_Online_price=float(
                    self.o_r_p+
                    self.o_a_p+
                    self.o_p_p+
                    self.o_l_p+
                    self.o_a_p+
                    self.o_m_p          
                     )       

        self.Online_price.set("Rs."+str(self.total_Online_price))
        self.o_tax=round((self.total_Online_price*0.05),2)
        self.Online_Tax.set("Rs."+str(self.o_tax))

        self.Total_bill=float(self.total_Copy_price+
                             self.total_Online_price+
                             self.C_Tax+
                             self.o_tax

                            )


    def welcome_bill(self):

            #self.txtarea.delete('1.0',End)
            self.txtarea.insert(END,"  **Welcome To Arya Jan Seva Kendra**")
            self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}") 
            self.txtarea.insert(END,f"\n Shop Number: 9891960810,9911614006")
            self.txtarea.insert(END,f"\n Gmail:cscsakipur@gmail.com")           
            self.txtarea.insert(END,f"\n ===================================")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number  : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n=====================================")
            self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
            self.txtarea.insert(END,f"\n=====================================")
            
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Please Enter The Customer Details !")
        elif self.Copy_price.get()=="Rs. 0.0" and self.Online_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Products Purcheased")
        else:                
            self.welcome_bill()
            if self.Copy.get()!=0:
                self.txtarea.insert(END,f"\n Copy \t\t{self.Copy.get()}\t\t{self.c_p_p}")   
            if self.PhotoGrapy.get()!=0:
                self.txtarea.insert(END,f"\n PhotoGrapy \t\t{self.PhotoGrapy.get()}\t\t{self.p_g_p}")    
            if self.Color.get()!=0:
                self.txtarea.insert(END,f"\n Color Copy \t\t{self.Color.get()}\t\t{self.c_l_p}")
            if self.Online.get()!=0:
                self.txtarea.insert(END,f"\n Online Print \t\t{self.Online.get()}\t\t{self.o_l_p}")
            if self.Offline.get()!=0:
                self.txtarea.insert(END,f"\n Offline Print \t\t{self.Offline.get()}\t\t{self.o_f_p}")
            if self.Scan.get()!=0:
                self.txtarea.insert(END,f"\n Scan Docs \t\t{self.Scan.get()}\t\t{self.s_g_p}")
                #=====================Online Works=================
                    
            if self.Ration_Card.get()!=0:    
                self.txtarea.insert(END,f"\n Ration Card \t\t{self.Ration_Card.get()}\t\t{self.o_r_p}")
                
            if self.Adhaar_Card.get()!=0:
                self.txtarea.insert(END,f"\n Adhaar Card \t\t{self.Adhaar_Card.get()}\t\t{self.o_a_p}")
                    
            if self.Pan_Card.get()!=0:
                self.txtarea.insert(END,f"\n Pan Card \t\t{self.Pan_Card.get()}\t\t{self.o_p_p}")
                
            if self.onprnt_lbl.get()!=0:
                self.txtarea.insert(END,f"\n I/C/D Certif \t\t{self.onprnt_lbl.get()}\t\t{self.o_l_p}")
                
            if self.Adhaar_Money.get()!=0:
                self.txtarea.insert(END,f"\n Adhaar Money \t\t{self.Adhaar_Money.get()}\t\t{self.o_a_p}")    
                
            if self.Mail_lbl.get()!=0:
               self.txtarea.insert(END,f"\n Share Docs\t\t{self.Mail_lbl.get()}\t\t{self.o_m_p}") 


               self.txtarea.insert(END,f"\n======================================")
            if self.Copys_Tax.get()!="Rs.0.0":
               self.txtarea.insert(END,f"\n Copy Tax:\t\t\t{self.Copys_Tax.get()}")
            if self.Online_Tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\n Online Works Tax:\t\t\t{self.Online_Tax.get()}") 
               self.txtarea.insert(END,f"\n======================================")
               self.txtarea.insert(END,f"\n Total Bill:\t\t\t{str(self.Total_bill)}") 
               self.txtarea.insert(END,f"\n======================================")
               self.save_Bill()

    def save_Bill(self):
        op=messagebox.askyesno("Save Bill","Do you save The Bill ?")
        if op>0:     
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")  
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved Bill",f"Bill.No :{self.bill_no.get()} Saved Successfully")
                 
        else:
             return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.bill_search.get():       
                 f1=open(f"bills/{i}","r")
                 self.txtarea.delete('1.0',END)
                 for d in f1:                                      
                     self.txtarea.insert(END,d)
                 f1.close()
                 present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill No.")    

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
  #=============B/W Copy==========
            self.Copy.set(0)
            self.PhotoGrapy.set(0)
            self.Color.set(0)
            self.Online.set(0)
            self.Offline.set(0)
            self.Scan.set(0)
            #=============Online Works ===========
            self.Ration_Card.set(0)
            self.Adhaar_Card.set(0)
            self.Pan_Card.set(0)
            self.onprnt_lbl.set(0)
            self.Adhaar_Money.set(0)
            self.Mail_lbl.set(0)
            #==========Total Product & Tax Variable=========
            self.Copy_price.set("")
            self.Online_price.set("")
            self.Money_Transfer.set("")

            self.Copys_Tax.set("")
            self.Online_Tax.set("")
            self.Money_Transfer_Tax.set("")
            
            #============Customer================

            self.c_name.set("")
            self.c_phone.set("")        
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.bill_search.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
