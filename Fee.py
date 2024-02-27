from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import datetime
import os
import sys
from tkinter import filedialog
import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'sic mundus'
MYSQL_DATABASE = 'student_fee'

def connect():
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS fee(
            id INT AUTO_INCREMENT PRIMARY KEY,
            recpt INTEGER,
            name TEXT,
            admsn TEXT,
            date DATE,
            student_class TEXT,
            roll_no TEXT,
            total INTEGER,
            paid INTEGER,
            due INTEGER
        )
    ''')

    con.commit()
    con.close()

def insert(recpt='', name='', admsn='', date='', student_class='', roll_no='', total='', paid='', due=''):
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    cur.execute('''
        INSERT INTO fee (recpt, name, admsn, date, student_class, roll_no, total, paid, due)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (recpt, name, admsn, date, student_class, roll_no, total, paid, due))

    con.commit()
    con.close()

def view():
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    cur.execute('SELECT * FROM fee')
    rows = cur.fetchall()

    con.close()
    return rows

def delete(id):
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    cur.execute('DELETE FROM fee WHERE id = %s', (id,))

    con.commit()
    con.close()

def update(id, recpt='', name='', admsn='', date='', student_class='', roll_no='', total='', paid='', due=''):
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    cur.execute('''
        UPDATE fee 
        SET recpt = %s, name = %s, admsn = %s, date = %s, student_class = %s, roll_no = %s, total = %s, paid = %s, due = %s 
        WHERE id = %s
    ''', (recpt, name, admsn, date, student_class, roll_no, total, paid, due, id))

    con.commit()
    con.close()

def search(recpt='', name='', admsn='', date='', student_class='', roll_no='', total='', paid='', due=''):
    con = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cur = con.cursor()

    # Construct the SQL query dynamically based on the provided search criteria
    sql_query = 'SELECT * FROM fee WHERE 1 = 1'
    sql_params = []

    if recpt:
        sql_query += ' AND recpt = %s'
        sql_params.append(recpt)
    if name:
        sql_query += ' AND name LIKE %s'  # Using LIKE for string comparison
        sql_params.append('%' + name + '%')
    if admsn:
        sql_query += ' AND admsn = %s'
        sql_params.append(admsn)
    if date:
        sql_query += ' AND date = %s'
        sql_params.append(date)
    if student_class:
        sql_query += ' AND student_class = %s'
        sql_params.append(student_class)
    if roll_no:
        sql_query += ' AND roll_no = %s'
        sql_params.append(roll_no)
    if total:
        sql_query += ' AND total = %s'
        sql_params.append(total)
    if paid and paid.strip():  # Check if paid is not empty or contains only whitespace
        try:
            float_paid = float(paid)  # Convert paid to a float
            sql_query += ' AND paid = %s'
            sql_params.append(float_paid)
        except ValueError:
            pass  # If paid cannot be converted to float, ignore it
    if due:
        sql_query += ' AND due = %s'
        sql_params.append(due)

    cur.execute(sql_query, tuple(sql_params))
    rows = cur.fetchall()

    con.close()
    return rows

