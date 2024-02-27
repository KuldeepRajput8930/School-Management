import tkinter as tk
from tkinter import *
import tkinter.messagebox
import mysql.connector
from tkinter import ttk
from datetime import datetime

class Std_info_BackEnd:

    @staticmethod
    def insert(name="", fname="", mname="", address="", mobno="", email="", dob="", gender="", admission_no="", roll_no=""):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sic mundus",
            database="student_info"
        )
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fname VARCHAR(255), mname VARCHAR(255), \
                     address TEXT, mobno VARCHAR(15), email VARCHAR(255), dob DATE, gender VARCHAR(10), admission_no VARCHAR(20), roll_no VARCHAR(20))")

        sql = "INSERT INTO student (name, fname, mname, address, mobno, email, dob, gender, admission_no, roll_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, fname, mname, address, mobno, email, dob, gender, admission_no, roll_no)
        cur.execute(sql, val)

        conn.commit()
        conn.close()

    @staticmethod
    def view():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sic mundus",
            database="student_info"
        )
        cur = conn.cursor()

        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        conn.close()
        return rows

    @staticmethod
    def delete(id):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sic mundus",
            database="student_info"
        )
        cur = conn.cursor()

        sql = "DELETE FROM student WHERE id = %s"
        val = (id,)
        cur.execute(sql, val)

        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name="", fname="", mname="", address="", mobno="", email="", dob="", gender="", admission_no="", roll_no=""):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sic mundus",
            database="student_info"
        )
        cur = conn.cursor()

        sql = "UPDATE student SET name = %s, fname = %s, mname = %s, address = %s, mobno = %s, email = %s, dob = %s, gender = %s, admission_no = %s, roll_no = %s WHERE id = %s"
        val = (name, fname, mname, address, mobno, email, dob, gender, admission_no, roll_no, id)
        cur.execute(sql, val)

        conn.commit()
        conn.close()

    @staticmethod
    def search(name="", fname="", mname="", address="", mobno="", email="", dob="", gender="", admission_no="", roll_no=""):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sic mundus",
            database="student_info"
        )
        cur = conn.cursor()

        sql = "SELECT * FROM student WHERE name = %s OR fname = %s OR mname = %s OR address = %s OR mobno = %s OR email = %s OR dob = %s OR gender = %s OR admission_no = %s OR roll_no = %s"
        val = (name, fname, mname, address, mobno, email, dob, gender, admission_no, roll_no)
        cur.execute(sql, val)
        rows = cur.fetchall()

        conn.close()
        return rows

