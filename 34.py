from tkinter import *
from tkinter import ttk

import sqlite3


class Registration:
    def __init__(self, root, ls, frame_old2):
        self.frame_old2 = frame_old2
        self.root = root
        self.ls = ls

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Student Management System', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Assigning the variables.
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Phone_var = StringVar()
        self.DOB_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Creating a Left-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*20//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)

        # Labeling a manage frame.
        m_title = Label(Manage_Frame, text="Manage Students", bg="lightpink", fg="blue",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Create a roll Number, name, email, and all things like form.
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, width=15, textvariable=self.Gender_var, font=("times new roman", 12),
                                    state="readonly")
        combo_Gender['values'] = ("Male", "Female", "Others")
        combo_Gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_Phone = Label(Manage_Frame, text="Phone", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Phone = Entry(Manage_Frame, textvariable=self.Phone_var, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_Phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.DOB_var, font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address",bg="LightBlue", fg="RED",
                            font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Creating a second frame.
        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        btn_frame.place(x=ls[0]*15//1336, y=ls[1]*500//714, width=ls[0]*420//1336)

        Addbtn = Button(btn_frame, text="ADD",bg='black',fg='white', width=10, command=self.add_data).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_frame, text="UPDATE",bg='black',fg='white', width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="DELETE",bg='black',fg='white', width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="CLEAR",bg='black',fg='white', width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
        Detail_Frame.place(x=ls[0]*490//1336, y=ls[1]*100//714, width=ls[0]*830//1336, height=ls[1]*580//714)

        lbl_search = Label(Detail_Frame, text="Search By", bg="cornsilk", fg="blue",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.search_by, font=("times new roman", 12, "bold"), state="readonly")
        combo_search['values'] = ("Name", "Roll_No", "Phone")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, width=20, textvariable=self.search_txt, font=("times new roman", 12, "bold"), bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Detail_Frame, text="Search", command=self.search_data, width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Detail_Frame, text="Show All", command=self.fetch, width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        Table_Frame.place(x=ls[0]*10//1336, y=ls[1]*70//714, width=ls[0]*760//1336, height=ls[1]*500//714)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                     columns=("Roll", "Name", "Email", "Gender", "Phone", "DOB", "Address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll", text="Roll NO.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Phone", text="Phone")
        self.Student_table.heading("DOB", text="DOB")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Phone", width=100)
        self.Student_table.column("DOB", width=100)
        self.Student_table.column("Address", width=200)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()
        pass

    def add_data(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("INSERT INTO student_data VALUES (?,?,?,?,?,?,?)",(self.Roll_No_var.get(),
                                                                 self.Name_var.get(),
                                                                 self.Email_var.get(),
                                                                 self.Gender_var.get(),
                                                                 self.Phone_var.get(),
                                                                 self.DOB_var.get(),
                                                                 self.txt_address.get('1.0',END)
                                                                 ))

        c.execute("INSERT INTO student_fees VALUES (?,?,?)", (self.Roll_No_var.get(), '0', '0'))
        c.execute("INSERT INTO student_attendance VALUES (?,?,?)", (self.Roll_No_var.get(), '0', '0'))
        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def fetch(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_data")
        rows = c.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Phone_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("UPDATE student_data SET name='{}', email='{}', gender='{}', phone='{}', DOB='{}', Address='{}' where Roll_no= {}"
                    .format(self.Name_var.get(),
                            self.Email_var.get(),
                            self.Gender_var.get(),
                            self.Phone_var.get(),
                            self.DOB_var.get(),
                            self.txt_address.get("1.0", END),
                            self.Roll_No_var.get()
        ))

        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM student_data where Roll_No = "+ self.Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch()
        self.clear()

    def search_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where " + str(self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Gender_var.set("")
        self.DOB_var.set("")
        self.txt_address.delete("1.0", END)
        self.Email_var.set("")
        self.Name_var.set("")
        self.Phone_var.set("")

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old2.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import ttk

import GeneratorMarksheet
import GeneratorAttendance
import GeneratorFees


class Student_Menu:
    def __init__(self, root, ls, frame_old, frame_run, roll):
        # Creating the first frame.
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.frame_run = frame_run
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Labeling the page.
        self.title = Label(self.frame, text='Nirma University', font=('Algerian', 25, 'bold'), bg="#163148", fg="#ffffff").pack(
            side=TOP)

        # Creating a second frame.
        self.frame2 = Frame(self.frame, bg='#ffffff')
        self.frame2.place(x=ls[0]//9, y=ls[1]//8, width=ls[0]//9*7, height=ls[1]//8*6)

        # Title for Register/Login.
        self.title1 = Label(self.frame2, text='student management system', font=('Algerian', 22, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Taking All pics in the variable.
        self.photo_ID_Card = PhotoImage(file=r"Images/IDCard.png")
        self.photo_attendance = PhotoImage(file=r"Images/attendance.png")
        self.photo_marksheet = PhotoImage(file=r"Images/marksheet.png")
        self.photo_fees = PhotoImage(file=r"Images/fees.png")
        self.photo_exit = PhotoImage(file=r"Images/exit.png")

        # Resizing the Images as per requirement.
        self.photo_ID_Card = self.photo_ID_Card.subsample(11, 11)
        self.photo_attendance = self.photo_attendance.subsample(5, 5)
        self.photo_marksheet = self.photo_marksheet.subsample(5, 5)
        self.photo_fees = self.photo_fees.subsample(5, 5)
        self.photo_exit = self.photo_exit.subsample(5, 5)

        # Creating a Button Images.
        self.ID_card = Button(self.frame2, text='Generate ID Card', bd=0, bg='#fbf8e6', image=self.photo_ID_Card, compound=TOP, command=self.IDGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1]//6+10, x=ls[0]//9, y=ls[1] // 6)

        self.attendance = Button(self.frame2, text='Show Attendance', bd=0, bg='#fbf8e6', image=self.photo_attendance,
                              compound=TOP, command=self.AttendanceGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9*3, y=ls[1] // 6)

        self.marksheet = Button(self.frame2, text='Show Marksheet', bd=0, bg='#fbf8e6', image=self.photo_marksheet,
                                 compound=TOP, command=self.MarksheetGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 5, y=ls[1] // 6)

        self.fees_btn = Button(self.frame2, text='Fee Status', bd=0, bg='#fbf8e6', image=self.photo_fees,
                                 compound=TOP, command=self.FeesGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 2, y=ls[1] // 6*3)

        self.Exit_btn = Button(self.frame2, text='Exit', bd=0, bg='#fbf8e6', image=self.photo_exit,
                                compound=TOP, command=self.exiting) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 4, y=ls[1] // 6*3)

    def FeesGenerator(self):
        self.frame.place_forget()
        GeneratorFees.Class_Fees(self.root, self.ls, self.frame, self.roll)

    def AttendanceGenerator(self):
        self.frame.place_forget()
        GeneratorAttendance.Class_Attendance(self.root, self.ls, self.frame, self.roll)

    def IDGenerator(self):
        self.frame.place_forget()
        GeneratorID.Class_ID(self.root, self.ls, self.frame, self.roll)

    def MarksheetGenerator(self):
        self.frame.place_forget()
        GeneratorMarksheet.Class_Marksheet(self.root, self.ls, self.frame, self.roll)

    def exiting(self):
        self.frame.place_forget()
        self.frame_run.destroy()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass
from tkinter import *
from tkinter import ttk

import Register_student
import MarksManager
import FeesManager
import Manage_Attendance


class Employee_Menu:
    def __init__(self, root, ls, frame_old, frame_run):
        # Creating the first frame.
        self.frame_run = frame_run
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Labeling the page.
        self.title = Label(self.frame, text='Nirma University', font=('Algerian', 25, 'bold'), bg="#163148",
                           fg="#ffffff").pack(
            side=TOP)

        # Creating a second frame.
        self.frame2 = Frame(self.frame, bg='#ffffff')
        self.frame2.place(x=ls[0] // 9, y=ls[1] // 8, width=ls[0] // 9 * 7, height=ls[1] // 8 * 6)

        # Title for Register/Login.
        self.title1 = Label(self.frame2, text='Faculty management system', font=('Algerian', 22, 'bold'),
                            bg='#ffffff').pack(
            side=TOP)

        # Taking All pics in the variable.
        self.photo_new_student = PhotoImage(file=r"Images/New Student.png")
        self.photo_attendance = PhotoImage(file=r"Images/attendance.png")
        self.photo_marksheet = PhotoImage(file=r"Images/marksheet.png")
        self.photo_fees = PhotoImage(file=r"Images/fees.png")
        self.photo_exit = PhotoImage(file=r"Images/exit.png")

        # Resizing the Images as per requirement.
        self.photo_new_student = self.photo_new_student.subsample(7, 7)
        self.photo_attendance = self.photo_attendance.subsample(5, 5)
        self.photo_marksheet = self.photo_marksheet.subsample(5, 5)
        self.photo_fees = self.photo_fees.subsample(5, 5)
        self.photo_exit = self.photo_exit.subsample(5, 5)

        # Creating a Button Images.
        self.new_student_btn = Button(self.frame2, text='Manage Student', bd=0, bg='#fbf8e6', image=self.photo_new_student,
                              compound=TOP, command=self.Register) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9, y=ls[1] // 6)

        self.attendance = Button(self.frame2, text='Manage Attendance', bd=0, bg='#fbf8e6', image=self.photo_attendance,
                                 compound=TOP, command=self.ManageAttendance) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 3, y=ls[1] // 6)

        self.marksheet = Button(self.frame2, text='Manage Marks', bd=0, bg='#fbf8e6', image=self.photo_marksheet,
                                compound=TOP, command=self.Manage_Marks) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 5, y=ls[1] // 6)

        self.fees_btn = Button(self.frame2, text='Manage Fee Status', bd=0, bg='#fbf8e6', image=self.photo_fees,
                               compound=TOP, command=self.Manage_Fees) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 2, y=ls[1] // 6 * 3)

        self.Exit_btn = Button(self.frame2, text='Exit', bd=0, bg='#fbf8e6', image=self.photo_exit,
                               compound=TOP, command=self.exiting) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 4, y=ls[1] // 6 * 3)

    def Manage_Marks(self):
        self.frame.place_forget()
        MarksManager.Class_Marks(self.root, self.ls, self.frame)
        pass

    def Manage_Fees(self):
        self.frame.place_forget()
        FeesManager.ClassFees(self.root, self.ls, self.frame)
        pass

    def ManageAttendance(self):
        self.frame.place_forget()
        Manage_Attendance.Class_Attendance(self.root, self.ls, self.frame)
        pass

    def Register(self):
        self.frame.place_forget()
        Register_student.Registration(self.root, self.ls, self.frame)
        pass

    def exiting(self):
        self.frame.place_forget()
        self.frame_run.destroy()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

from tkinter import *
from tkinter import ttk

import sqlite3


class Class_Marks:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()
        self.search_txt = StringVar()

        # Creating Subject Variable.
        self.Subject_1 = StringVar()
        self.Subject_2 = StringVar()
        self.Subject_3 = StringVar()
        self.Subject_4 = StringVar()
        self.Subject_5 = StringVar()
        self.Subject_6 = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Manage Student Marks', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a Left-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*20//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)

        # Labeling a manage frame.
        m_title = Label(Manage_Frame, text="Manage Students", bg="lightpink", fg="blue",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Create a roll Number, name, email, and all things like form.
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_sub1 = Label(Manage_Frame, text="Data Structures: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub1.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_sub1 = Entry(Manage_Frame, textvariable=self.Subject_1, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_sub1.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_sub2 = Label(Manage_Frame, text="Digital Electronics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub2.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_sub2 = Entry(Manage_Frame, textvariable=self.Subject_2, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub2.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_sub3 = Label(Manage_Frame, text="Discrete Mathematics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub3.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_sub3 = Entry(Manage_Frame, textvariable=self.Subject_3, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_sub3.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_sub4 = Label(Manage_Frame, text="Principle of Economics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub4.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_sub4 = Entry(Manage_Frame, textvariable=self.Subject_4, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub4.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_sub5 = Label(Manage_Frame, text="Object Oriented Prog.: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub5.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_sub5 = Entry(Manage_Frame, textvariable=self.Subject_5, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub5.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_sub6 = Label(Manage_Frame, text="Digital Communication: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub6.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_sub6 = Entry(Manage_Frame, textvariable=self.Subject_6, font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_sub6.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Creating a second frame.
        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        btn_frame.place(x=ls[0]*15//1336, y=ls[1]*500//714, width=ls[0]*420//1336)

        Addbtn = Button(btn_frame, text="ADD", bg='black', fg='white', width=10, command=self.add_data).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
        updatebtn = Button(btn_frame, text="UPDATE", bg='black', fg='white', width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="DELETE", bg='black', fg='white', width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="CLEAR", bg='black', fg='white', width=10, command=self.clear).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)

        Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
        Detail_Frame.place(x=ls[0]*490//1336, y=ls[1]*100//714, width=ls[0]*830//1336, height=ls[1]*580//714)

        lbl_search = Label(Detail_Frame, text="Search By", bg="cornsilk", fg="blue",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, width=20, textvariable=self.search_txt, font=("times new roman", 12, "bold"),
                           bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,column=3, padx=10, pady=10)
        showall_btn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch).grid(row=0, column=4, padx=10, pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        Table_Frame.place(x=ls[0]*10//1336, y=ls[1]*70//714, width=ls[0]*760//1336, height=ls[1]*500//714)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=("Roll", "DSA", "D.E.", "D.M.", "POE", "OOPs", "D.C."),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll", text="Roll NO.")
        self.Student_table.heading("DSA", text="DSA")
        self.Student_table.heading("D.E.", text="D.E.")
        self.Student_table.heading("D.M.", text="D.M.")
        self.Student_table.heading("POE", text="POE")
        self.Student_table.heading("OOPs", text="OOPs")
        self.Student_table.heading("D.C.", text="D.C.")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("DSA", width=100)
        self.Student_table.column("D.E.", width=100)
        self.Student_table.column("D.M.", width=100)
        self.Student_table.column("POE", width=100)
        self.Student_table.column("OOPs", width=100)
        self.Student_table.column("D.C.", width=100)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()

    def add_data(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_data WHERE roll_no= "+self.Roll_No_var.get())

        rows = c.fetchall()

        if len(rows)!=0:
            c.execute("INSERT INTO student_marks VALUES (?,?,?,?,?,?,?)", (self.Roll_No_var.get(),
                                                                          self.Subject_1.get(),
                                                                          self.Subject_2.get(),
                                                                          self.Subject_3.get(),
                                                                          self.Subject_4.get(),
                                                                          self.Subject_5.get(),
                                                                          self.Subject_6.get()
                                                                          ))
            conn.commit()
            self.fetch()
            self.clear()
            conn.close()
            pass
        else:
            #Message Box.
            pass

    def fetch(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_marks")
        rows = c.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Subject_1.set(row[1])
        self.Subject_2.set(row[2])
        self.Subject_3.set(row[3])
        self.Subject_4.set(row[4])
        self.Subject_5.set(row[5])
        self.Subject_6.set(row[6])

    def update_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("UPDATE student_marks SET english='{}', mathematics='{}', social_science='{}', sanskrit='{}', gujarati='{}', science='{}' where Roll_no= {}"
                    .format(self.Subject_1.get(),
                            self.Subject_2.get(),
                            self.Subject_3.get(),
                            self.Subject_4.get(),
                            self.Subject_5.get(),
                            self.Subject_6.get(),
                            self.Roll_No_var.get()
        ))

        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM student_marks where Roll_No = " + self.Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch()
        self.clear()

    def clear(self):
        self.Roll_No_var.set("")
        self.Subject_1.set("")
        self.Subject_2.set("")
        self.Subject_3.set("")
        self.Subject_4.set("")
        self.Subject_5.set("")
        self.Subject_6.set("")

    def search_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_marks where Roll_No LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import ttk
# import HomePage
import ctypes
import sqlite3

class Class_Attendance:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()
        self.var_radio = IntVar()
        self.flag1 = 0
        self.flag2 = 0

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Attendence Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Roll_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Roll_Frame.place(x=ls[0] // 2 - 200, y=ls[1] // 7 * 1, width=ls[0]*400//1336, height=ls[1] // 7 * 2)

        # Creating a Bottom-Side Frame.
        self.Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        self.Manage_Frame.place(x=ls[0] // 2 - 400, y=ls[1] // 7 * 4, width=ls[0]*800//1336, height=ls[1] // 7 * 2)

        # Labeling And Roll_No
        lbl_roll = Label(Roll_Frame, text="Enter Your Roll No.", bg="LightBlue", fg="RED",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=25, padx=70, sticky="w")

        # Text Box For Roll_No.
        txt_Roll = Entry(Roll_Frame, width=20, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=0, pady=0, padx=105, sticky="w")

        # Button
        CheckBtn = Button(Roll_Frame, text="Check It!!", bg='black', fg='white', width=10, command=self.Attendance)
        CheckBtn.grid(row=3, column=0, pady=20, padx=150, sticky="w")
        # -----------

    def Attendance(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.Roll_No_var.get()))

        rows = cur.fetchall()

        if len(rows) != 0:
            def sel():
                selection = "You selected the option " + str(self.var_radio.get())

            if self.flag1 == 0:
                if self.flag2 == 0:
                    self.lbl = Label(self.Manage_Frame, text="Mark Present/Absent ", bg="cornsilk", fg="red",
                                 font=("times new roman", 16, "bold"))
                    self.lbl.place(x=self.ls[0]*300//1336, y=self.ls[1]*10//714)

                    self.present = Radiobutton(self.Manage_Frame, text="Present", bg="cornsilk", variable=self.var_radio,
                                           value=1,
                                           command=sel, font=("times new roman", 16))
                    self.present.place(x=self.ls[0]*350//1336, y=self.ls[1]*35//714)

                    self.Absent = Radiobutton(self.Manage_Frame, text="Absent", bg="cornsilk", variable=self.var_radio,
                                          value=2,
                                          command=sel, font=("times new roman", 16))
                    self.Absent.place(x=self.ls[0]*350//1336, y=self.ls[1]*75//714)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                     command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*350//1336, y=self.ls[1]*130//714)
                    self.flag1 = 1
                else:
                    self.Attendence.destroy()
                    self.lbl = Label(self.Manage_Frame, text="Mark Present/Absent ", bg="cornsilk", fg="red",
                                     font=("times new roman", 16, "bold"))
                    self.lbl.place(x=self.ls[0]*300//1336, y=self.ls[1]*10//714)

                    self.present = Radiobutton(self.Manage_Frame, text="Present", bg="cornsilk",
                                               variable=self.var_radio,
                                               value=1,
                                               command=sel, font=("times new roman", 16))
                    self.present.place(x=self.ls[0]*350//1336, y=self.ls[1]*35//714)

                    self.Absent = Radiobutton(self.Manage_Frame, text="Absent", bg="cornsilk", variable=self.var_radio,
                                              value=2,
                                              command=sel, font=("times new roman", 16))
                    self.Absent.place(x=self.ls[0]*350//1336, y=self.ls[1]*75//714)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                         command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*350//1336, y=self.ls[1]*130//714)
                    self.flag1 = 1
                    self.flag2 = 0
            elif self.flag1 == 1:
                pass
        else:
            if self.flag2 == 0:
                if self.flag1 == 0:
                    self.Attendence = Label(self.Manage_Frame,text="Roll Number Does not Exist", anchor=CENTER, bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                else:
                    self.lbl.place_forget()
                    self.present.place_forget()
                    self.Absent.place_forget()
                    self.ok_btn.place_forget()
                    self.Attendence = Label(self.Manage_Frame, text="Roll Number Does not Exist", anchor=CENTER,
                                            bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                    self.flag1 = 0
            elif self.flag2 == 1:
                pass
        pass

    def ok_fun(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_attendance WHERE roll_no = "+str(self.Roll_No_var.get()))
        rows = c.fetchall()
        att = int(self.var_radio.get()) - 1

        if att==0:
            present = int(rows[0][1]) + 1
            total = int(rows[0][2]) + 1
            print(present, total)
            c.execute(f"UPDATE student_attendance SET present={present}, total={total} WHERE roll_no = " + str(self.Roll_No_var.get()))
            # Update both
        else:
            total = int(rows[0][2]) + 1
            c.execute(f"UPDATE student_attendance SET total={total} WHERE roll_no = " + str(
                self.Roll_No_var.get()))

        self.var_radio.set(0)
        conn.commit()
        conn.close()
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import messagebox

import sqlite3

import Menu_Student

class Student_Show:
    def __init__(self,root,ls,frame_old):
        self.frame_old = frame_old
        self.root = root
        self.ls = ls

        # Creating the variable.
        self.Roll_No_var = StringVar()
        self.password_var = StringVar()

        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0] // 7 * 2, y=ls[1] // 4, width=ls[0] // 7 * 3, height=ls[1] // 4 * 2)

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the page.
        self.title = Label(self.frame, text='NIRMA UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='Student Login', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Label Login
        lbl_id = Label(self.frame1, text="Roll No.: ", bg="white", fg="blue", font=("times new roman",15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*127//714)

        txt_id = Entry(self.frame1, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*130//714)

        # Label Login
        lbl_id = Label(self.frame1, text="Password: ", bg="white", fg="blue", font=("times new roman", 15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*197//714)

        txt_id = Entry(self.frame1, textvariable=self.password_var, font=("times new roman", 12), bd=2,
                       relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*200//714)

        # Submit Button
        self.fees_btn = Button(self.frame1, text='Login', bd=0, bg='black',fg='white',font=("times new roman", 15),
                               compound=TOP, command=self.new_page)
        self.fees_btn.place(x=ls[0]*250//1336, y=ls[1]*300//714)

    def new_page(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM student_data where Roll_No=" + str(self.Roll_No_var.get()))

        rows = cur.fetchall()
        if len(rows) != 0:
            if str(self.password_var.get()) == str(rows[0][4]):
                self.roll = str(rows[0][0])
                firster = Menu_Student.Student_Menu(self.root, self.ls, self.frame_old, self.frame, self.roll)
            else:
                messagebox.showerror("Error", "Wrong Password, Please Input Valid Password.")
        else:
            messagebox.showerror("Error", "No such student found!!!")


    def exiting(self):
        self.frame.place_forget()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3
import Menu_Employee

class Employee_Show:
    def __init__(self,root,ls,frame_old):
        self.frame_old = frame_old
        self.root = root
        self.ls = ls

        # Creating the variable.
        self.id_var = StringVar()
        self.password_var = StringVar()

        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0] // 7 * 2, y=ls[1] // 4, width=ls[0] // 7 * 3, height=ls[1] // 4 * 2)

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the page.
        self.title = Label(self.frame, text='NIRMA UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='Faculty Login', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Label Login
        lbl_id = Label(self.frame1, text="Id: ", bg="white", fg="blue", font=("times new roman",15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*127//714)

        txt_id = Entry(self.frame1, textvariable=self.id_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*130//714)

        # Label Login
        lbl_id = Label(self.frame1, text="Password: ", bg="white", fg="blue", font=("times new roman", 15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*197//714)

        txt_id = Entry(self.frame1, textvariable=self.password_var, font=("times new roman", 12), bd=2,
                       relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*200//714)

        # Submit Button
        self.fees_btn = Button(self.frame1, text='Login', bd=0, bg='black',fg='white',font=("times new roman", 15),
                               compound=TOP, command=self.new_page)
        self.fees_btn.place(x=ls[0]*250//1336, y=ls[1]*300//714)

    def new_page(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM employee_login where id=" + str(self.id_var.get()))

        rows = cur.fetchall()
        if len(rows) != 0:
            if str(self.password_var.get()) == str(rows[0][1]):
                firster = Menu_Employee.Employee_Menu(self.root, self.ls, self.frame_old, self.frame)
            else:
                messagebox.showerror("Error", "Wrong Password, Please Input Valid Password.")
        else:
            messagebox.showerror("Error", "No such employee found!!!")
        pass

    def exiting(self):
        self.frame.place_forget()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

import Login_Student
import Login_Employee
 
class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls
        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0]//9*2, y=ls[1]//4, width=ls[0]//9*5, height=ls[1]//4*2)

        # Taking All pics in the variable.
        self.photo_student = PhotoImage(file=r"Images/student_img.png")
        self.photo_employee = PhotoImage(file=r"Images/employee.png")

        # Resizing the Images as per requirement.
        self.photo_student = self.photo_student.subsample(4, 4)
        self.photo_employee = self.photo_employee.subsample(4, 4)

        # Labeling the page.
        self.title = Label(self.frame, text='NIRMA UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='Register/Login', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.student_btn = Button(self.frame1, text='Student', bd=0, bg='#ffffff', image=self.photo_student,
                                   compound=TOP, command=self.student) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9)*3-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

        self.employee_btn = Button(self.frame1, text="Faculty", bd=0, bg='#ffffff', image=self.photo_employee,
                                   compound=TOP, command=self.employee) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9 * 5)-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

    def student(self):
        self.frame.place_forget()
        student_menu = Login_Student.Student_Show(self.root, self.ls, self.frame)

    def employee(self):
        self.frame.place_forget()
        employee_menu = Login_Employee.Employee_Show(self.root, self.ls, self.frame)

from tkinter import *
from tkinter import ttk

import sqlite3


class Class_Marksheet:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Marksheet Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a Main-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*430//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)


        # Database
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_marks where Roll_No= "+self.roll)

        rows = cur.fetchall()

        self.sub1 = rows[0][1]
        self.sub2 = rows[0][2]
        self.sub3 = rows[0][3]
        self.sub4 = rows[0][4]
        self.sub5 = rows[0][5]
        self.sub6 = rows[0][6]
        flag=0


        # Label Nirma
        uni_labl = Label(Manage_Frame, anchor=CENTER, bg='lightblue', text='Nirma University', font=('Algerian', 20))
        uni_labl.pack(side=TOP,fill=X)

        # Creating the Sr. No.
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Sr No.", font=('Times New Roman', 18))
        srl_lbl.place(x=ls[0]*30//1336,y=ls[1]*100//714)

        # Creating the subject tag.
        name_lbl = Label(Manage_Frame, bg='lightblue', text="Subject", font=('Times New Roman', 18))
        name_lbl.place(x=ls[0]*175//1336, y=ls[1]*100//714)

        # Creating the marks_lbl.
        marks_lbl = Label(Manage_Frame, bg='lightblue', text="Marks", font=('Times New Roman', 18))
        marks_lbl.place(x=ls[0]*320//1336, y=ls[1]*100//714)


        # Creating the Sr. No.1
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="1", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*140//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Data Structures", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*140//1336, y=ls[1]*140//714)

        sub1_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub1, font=('Times New Roman', 16))
        sub1_lbl.place(x=ls[0]*335//1336, y=ls[1]*140//714)

        if int(self.sub1) < 33:
            flag=1
            sub1_lbl.config(fg='red')


        # Creating the Sr. No.2
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="2", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*180//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Digital Electronics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*130//1336, y=ls[1]*180//714)

        sub2_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub2, font=('Times New Roman', 16))
        sub2_lbl.place(x=ls[0]*335//1336, y=ls[1]*180//714)

        if int(self.sub2) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.3
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="3", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*220//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Discrete Mathematics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*120//1336, y=ls[1]*220//714)

        sub3_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub3, font=('Times New Roman', 16))
        sub3_lbl.place(x=ls[0]*335//1336, y=ls[1]*220//714)

        if int(self.sub3) < 33:
            flag=1
            sub1_lbl.config(fg='red')


        # Creating the Sr. No.4
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="4", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*260//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Principle Of Economics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*110//1336, y=ls[1]*260//714)

        sub4_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub4, font=('Times New Roman', 16))
        sub4_lbl.place(x=ls[0]*335//1336, y=ls[1]*260//714)

        if int(self.sub4) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.5
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="5", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*300//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Object Oriented Prog.", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*120//1336, y=ls[1]*300//714)

        sub5_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub5, font=('Times New Roman', 16))
        sub5_lbl.place(x=ls[0]*335//1336, y=ls[1]*300//714)

        if int(self.sub5) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.6
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="6", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*340//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Digital Communication", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*110//1336, y=ls[1]*340//714)

        sub6_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub6, font=('Times New Roman', 16))
        sub6_lbl.place(x=ls[0]*335//1336, y=ls[1]*340//714)

        if int(self.sub6) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        total = int(self.sub1) + int(self.sub2) + int(self.sub3) + int(self.sub4) +int(self.sub5) +int(self.sub6)

        total_lbl = Label(Manage_Frame, bg='lightblue', text="Total", font=('Times New Roman', 16))
        total_lbl.place(x=ls[0]*285//1336, y=ls[1]*390//714)

        total_lbl = Label(Manage_Frame, bg='lightblue', text=total, font=('Times New Roman', 16))
        total_lbl.place(x=ls[0]*335//1336, y=ls[1]*390//714)

        if flag==1:
            total_lbl.config(text="IF", fg='red')

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import ttk

import sqlite3



class Class_ID:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='ID-Card Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.roll))

        rows = cur.fetchall()

        self.name = str(rows[0][1])
        self.email = str(rows[0][2])
        self.gender = str(rows[0][3])
        self.phone = str(rows[0][4])
        self.dob = str(rows[0][5])
        self.address = str(rows[0][6])

        # Generating Bar Code.
        from PIL import Image, ImageDraw, ImageFont
        image = Image.new('RGB', (1000, 600), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('arial.ttf', size=45)
        import qrcode

        # Nirma Tag
        (x, y) = (230, 40)
        message = "Nirma University"
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=70)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 190)
        name = "Name: " + self.name
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), name, fill=color, font=font)

        (x, y) = (50, 260)
        message = "Gender: " + self.gender
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 330)
        message = "Phone: " + self.phone
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 400)
        message = "DOB: " + self.dob
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 470)
        message = "Address: " + self.address
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        # save the edited image

        image.save(str("id_card") + '.png')

        img = qrcode.make(str(company) + str(self.roll))  # this info. is added in QR code, also add other things
        img.save(str("id_card") + '.bmp')

        til = Image.open(str("id_card") + '.png')
        im = Image.open(str("id_card") + '.bmp')  # 25x25
        til.paste(im, (640, 160))
        til.save(str("id_card") + '.png')

        self.photo_ID_Card = PhotoImage(file=r"id_card.png").subsample(2,2)

        image_id = Label(self.frame, image=self.photo_ID_Card, bg="white")
        image_id.place(x=ls[0]*420//1336, y=ls[1]*260//714)

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

from tkinter import *
from tkinter import ttk


import sqlite3

class Class_Fees:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll=roll
        self.frame_old = frame_old

        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Fee Status Checker', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Paid_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Paid_Frame.place(x=ls[0]//2-350, y=ls[1]//9*1+50, width=ls[0]*300//1336, height=ls[1]//9*2)

        # Creating a top-Side Frame.
        Rem_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Rem_Frame.place(x=ls[0] // 2 + 50, y=ls[1] // 9 * 1 + 50, width=ls[0]*300//1336, height=ls[1] // 9 * 2)

        # Creating a Bottom-Side Frame.
        Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        Manage_Frame.place(x=ls[0]//2-400, y=ls[1]//7*4, width=ls[0]*800//1336, height=ls[1]//7*2)

        # Text Variable.
        self.Txt_fees = Label(Manage_Frame, anchor=CENTER, bg='cornsilk', font=("times new roman", 30))
        self.Txt_fees.pack(fill=BOTH, expand=1)

        # Text Variable.
        self.Txt_paid = Label(Paid_Frame, anchor=CENTER, text="Fees Paid", bg='lightblue',fg='red', font=("times new roman", 18))
        self.Txt_paid.place(x=0, y=ls[1]*50//714, width=ls[0]*300//1336-15)

        # Text Variable.
        self.Txt_rem = Label(Rem_Frame,anchor=CENTER, text="Fees Remaining", bg='lightblue',fg='red', font=("times new roman", 18))
        self.Txt_rem.place(x=0, y=ls[1]*50//714, width=ls[0]*300//1336-15)

        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_fees WHERE Roll_No= "+self.roll)

        rows = c.fetchall()

        if int(rows[0][1]) == 0:
            self.Txt_fees.config(text="Fees Data Not Available")
        else:
            if int(rows[0][2]) == 0:
                self.Txt_fees.config(text="Your current semester fees has been paid.")
            else:
                self.Txt_fees.config(text="Partial Fees Paid")

        # Creating the fees.
        self.fees_paid = Label(Paid_Frame,anchor=CENTER, text=str(rows[0][1]), bg='lightblue', font=("times new roman", 18))
        self.fees_paid.place(x=0, y=ls[1]*80//714, width=ls[0]*300//1336-15)

        # Creating the fees.
        self.fees_rem = Label(Rem_Frame,anchor=CENTER, text=str(rows[0][2]), bg='lightblue', font=("times new roman", 18))
        self.fees_rem.place(x=0, y=ls[1]*80//714, width=ls[0]*300//1336-15)


    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import ttk

import sqlite3

class Class_Attendance:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.roll = roll
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Attendance Checker', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.roll))

        rows = cur.fetchall()
        if len(rows) != 0:
            self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
            self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

            cur.execute("SELECT * FROM student_attendance where Roll_No= " + str(self.roll))
            rows_attendence_roll = cur.fetchall()
            if len(rows_attendence_roll) != 0 and int(rows_attendence_roll[0][2]) != 0:
                self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
                self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)
                percentage = int(rows_attendence_roll[0][1])/int(rows_attendence_roll[0][2])*100

                # Labeling And Roll_No
                lbl_roll = Label(self.Detail_Frame, text=f"Your attendance is {percentage}!!!", bg="cornsilk",
                                 fg="blue",
                                 font=("times new roman", 30, "bold"))
                lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)
            else:
                self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
                self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

                # Labeling And Roll_No
                lbl_roll = Label(self.Detail_Frame, text="Attendence is Not Available, Sorry!!!", bg="cornsilk",
                                 fg="blue",
                                 font=("times new roman", 30, "bold"))
                lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)

        else:
            self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
            self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

            # Labeling And Roll_No
            lbl_roll = Label(self.Detail_Frame, text="Roll Number Does Not Exist!!!", bg="cornsilk", fg="blue",
                             font=("times new roman", 30, "bold"))
            lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

from tkinter import *
from tkinter import ttk

import sqlite3


class ClassFees:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.flag2 = 0
        self.flag1 = 0

        self.Roll_No_var = StringVar()
        self.search_txt = StringVar()
        self.fees_paid = StringVar()
        self.fees_rem = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Manage Student Fees', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Roll_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Roll_Frame.place(x=ls[0] // 2 - 200, y=ls[1] // 7 * 1, width=ls[0] * 400 // 1336, height=ls[1] // 7 * 2)

        # Creating a Bottom-Side Frame.
        self.Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        self.Manage_Frame.place(x=ls[0] // 2 - 400, y=ls[1] // 7 * 4, width=ls[0] * 800 // 1336, height=ls[1] // 7 * 2)

        # Labeling And Roll_No
        lbl_roll = Label(Roll_Frame, text="Enter Your Roll No.", bg="LightBlue", fg="RED",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=25, padx=70, sticky="w")

        # Text Box For Roll_No.
        txt_Roll = Entry(Roll_Frame, width=20, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=0, pady=0, padx=105, sticky="w")

        # Button
        CheckBtn = Button(Roll_Frame, text="Check It!!", bg='black', fg='white', width=10, command=self.Fees)
        CheckBtn.grid(row=3, column=0, pady=20, padx=150, sticky="w")
        # -----------

    def Fees(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.Roll_No_var.get()))

        rows = cur.fetchall()

        if len(rows) != 0:
            if self.flag1 == 0:
                if self.flag2 == 0:
                    # Paid Fees Part
                    self.Frame_paid = Frame(self.Manage_Frame, bg='cornsilk')
                    self.Frame_paid.place(x=0,y=0,width=(self.ls[0] * 800 // 1336)//2-5, height=150)

                    # Fees Remaining.
                    # Paid Fees Part
                    self.Frame_rem = Frame(self.Manage_Frame, bg='cornsilk')
                    self.Frame_rem.place(x=(self.ls[0] * 800 // 1336)//2+5, y=0, width=(self.ls[0] * 800 // 1336) // 2-5, height=150)

                    # Labeling And Text.
                    self.lbl_paid = Label(self.Frame_paid,anchor=CENTER, text="Enter Fees Paid",font=("times new roman", 16), bg='cornsilk', fg='blue')
                    self.lbl_paid.place(x=0,y=0,width=(self.ls[0] * 800 // 1336)//2-5, height=75)

                    # Labeling And Text.
                    self.lbl_paid = Label(self.Frame_rem, anchor=CENTER, text="Enter Fees Remaining",font=("times new roman", 16), bg='cornsilk', fg='blue')
                    self.lbl_paid.place(x=0, y=0, width=(self.ls[0] * 800 // 1336) // 2 - 5, height=75)

                    # Text Paid.
                    self.txt_paid = Entry(self.Frame_paid,textvariable=self.fees_paid, font=("times new roman", 14))
                    self.txt_paid.place(x=self.ls[0]*115//1336,y=self.ls[1]*78//714,width=self.ls[0]*175//1336)

                    # Text Rem.
                    self.txt_rem = Entry(self.Frame_rem,textvariable=self.fees_rem, font=("times new roman", 14))
                    self.txt_rem.place(x=self.ls[0]*115//1336, y=self.ls[1]*78//714, width=self.ls[0] * 175 // 1336)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                     command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*360//1336, y=self.ls[1]*170//714)
                    self.flag1 = 1
                else:
                    self.Attendence.destroy()
                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                         command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*360//1336, y=self.ls[1]*170//714)
                    self.flag1 = 1
                    self.flag2 = 0
            elif self.flag1 == 1:
                pass
        else:
            if self.flag2 == 0:
                if self.flag1 == 0:
                    self.Attendence = Label(self.Manage_Frame,text="Roll Number Does not Exist", anchor=CENTER, bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                else:
                    self.Attendence = Label(self.Manage_Frame, text="Roll Number Does not Exist", anchor=CENTER,
                                            bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                    self.flag1 = 0
            elif self.flag2 == 1:
                pass

    def ok_fun(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_fees WHERE roll_no = " + str(self.Roll_No_var.get()))
        rows = c.fetchall()
        if int(self.fees_paid.get())>=0 and int(self.fees_rem.get())>=0:
            c.execute(f"UPDATE student_fees SET fees_paid={self.fees_paid.get()}, fees_rem={int(self.fees_rem.get())} WHERE roll_no = " + str(
                self.Roll_No_var.get()))
        conn.commit()
        conn.close()
        self.Frame_paid.place_forget()
        self.Frame_rem.place_forget()
        self.ok_btn.place_forget()
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