class Fee:
    def __init__(self, master):
        self.master = master
        self.master.title('School Management System/Fee Report')
        self.master.attributes('-fullscreen', True)  # Open in fullscreen mode
        self.master.config(bg='lightblue')

        # ==================================================Variables=================================================
        self.recpt = StringVar()
        self.name = StringVar()
        self.admsn = StringVar()
        self.date = StringVar()
        self.student_class = StringVar()
        self.roll_no = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()

        # Call the connect function to ensure the database connection is established
        connect()

        # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.student_class_entry.delete(0, END)
                self.student_class_entry.insert(END, st[5])
                self.roll_no_entry.delete(0, END)
                self.roll_no_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        def validate_recpt(new_text):
            if not new_text:
                return True
            return len(new_text) <= 9 and new_text.isdigit()

        def validate_admsn(new_text):
            if not new_text:
                return True
            return len(new_text) <= 9 and new_text.isdigit()

        def Insert():
            if len(self.admsn.get()) != 0:
                formatted_date = datetime.date.today().strftime('%Y-%m-%d')
                insert(
                    recpt=self.recpt.get(),
                    name=self.name.get(),
                    admsn=self.admsn.get(),
                    date=formatted_date,  # Format the date here
                    student_class=self.student_class.get(),
                    roll_no=self.roll_no.get(),
                    total=self.total.get(),
                    paid=self.paid.get(),
                    due=self.due.get()
                )
                View()

        def View():
            self.list.delete(0, END)
            for row in view():
                self.list.insert(END, row)

        def Reset():
           self.recpt.set('')
           self.name.set('')
           self.admsn.set('')
           # self.date.set('')
           self.student_class.set('')
           self.roll_no.set('')
           self.paid.set(0.0)  # Set to 0.0 instead of ''
           self.total.set(0.0)  # Set to 0.0 instead of ''
           self.due.set(0.0)  # Set to 0.0 instead of ''
           self.Display.delete('1.0', END)
           self.list.delete(0, END)


        def Delete():
            delete(st[0])
            Reset()
            View()

        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tReceipt No.\t      :  '   + self.recpt.get() + '\n')
            self.Display.insert(END, '\tStudent Name  :  ' +
                                self.name.get() + '\n')
            self.Display.insert(END, '\tAdmission No.\t:  ' +
                                self.admsn.get() + '\n')
            self.Display.insert(
                END, '\tDate\t          :  ' + self.date.get() + '\n')
            self.Display.insert(
                END, '\tClass\t          :  ' + self.student_class.get() + '\n')
            self.Display.insert(
                END, '\tRoll No. \t          :  '   + self.roll_no.get() + '\n\n')

            x1 = self.total.get()

            x2 = (self.paid.get())
            x3 = (x1 - x2)

            self.Display.insert(END, '\tTotal Amount  :  ' + str(x1) + '\n')
            self.Display.insert(END, '\tPaid Amount   :  ' + str(x2) + '\n')
            self.Display.insert(END, '\tBalance\t         :  ' + str(x3) + '\n')

            self.due.set(x3)
            
        def PrintReceipt():
             receipt_text = self.Display.get('1.0', END)
             if not receipt_text.strip():  # Check if the receipt text is empty or contains only whitespace
                 tkinter.messagebox.showwarning("Warning", "Generate receipt to print")
             else:
                 default_filename = f"{self.name.get()}({self.admsn.get()}).txt"
                 filename = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_filename, filetypes=[("Text files", "*.txt")])
                 if filename:  # If a file name is chosen
                     with open(filename, "w") as file:
                         file.write(receipt_text)



        def Search():
         self.list.delete(0, END)
         rows = search(
             recpt=self.recpt.get(),
             name=self.name.get(),
             admsn=self.admsn.get(),
             date=self.date.get(),
             student_class=self.student_class.get(),
             roll_no=self.roll_no.get(),
             total=self.total.get(),
             paid=self.paid.get(),
             due=self.due.get()
         )
     
         if not rows:
             # Display message if no records are found
             tkinter.messagebox.showinfo("No Record Found", "No record found!")
         else:
             # Populate the list with search results
             for row in rows:
                 self.list.insert(END, row)



        def Update():
            update(
                id=st[0],
                recpt=self.recpt.get(),
                name=self.name.get(),
                admsn=self.admsn.get(),
                date=self.date.get(),
                student_class=self.student_class.get(),
                roll_no=self.roll_no.get(),
                total=self.total.get(),
                paid=self.paid.get(),
                due=self.due.get()
            )
            View()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return

        def back_button_click():
            root.destroy()  # Close the current Tkinter window
            os.system("python Menu.py")
            sys.exit()  # Exit the script

        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='lightblue', padx=80, pady=80)
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='lightblue', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='lightblue', padx=13)
        self.lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='lightblue', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                             bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.recpt_label = Label(Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.admsn_label = Label(Frame_1, text='Admission No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)
        
        self.roll_no_label = Label(Frame_1, text='Roll No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.roll_no_label.grid(row=4, column=0, padx=15, sticky=W)

        self.student_class_label = Label(Frame_1, text='Class : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.student_class_label.grid(row=5, column=0, padx=15, sticky=W)


        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.paid_label.grid(row=3, column=2, padx=5, sticky=W)

        self.due_label = Label(Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.due_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        # self.var_1 = DoubleVar(Frame_1, value='15000')
        d1 = datetime.date.today()
        self.date.set(d1)

        validate_recpt_cmd = (self.master.register(validate_recpt), '%P')
        validate_admsn_cmd = (self.master.register(validate_admsn), '%P')

        self.recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.recpt, validate='key', validatecommand=validate_recpt_cmd)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.admsn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.admsn, validate='key', validatecommand=validate_admsn_cmd)
        self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)


        self.roll_no_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.roll_no, validate='key', validatecommand=validate_admsn_cmd)
        self.roll_no_entry.grid(row=4, column=1, padx=17, pady=5)

        self.student_class_entry = ttk.Combobox(Frame_1, values=('1st', '2nd', '3rd', '4th', '5th', '6th','7th','8th','9th','10th','11th','12th'),
                                         font=('arial', 14), width=19, textvariable=self.student_class)
        self.student_class_entry.grid(row=5, column=1, padx=15, pady=5)
        
        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.total)
        self.total_entry.grid(row=2, column=3, padx=8, pady=5)

        self.paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.paid)
        self.paid_entry.grid(row=3, column=3, pady=5)

        self.due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.due)
        self.due_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)
        
        btnPrint = Button(Button_Frame, text='PRINT RECEIPT', font=(
            'arial', 14, 'bold'), width=12, command=PrintReceipt)
        btnPrint.grid(row=0, column=7, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=8, padx=5, pady=5)

        # Add a back button to the upper left corner
        back_button = Button(self.master, text="Back", font=(
            'arial', 14, 'bold'), width=10, command=back_button_click)
        back_button.place(x=20, y=20)

        self.master.mainloop()


root = Tk()
application = Fee(root)