class Std_info():
    def __init__(self, master):
        self.master = master
        self.master.title('School Management System/Student Information')
        self.master.config(bg='lightblue')
        
        self.Frame_3 = LabelFrame(master, width=1200, height=100, font=('arial', 10, 'bold'),
                                   bg='lightblue', relief='ridge', bd=13)
        self.Frame_3.grid(row=2, column=0, pady=10)
        # self.create_buttons()
        
        def toggle_fullscreen(event=None):
            self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen"))

        self.master.bind("<F11>", toggle_fullscreen)
        self.master.bind("<Escape>", toggle_fullscreen)

        toggle_fullscreen()

        def on_close():
            if tkinter.messagebox.askokcancel("Close", "Do you want to close the program?"):
                master.destroy()

        close_button = Button(master, text="X", font=('arial', 12, 'bold'), bg='red', fg='white', command=on_close)
        close_button.place(relx=1, x=-2, y=5, anchor=NE)
        border_frame = LabelFrame(master, bg='black', bd=3, relief='ridge')
        border_frame.place(relx=0.5, rely=0.05, relwidth=1, anchor=N)

        self.name = StringVar()
        self.fname = StringVar()
        self.mname = StringVar()
        self.address = StringVar()
        self.mobno = StringVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.gender = StringVar()
        self.admission_no = StringVar()
        self.roll_no = StringVar()

        self.Main_Frame = LabelFrame(self.master, width=1300, height=500, font=('arial', 20, 'bold'),
                                     bg='lightblue', bd=15, relief='ridge')
        self.Main_Frame.grid(row=0, column=0, padx=105, pady=100)

        self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=400, font=('arial', 15, 'bold'),
                                   relief='ridge', bd=10, bg='lightblue', text='STUDENT INFORMATION ')
        self.Frame_1.grid(row=1, column=0, padx=10)

        self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=400, font=('arial', 15, 'bold'),
                                   relief='ridge', bd=10, bg='lightblue', text='STUDENT DATABASE')
        self.Frame_2.grid(row=1, column=1, padx=5)

        self.Frame_3 = LabelFrame(self.master, width=1200, height=100, font=('arial', 10, 'bold'),
                                   bg='lightblue', relief='ridge', bd=13)
        self.Frame_3.grid(row=2, column=0, pady=10)

        self.Label_name = Label(self.Frame_1, text='Name', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_name.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Label_fname = Label(self.Frame_1, text='Father Name', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_fname.grid(row=1, column=0, sticky=W, padx=20)
        self.Label_mname = Label(self.Frame_1, text='Mother Name', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_mname.grid(row=2, column=0, sticky=W, padx=20)
        self.Label_address = Label(self.Frame_1, text='Address', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_address.grid(row=3, column=0, sticky=W, padx=20)
        self.Label_mobno = Label(self.Frame_1, text='Mobile Number', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_mobno.grid(row=4, column=0, sticky=W, padx=20)
        self.Label_emailID = Label(self.Frame_1, text='Email ID', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_emailID.grid(row=5, column=0, sticky=W, padx=20)
        self.Label_dob = Label(self.Frame_1, text='Date of Birth', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_dob.grid(row=6, column=0, sticky=W, padx=20)
        self.Label_gender = Label(self.Frame_1, text='Gender', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_gender.grid(row=7, column=0, sticky=W, padx=20, pady=10)
        self.Label_admission_no = Label(self.Frame_1, text='Admission No.', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_admission_no.grid(row=8, column=0, sticky=W, padx=20, pady=10)
        self.Label_roll_no = Label(self.Frame_1, text='Roll No.', font=('arial', 20, 'bold'), bg='lightblue')
        self.Label_roll_no.grid(row=9, column=0, sticky=W, padx=20, pady=10)

        self.Entry_name = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.name)
        self.Entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.Entry_fname = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.fname)
        self.Entry_fname.grid(row=1, column=1, padx=10, pady=5)
        self.Entry_mname = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.mname)
        self.Entry_mname.grid(row=2, column=1, padx=10, pady=5)
        self.Entry_address = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.address)
        self.Entry_address.grid(row=3, column=1, padx=10, pady=5)
        self.Entry_mobno = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.mobno)
        self.Entry_mobno.grid(row=4, column=1, padx=10, pady=5)
        self.Entry_emailID = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.email)
        self.Entry_emailID.grid(row=5, column=1, padx=10, pady=5)
        self.Entry_dob = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.dob)
        self.Entry_dob.grid(row=6, column=1, padx=10, pady=5)
        self.Entry_gender = ttk.Combobox(self.Frame_1, values=(' ', 'Male', 'Female', 'Others'),
                                         font=('arial', 17, 'bold'), textvariable=self.gender, width=19)
        self.Entry_gender.grid(row=7, column=1, padx=10, pady=5)
        self.Entry_admission_no = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.admission_no)
        self.Entry_admission_no.grid(row=8, column=1, padx=10, pady=5)
        self.Entry_roll_no = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.roll_no)
        self.Entry_roll_no.grid(row=9, column=1, padx=10, pady=5)

        self.btnSave = Button(self.Frame_3, text='SAVE', font=('arial', 17, 'bold'), width=8, command=self.Add)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnDisplay = Button(self.Frame_3, text='DISPLAY', font=('arial', 17, 'bold'), width=8, command=self.Display)
        self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)
        self.btnReset = Button(self.Frame_3, text='RESET', font=('arial', 17, 'bold'), width=8, command=self.Reset)
        self.btnReset.grid(row=0, column=2, padx=10, pady=10)
        self.btnUpdate = Button(self.Frame_3, text='UPDATE', font=('arial', 17, 'bold'), width=8, command=self.Update)
        self.btnUpdate.grid(row=0, column=3, padx=10, pady=10)
        self.btnDelete = Button(self.Frame_3, text='DELETE', font=('arial', 17, 'bold'), width=8, command=self.Delete)
        self.btnDelete.grid(row=0, column=4, padx=10, pady=10)
        self.btnSearch = Button(self.Frame_3, text='SEARCH', font=('arial', 17, 'bold'), width=8, command=self.Search)
        self.btnSearch.grid(row=0, column=5, padx=10, pady=10)
        self.btnExit = Button(self.Frame_3, text='EXIT', font=('arial', 17, 'bold'), width=8, command=on_close)
        self.btnExit.grid(row=0, column=6, padx=10, pady=10)
        
        self.btnShowInfo = Button(self.Frame_3, text='Show Info', font=('arial', 17, 'bold'), width=8, command=self.show_info_window)
        self.btnShowInfo.grid(row=0, column=7, padx=10, pady=10)
        

        self.scrollbar = Scrollbar(self.Frame_2)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.listbox = Listbox(self.Frame_2, width=75, height=20, font=('arial', 12, 'bold'))
        self.listbox.bind('<<ListboxSelect>>', self.StudentRec)
        self.listbox.grid(row=0, column=0)
        self.scrollbar.config(command=self.listbox.yview)

    def Add(self):
        if len(self.name.get()) != 0:
            try:
                dob = datetime.strptime(self.dob.get(), '%d/%m/%Y').strftime('%Y-%m-%d')
                Std_info_BackEnd.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(),
                                        self.mobno.get(), self.email.get(), dob, self.gender.get(), self.admission_no.get(), self.roll_no.get())
                self.Display()
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Invalid date format. Please use DD/MM/YYYY.")
                self.Display()

    def Display(self):
        self.listbox.delete(0, END)
        for row in Std_info_BackEnd.view():
            self.listbox.insert(END, row)

    def Reset(self):
        self.name.set('')
        self.fname.set('')
        self.mname.set('')
        self.address.set('')
        self.mobno.set('')
        self.email.set('')
        self.dob.set('')
        self.gender.set('')
        self.admission_no.set('')
        self.roll_no.set('')
        self.listbox.delete(0, END)

    def Delete(self):
        if (len(self.name.get()) != 0):
            Std_info_BackEnd.delete(selected_tuple[0])
            self.Reset()
            self.Display()

    def Search(self):
         self.listbox.delete(0, END)
         dob = self.dob.get()
         if dob:
             try:
                 dob = datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
             except ValueError:
                 tkinter.messagebox.showinfo("Error", "Invalid date format. Please use DD/MM/YYYY.")
                 return
         else:
             dob = None  # Set dob to None if it's empty
         for row in Std_info_BackEnd.search(self.name.get(), self.fname.get(), self.mname.get(),
                                            self.address.get(), self.mobno.get(), self.email.get(), dob,
                                            self.gender.get(), self.admission_no.get(), self.roll_no.get()):
             self.listbox.insert(END, row)

    def Update(self):
        if (len(self.name.get()) != 0):
            
            try:
                dob = datetime.strptime(self.dob.get(), '%d/%m/%Y').strftime('%Y-%m-%d')
                Std_info_BackEnd.update(selected_tuple[0], self.name.get(), self.fname.get(), self.mname.get(),
                                    self.address.get(), self.mobno.get(), self.email.get(),dob,
                                    self.gender.get(), self.admission_no.get(), self.roll_no.get())
                self.Display()
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Invalid date format. Please use DD/MM/YYYY.")
                self.Display()

    def StudentRec(self, event):
        try:
            global selected_tuple
            index = self.listbox.curselection()[0]
            selected_tuple = self.listbox.get(index)

            self.Entry_name.delete(0, END)
            self.Entry_name.insert(END, selected_tuple[1])
            self.Entry_fname.delete(0, END)
            self.Entry_fname.insert(END, selected_tuple[2])
            self.Entry_mname.delete(0, END)
            self.Entry_mname.insert(END, selected_tuple[3])
            self.Entry_address.delete(0, END)
            self.Entry_address.insert(END, selected_tuple[4])
            self.Entry_mobno.delete(0, END)
            self.Entry_mobno.insert(END, selected_tuple[5])
            self.Entry_emailID.delete(0, END)
            self.Entry_emailID.insert(END, selected_tuple[6])
            self.Entry_dob.delete(0, END)
            self.Entry_dob.insert(END, selected_tuple[7])
            self.Entry_gender.delete(0, END)
            self.Entry_gender.insert(END, selected_tuple[8])
            self.Entry_admission_no.delete(0, END)
            self.Entry_admission_no.insert(END, selected_tuple[9])
            self.Entry_roll_no.delete(0, END)
            self.Entry_roll_no.insert(END, selected_tuple[10])
        except IndexError:
            pass
         
    
    def show_info_window(self):
        # Function to display individual record details in a separate window
        info_window = Toplevel(self.master)
        info_window.title("Record Details")
        info_window.geometry("400x300")

        # Get the selected record details
        selected_record = self.listbox.get(self.listbox.curselection())

        # Display record details in labels
        Label(info_window, text="Name: " + selected_record[1]).pack()
        Label(info_window, text="Father's Name: " + selected_record[2]).pack()
        Label(info_window, text="Mother's Name: " + selected_record[3]).pack()
        Label(info_window, text="Address: " + selected_record[4]).pack()
        Label(info_window, text="Mobile Number: " + selected_record[5]).pack()
        Label(info_window, text="Email ID: " + selected_record[6]).pack()
        Label(info_window, text="Date of Birth: " + selected_record[7]).pack()
        Label(info_window, text="Gender: " + selected_record[8]).pack()
        Label(info_window, text="Admission No.: " + selected_record[9]).pack()
        Label(info_window, text="Roll No.: " + selected_record[10]).pack()

root = Tk()
obj = Std_info(root)
root.mainloop()
