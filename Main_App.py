import tkinter as tk
import tkinter.messagebox
import subprocess
import mysql.connector
from tkinter import *

class FullScreenApp(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.title("School Management System")
        self.master.config(bg="lightblue")

        # Custom close button
        close_button = Button(master, text="X", font=('arial', 12, 'bold'), bg='red', fg='white', command=self.close_program)
        close_button.place(relx=1, x=-2, y=5, anchor=NE)
        border_frame = LabelFrame(master, bg='black', bd=3, relief='ridge')
        border_frame.place(relx=0.5, rely=0.05, relwidth=1, anchor=N)

        # Create the menu content
        self.create_menu()

    def create_menu(self):
        title_Frame = tk.LabelFrame(self.master, font=('arial', 50, 'bold'), width=1000, height=100, bg='lightblue',
                                    relief='raise', bd=13)
        title_Frame.pack(pady=150)

        title_Label = tk.Label(title_Frame, text='School Management System', font=('arial', 30, 'bold'),
                               bg='lightblue')
        title_Label.pack(padx=20)

        # Frames
        Frame_1 = tk.LabelFrame(self.master, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue',
                                 relief='ridge', bd=10)
        Frame_1.pack(padx=280)

        Frame_2 = tk.LabelFrame(self.master, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue',
                                 relief='ridge', bd=10)
        Frame_2.pack(padx=130, pady=7)

        # Labels
        Label_1 = tk.Label(Frame_1, text='STUDENT PROFILE', font=('arial', 25, 'bold'), bg='lightblue')
        Label_1.grid(row=0, column=0, padx=50, pady=5)

        Label_2 = tk.Label(Frame_2, text='FEE REPORT', font=('arial', 25, 'bold'), bg='lightblue')
        Label_2.grid(row=0, column=0, padx=100, pady=5)

        # Buttons
        Button_1 = tk.Button(Frame_1, text='VIEW', font=('arial', 16, 'bold'), width=8, command=self.__information__)
        Button_1.grid(row=0, column=3, padx=50)

        Button_2 = tk.Button(Frame_2, text='VIEW', font=('arial', 16, 'bold'), width=8, command=self.__FeeReport__)
        Button_2.grid(row=0, column=3, padx=50)

    def close_program(self):
        if tkinter.messagebox.askokcancel("Close", "Do you want to close the program?"):
            self.master.destroy()

    def __information__(self):
        file_to_run = "student_info.py"
        subprocess.run(["python", file_to_run])

    def __FeeReport__(self):
        file_to_run = "Fee.py"
        subprocess.run(["python", file_to_run])


class Window_1:
    def __init__(self, master):
        self.master = master

        # Custom close button
        close_button = Button(master, text="X", font=('arial', 12, 'bold'), bg='red', fg='white', command=self.close_window)
        close_button.place(relx=1, x=-2, y=5, anchor=NE)
        border_frame = LabelFrame(master, bg='black', bd=3, relief='ridge')
        border_frame.place(relx=0.5, rely=0.05, relwidth=1, anchor=N)

        self.master.title("School Management System")
        self.master.geometry('1350x750')
        self.master.attributes("-fullscreen", True)  # Open the window in full screen
        self.master.config(bg="lightblue")
        self.Frame = tk.Frame(self.master, bg="lightblue", pady=50)
        self.Frame.pack()

        self.Username = tk.StringVar()
        self.Password = tk.StringVar()

        # Load existing users
        self.load_users()

        self.Lbl_Title = tk.Label(self.Frame, text='Login Menu', font=('arial', 55, 'bold'), bg='lightblue',
                                   fg='Black')
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Login_Frame_1 = tk.LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='lightblue', bd=15,
                                            font=('arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0)
        self.Login_Frame_2 = tk.LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='lightblue', bd=15,
                                            font=('arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=2, column=0)

        # Labels
        self.Label_Username = tk.Label(self.Login_Frame_1, text='Username', font=('arial', 20, 'bold'), bg='lightblue',
                                       bd=20)
        self.Label_Username.grid(row=0, column=0)
        self.text_Username = tk.Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_Username.grid(row=0, column=1, padx=50)

        self.Label_Password = tk.Label(self.Login_Frame_1, text='Password', font=('arial', 20, 'bold'), bg='lightblue',
                                       bd=20)
        self.Label_Password.grid(row=1, column=0)
        self.text_Password = tk.Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), show='*',
                                      textvariable=self.Password)
        self.text_Password.grid(row=1, column=1)

        # Buttons
        self.btnLogin = tk.Button(self.Login_Frame_2, text='Login', width=10, font=('airia', 15, 'bold'),
                                   command=self.login)
        self.btnLogin.grid(row=3, column=0, padx=8, pady=20)

        self.btnReset = tk.Button(self.Login_Frame_2, text='Reset', width=10, font=('airia', 15, 'bold'),
                                  command=self.Reset)
        self.btnReset.grid(row=3, column=1, padx=8, pady=20)

        self.btnExit = tk.Button(self.Login_Frame_2, text='Exit', width=10, font=('airia', 15, 'bold'),
                                 command=self.Exit)
        self.btnExit.grid(row=3, column=2, padx=8, pady=20)

        # Add User button
        self.btnAddUser = tk.Button(self.Login_Frame_2, text='Add User', width=10, font=('airia', 15, 'bold'),
                                    command=self.open_add_user_window)
        self.btnAddUser.grid(row=3, column=3, padx=8, pady=20)

    def load_users(self):
        # Connect to MySQL
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sic mundus",
                database="users"
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT username, Password FROM user_details")
            self.users = self.cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)

    def login(self):
        u = self.Username.get()
        p = self.Password.get()

        for user in self.users:
            if user[0] == u and user[1] == p:
                self.show_menu()
                return

        tk.messagebox.askyesno("Login", "Error : Wrong Password")
        self.Username.set("")
        self.Password.set("")

    def show_menu(self):
        self.master.destroy()
        root = tk.Tk()
        app = FullScreenApp(root)
        root.mainloop()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")

    def Exit(self):
        self.Exit = tk.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def close_window(self):
        if tkinter.messagebox.askokcancel("Close", "Do you want to close the program?"):
            self.master.destroy()

    def open_add_user_window(self):
        self.add_user_window = tk.Toplevel(self.master)
        self.add_user_window.title("Add User")
        self.add_user_window.geometry("400x200")
        self.add_user_window.config(bg="lightblue")

        lbl_username = tk.Label(self.add_user_window, text="Username:", font=('arial', 12, 'bold'), bg='lightblue')
        lbl_username.grid(row=0, column=0, padx=10, pady=10)
        self.new_username = tk.Entry(self.add_user_window, font=('arial', 12))
        self.new_username.grid(row=0, column=1, padx=10, pady=10)

        lbl_password = tk.Label(self.add_user_window, text="Password:", font=('arial', 12, 'bold'), bg='lightblue')
        lbl_password.grid(row=1, column=0, padx=10, pady=10)
        self.new_password = tk.Entry(self.add_user_window, font=('arial', 12), show='*')
        self.new_password.grid(row=1, column=1, padx=10, pady=10)

        btn_add_user = tk.Button(self.add_user_window, text="Add User", font=('arial', 12, 'bold'),
                                 command=self.add_user)
        btn_add_user.grid(row=2, columnspan=2, padx=10, pady=10)

    def add_user(self):
        new_user = (self.new_username.get(), self.new_password.get())
        try:
            self.cursor.execute("INSERT INTO user_details (username, password) VALUES (%s, %s)", new_user)
            self.conn.commit()
            tk.messagebox.showinfo("Success", "New user added successfully!")
            self.load_users()
        except mysql.connector.Error as e:
            print("Error adding user:", e)
            tk.messagebox.showerror("Error", "Failed to add user!")
        finally:
            self.add_user_window.destroy()

def main():
    root = tk.Tk()
    app = Window_1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
