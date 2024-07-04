from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
# import rows as rows


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('HOSPITAL MANAGEMENT SYSTEM')
        root.resizable(False, False)
        #============== Color Tag===============
        bg_color = "white"
        font_color="black"

#==============================Variable Frame=====================================
        self.name_of_tab=StringVar()
        self.ref_no=StringVar()
        self.dose_no=StringVar()
        self.no_tab=StringVar()
        self.lot=StringVar()
        self.issue_date=StringVar()
        self.expiry_date=StringVar()
        self.daily_dos=StringVar()
        self.side_effect=StringVar()
        self.further_info=StringVar()
        self.blood_group=StringVar()
        self.blood_pressure=StringVar()
        self.storage_advice=StringVar()
        self.medication=StringVar()
        self.patient_id=StringVar()
        self.NHS_no=StringVar()
        self.patient_name=StringVar()
        self.patient_cnic=StringVar()
        self.date_of_birth=StringVar()
        self.patient_address=StringVar()

        # ===============Title===============
        title = Label(self.root, text="+ HOSPITAL MANAGEMENT SYSTEM", bd=10, relief=GROOVE, bg=bg_color,fg='red', font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #====================== Data Form========================
        data_frame = Label(self.root, relief=RIDGE, bg="white",)
        data_frame.place(x=0, y=65, width=1350, height=400)
                    # ====================== Data Left Form========================
        data_frame_left = LabelFrame(data_frame, relief=GROOVE, text="Patient Information", fg='green',bg=bg_color,font=("times new roman", 12, "bold"), bd=10)
        data_frame_left.place(x=5, y=5, width=800, height=380)

        #================== Tablet Name==================
        tab_name = Label(data_frame_left, text="Name Of Tablet :",  font=("times new roman", 12, "bold"),bg=bg_color,fg=font_color,padx=2,pady=6).grid(row=0, column=0,)
        tab_combo=ttk.Combobox(data_frame_left,textvariable=self.name_of_tab,font=("times new roman", 12, "bold"),width=25 )
        tab_combo["values"]=("alendronate tablet","acyclovir capsule","acyclovir tablet	","albuterol inhalation solution","albuterol sulfate")
        tab_combo.grid(row=0, column=1)

        refrence_no = Label(data_frame_left, text="Reference No :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=1, column=0, sticky=W)
        refrence_no_entry = ttk.Entry(data_frame_left,textvariable=self.ref_no, width=24 ,font=("arial", 12),).grid(row=1,column=1, padx=5,pady=5,sticky=W)

        dose_no = Label(data_frame_left, text="Dose Number :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=2, column=0, sticky=W)
        dose_no_entry = ttk.Entry(data_frame_left,textvariable=self.dose_no, width=24 ,font=("arial", 12),).grid(row=2,column=1, padx=5,pady=5,sticky=W)

        no_tab = Label(data_frame_left, text="No of Tablet :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=3, column=0, sticky=W)
        no_tab_entry = ttk.Entry(data_frame_left,textvariable=self.no_tab, width=24 ,font=("arial", 12),).grid(row=3,column=1, padx=5,pady=5,sticky=W)

        lot = Label(data_frame_left, text="Lot :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=4, column=0, sticky=W)
        lot_entry = ttk.Entry(data_frame_left,textvariable=self.lot, width=24 ,font=("arial", 12),).grid(row=4,column=1, padx=5,pady=5,sticky=W)

        issue_date = Label(data_frame_left, text="Issue Date :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=5, column=0, sticky=W)
        issue_date_entry = ttk.Entry(data_frame_left,textvariable=self.issue_date, width=24 ,font=("arial", 12),).grid(row=5,column=1, padx=5,pady=5,sticky=W)

        exp_date = Label(data_frame_left, text="Exp Date :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=6, column=0, sticky=W)
        exp_date_entry = ttk.Entry(data_frame_left,textvariable=self.expiry_date, width=24 ,font=("arial", 12),).grid(row=6,column=1, padx=5,pady=5,sticky=W)

        daily_dose = Label(data_frame_left, text="Daily Dose :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=7, column=0, sticky=W)
        daily_dose_entry = ttk.Entry(data_frame_left,textvariable=self.daily_dos, width=24 ,font=("arial", 12),).grid(row=7,column=1, padx=5,pady=5,sticky=W)

        side_effect = Label(data_frame_left, text="Side Effect :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=8, column=0, sticky=W)
        side_effect_entry = ttk.Entry(data_frame_left,textvariable=self.side_effect, width=24 ,font=("arial", 12),).grid(row=8,column=1, padx=5,pady=5,sticky=W)

        furder_info = Label(data_frame_left, text="Further Info :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=9, column=0, sticky=W)
        furder_info_entry = ttk.Entry(data_frame_left,textvariable=self.further_info, width=24 ,font=("arial", 12),).grid(row=9,column=1, padx=5,pady=5,sticky=W)


        blood_group = Label(data_frame_left, text="Blood Group :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=0, column=2, sticky=W)
        blood_group_combo = ttk.Combobox(data_frame_left,textvariable=self.blood_group, font=("times new roman", 12, "bold"), width=25)
        blood_group_combo["values"] = ( "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        blood_group_combo.grid(row=0, column=3)

        blood_pressure = Label(data_frame_left, text="Blood Pressure :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=1, column=2, sticky=W)
        blood_pressure_entry = ttk.Entry(data_frame_left,textvariable=self.blood_pressure, width=24 ,font=("arial", 12),).grid(row=1,column=3, padx=5,pady=5,sticky=W)

        storage_advice = Label(data_frame_left, text="Storage Advice :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=2, column=2, sticky=W)
        storage_advice_entry = ttk.Entry(data_frame_left,textvariable=self.storage_advice, width=24 ,font=("arial", 12),).grid(row=2,column=3, padx=5,pady=5,sticky=W)

        madication = Label(data_frame_left, text="Madication :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=3, column=2, sticky=W)
        madication_entry = ttk.Entry(data_frame_left,textvariable=self.medication, width=24 ,font=("arial", 12),).grid(row=3,column=3, padx=5,pady=5,sticky=W)

        patient_ID = Label(data_frame_left, text="Patient ID :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=4, column=2, sticky=W)
        patient_ID_entry = ttk.Entry(data_frame_left,textvariable=self.patient_id, width=24 ,font=("arial", 12),).grid(row=4,column=3, padx=5,pady=5,sticky=W)

        NHS_no = Label(data_frame_left, text="NHS Number :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=5, column=2, sticky=W)
        NHS_no_entry = ttk.Entry(data_frame_left,textvariable=self.NHS_no, width=24 ,font=("arial", 12),).grid(row=5,column=3, padx=5,pady=5,sticky=W)

        patient_name = Label(data_frame_left, text="Patient Name :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=6, column=2, sticky=W)
        patient_name_entry = ttk.Entry(data_frame_left,textvariable=self.patient_name, width=24 ,font=("arial", 12),).grid(row=6,column=3, padx=5,pady=5,sticky=W)

        patient_cnic = Label(data_frame_left, text="Patient CNIC No :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=7, column=2, sticky=W)
        patient_cnic_entry = ttk.Entry(data_frame_left,textvariable=self.patient_cnic, width=24 ,font=("arial", 12),).grid(row=7,column=3, padx=5,pady=5,sticky=W)


        date_of_birt = Label(data_frame_left, text="Date of Birth :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=8, column=2, sticky=W)
        date_of_birt_entry = ttk.Entry(data_frame_left,textvariable=self.date_of_birth, width=24 ,font=("arial", 12),).grid(row=8,column=3, padx=5,pady=5,sticky=W)

        address = Label(data_frame_left, text="Patient Address :",bg=bg_color,font=("arial", 12, "bold"), fg=font_color, padx=2,pady=5).grid(row=9, column=2, sticky=W)
        address_entry = ttk.Entry(data_frame_left,textvariable=self.patient_address, width=24 ,font=("arial", 12),).grid(row=9,column=3, padx=5,pady=5,sticky=W)
                    # ====================== Data Right Form========================
        data_frame_right = LabelFrame(data_frame, relief=GROOVE, text="Precscription", fg='green',bg=bg_color,
                                                font=("times new roman", 12, "bold"), bd=10)
        data_frame_right.place(x=820, y=5, width=520, height=380)

        title = Label(data_frame_right, text="Patient Detail", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(data_frame_right, orient=VERTICAL)
        scroll_x = ttk.Scrollbar(data_frame_right, orient=HORIZONTAL)
        self.textarea = Text(data_frame_right, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scrol_y.config(command=self.textarea.yview)
        scroll_x.config(command=self.textarea.xview)
        self.textarea.pack(fill=BOTH, expand=1)

        #===============================Button Frame===============================

 #=================Button Farame===============
        button_frame=Frame(self.root,bd=10,relief=GROOVE,bg="White")
        button_frame.place(x=0,y=470,width=1350,height=60)
        #================== precscription Button==================
        precscription_btn=Button(button_frame,text="Precscription",command=self.add_date,font=("arial", 12, "bold"),width=21,bg="green",fg="white", bd=5, relief=RIDGE,).grid(row=0,column=0,)
        # ================== Clear Button==================
        precscription_date_btn = Button(button_frame, text="Precscription Date", font=("arial", 12, "bold"), width=21, bg="green", fg="white",bd=5, relief=RIDGE, ).grid(row=0, column=1, )
        #================== Update Button==================
        update_btn=Button(button_frame,text="Update",font=("arial", 12, "bold"),width=21,bg="green",fg="white", bd=5, relief=RIDGE,).grid(row=0,column=2,)
        #================== Delete Button==================
        delete_btn=Button(button_frame,text="Delete",font=("arial", 12, "bold"),width=20,bg="blue",fg="white", bd=5, relief=RIDGE,).grid(row=0,column=3,)
        #================== Clear Button==================
        clear_btn=Button(button_frame,text="Clear",font=("arial", 12, "bold"),width=20,bg="blue",fg="white", bd=5, relief=RIDGE,).grid(row=0,column=4,)
        # ================== Exit Button==================
        exit_btn = Button(button_frame, text="Exit", font=("arial", 12, "bold"), width=20, bg="red", fg="white",bd=5, relief=RIDGE, ).grid(row=0, column=5,)

 #=================Details Farame===============
        detail_frame=Frame(self.root,bd=10,relief=GROOVE,bg="White")
        detail_frame.place(x=0,y=530,width=1350,height=150)
        # ===============Scrol Bar=====================
        scroll_x = ttk.Scrollbar(detail_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_frame, orient=VERTICAL)

        self.patient_data_table = ttk.Treeview(detail_frame, column=( "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15","16","17","18","19","20"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.patient_data_table.xview)
        scroll_y.config(command=self.patient_data_table.yview)

        self.patient_data_table.heading('1', text="Name Of Tablet")
        self.patient_data_table.heading('2', text="Reference No")
        self.patient_data_table.heading('3', text="Dose Number")
        self.patient_data_table.heading('4', text="No Of Tablet")
        self.patient_data_table.heading('5', text="Lot")
        self.patient_data_table.heading('6', text="Issue Date")
        self.patient_data_table.heading('7', text="Expiry Date")
        self.patient_data_table.heading('8', text="Daily Dose")
        self.patient_data_table.heading('9', text="Side Effect")
        self.patient_data_table.heading('10', text="Further Information")
        self.patient_data_table.heading('11', text="Blood Group")
        self.patient_data_table.heading('12', text="Blood Pressure")
        self.patient_data_table.heading('13', text="Storage Advice")
        self.patient_data_table.heading('14', text="Maication")
        self.patient_data_table.heading('15', text="Patient ID")
        self.patient_data_table.heading('16', text="NHS Number")
        self.patient_data_table.heading('17', text="Patient Name")
        self.patient_data_table.heading('18', text="Patient CNIC No")
        self.patient_data_table.heading('19', text="Date Of Birth")
        self.patient_data_table.heading('20', text="Patient address")

        self.patient_data_table['show'] = 'headings'

        self.patient_data_table.column("1", width=200)
        self.patient_data_table.column("2", width=150)
        self.patient_data_table.column("3", width=150)
        self.patient_data_table.column("4", width=150)
        self.patient_data_table.column("5", width=150)
        self.patient_data_table.column("6", width=150)
        self.patient_data_table.column("7", width=150)
        self.patient_data_table.column("8", width=150)
        self.patient_data_table.column("9", width=150)
        self.patient_data_table.column("10", width=300)
        self.patient_data_table.column("11", width=150)
        self.patient_data_table.column("12", width=150)
        self.patient_data_table.column("13", width=150)
        self.patient_data_table.column("14", width=150)
        self.patient_data_table.column("15", width=150)
        self.patient_data_table.column("16", width=150)
        self.patient_data_table.column("17", width=200)
        self.patient_data_table.column("18", width=200)
        self.patient_data_table.column("19", width=150)
        self.patient_data_table.column("20", width=300)

        self.patient_data_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        # ==================== Coppy Right Frame================
        LabelFrame(self.root, text="Designe By Muhammad Salman @ Copyright by graphictech", font="arial 8 bold",
                   bg="White", fg="black", borderwidth=0, labelanchor=S, ).place(x=0, y=680, relwidth=1, height=15)

#=========================== Functions===============================
    def add_date(self):
        if self.name_of_tab.get()=="" or self.ref_no.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host='localhost', username='root', password='Sallu410802',database='hospital_management')
                my_cursor = connection.cursor()
                my_cursor.execute('insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                                self.name_of_tab.get(),
                                                                                                                self.ref_no.get(),
                                                                                                                self.dose_no.get(),
                                                                                                                self.no_tab.get(),
                                                                                                                self.lot.get(),
                                                                                                                self.issue_date.get(),
                                                                                                                self.expiry_date.get(),
                                                                                                                self.daily_dos.get(),
                                                                                                                self.side_effect.get(),
                                                                                                                self.further_info.get(),
                                                                                                                self.blood_group.get(),
                                                                                                                self.blood_pressure.get(),
                                                                                                                self.storage_advice.get(),
                                                                                                                self.medication.get(),
                                                                                                                self.patient_id.get(),
                                                                                                                self.NHS_no.get(),
                                                                                                                self.patient_name.get(),
                                                                                                                self.patient_cnic.get(),
                                                                                                                self.date_of_birth.get(),
                                                                                                                self.patient_address.get()



                                                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success', 'Record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')

    def fetch_data(self):
        connection = mysql.connector.connect(host='localhost', username='root', password='Sallu410802',database='hospital_management')
        my_cursor = connection.cursor()
        my_cursor.execute('select * from hospital')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_data_table.delete(*self.patient_data_table.get_children())
            for i in data:
                self.patient_data_table("",END,values=i)
            connection.commit()
        connection.close()
if __name__ == '__main__':
    root = Tk()
    obj = Hospital(root)
    root.mainloop()