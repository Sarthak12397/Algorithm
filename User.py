from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

import backend.Dbconnection
import Model.model

class page:
    def __init__(self,window):
        self.window = window
        self.window.title("User Management System")
        self.window.geometry("800x700+300+0")
        self.window.resizable(False,False)
        self.userid = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.address = StringVar()


        self.query1= backend.Dbconnection.DBConnect()
        self.querycon = pymysql.connect(host='localhost', user='Kyser', password='Sarthak1', database='user')
        self.cur = self.querycon.cursor()


        Main_frame = Frame(self.window, bd = 10, width = 770, height = 700, relief = RIDGE, bg = "lavender")
        Main_frame.grid()
        Title_frame = Frame(Main_frame, bd = 7, width = 770, height = 100, relief = RIDGE)
        Title_frame.grid(row = 0, column = 0)
        Top_frame = Frame(Main_frame, bd = 5, width = 770, height = 500, relief = RIDGE)
        Top_frame.grid(row = 1, column = 0)

        Left_Frame = Frame(Top_frame, bd = 5, width = 770, height = 400, padx = 2, bg = "Lavender", relief = RIDGE)
        Left_Frame.pack(side = LEFT)
        L_frame = Frame(Left_Frame, bd =5, width=600, height =180, padx =12, pady = 8, relief =RIDGE)
        L_frame.pack(side = TOP, padx = 0, pady = 0)

        Right_Frame = Frame(Top_frame, bd = 5, width = 100, height = 400, padx = 2, bg = "Lavender", relief = RIDGE)
        Right_Frame.pack(side = RIGHT)
        R_frame = Frame(Right_Frame, bd =5, width=90, height =300, padx =12, pady = 2, relief =RIDGE)
        R_frame.pack(side = TOP)


        self.lbltitle = Label(Title_frame, font=("Times New Roman", 40, 'bold'), text="User Management System", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.userId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="User ID", bd=7)
        self.userId.grid(row=1, column=0, sticky=W, padx=5)
        self.user_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left',
                                textvariable=self.userid)
        self.user_entry.grid(row=1, column=1, sticky=W, padx=5)

        self.user = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="username", bd=7)
        self.user.grid(row=2, column=0, sticky=W, padx=5)
        self.username_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left',
                                    textvariable=self.username)
        self.username_entry.grid(row=2, column=1, sticky=W, padx=5)

        self.emailId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Email", bd=7)
        self.emailId.grid(row=3, column=0, sticky=W, padx=5)
        self.email_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left',
                                 textvariable=self.email)
        self.email_entry.grid(row=3, column=1, sticky=W, padx=5)

        self.passwordId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Password", bd=7)
        self.passwordId.grid(row=4, column=0, sticky=W, padx=5)
        self.password_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left',
                                    textvariable=self.password)
        self.password_entry.grid(row=4, column=1, sticky=W, padx=5)

        self.addres = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Address", bd=7)
        self.addres.grid(row=5, column=0, sticky=W, padx=5)
        self.Address_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left',
                               textvariable=self.address)
        self.Address_entry.grid(row=5, column=1, sticky=W, padx=5)

        scroll_y = Scrollbar(Left_Frame, orient=VERTICAL)
        self.user_record = ttk.Treeview(Left_Frame, height=14, columns=('uid', 'uname', 'email', 'passw', 'age'),
                                        xscrollcommand=scroll_y.set)



        scroll_y.pack(side=RIGHT, fill=Y)
        # heading and columns
        self.user_record.heading('uid', text='userid')
        self.user_record.heading('uname', text='username')
        self.user_record.heading('email', text='Email')
        self.user_record.heading('passw', text='password')
        self.user_record.heading('age', text='Age')

        self.user_record['show'] = 'headings'

        self.user_record.column('uid', width=60)
        self.user_record.column('uname', width=90)
        self.user_record.column('email', width=90)
        self.user_record.column('passw', width=70)
        self.user_record.column('age', width=60)

        self.user_record.pack(fill=BOTH, expand=1)




        self.add_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="insert data", bd=5, pady=2,
                                 padx=25, width=6, height=2, command=self.add_btn).grid(row=0, column=0, padx=1)

        self.reset_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="Reset", bd=5, pady=2,
                                 padx=25, width=6, height=2, command=self.reset).grid(row=5, column=0, padx=1)


        self.display = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="display", bd=5, pady=2,
                                    padx=25, width=6, height=2, command=self.display_data).grid(row=6, column=0, padx=1)

        self.update = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="update", bd=5, pady=2,
                                    padx=25, width=6, height=2, command=self.update).grid(row=7, column=0, padx=1)

        self.delete = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="delete", bd=5, pady=2,
                                    padx=25, width=6, height=2, command=self.delete).grid(row=8, column=0, padx=1)

        self.search = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="search", bd=5, pady=2,
                                    padx=25, width=6, height=2, command=self.search).grid(row=9, column=0, padx=1)






    def reset(self):
        self.email_entry.delete(0, END)
        self.email_entry.insert(0, "")
        self.user_entry.delete(0, END)
        self.user_entry.insert(0, "")
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, "")
        self.Address_entry.delete(0, END)
        self.Address_entry.insert(0, "")
        self.username_entry.delete(0, END)
        self.username_entry.insert(0, "")

    def add_btn(self):
        userid = self.user_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        address = self.Address_entry.get()
        email = self.email_entry.get()

        if self.user_entry.get() == '' or self.username_entry.get() == '' or self.email_entry.get()== '' or self.Address_entry.get() == '' or self.email_entry.get() == '':
            messagebox.showerror("Empty Field", "plz fill correct details")
            return
        u = Model.model.user(userid,username, password,address,email )

        query = "insert into user_detail(userid, username,password,address,email) values(%s,%s,%s,%s,%s)"
        values = (u.get_userId(),u.get_username(),u.get_password(),u.get_address(),u.get_email())
        self.query1.insert(query,values)
        messagebox.showinfo("Data is registered","Data registered")

    def display_data(self):
        query = "select * from user_detail"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.update_row(rows)


    def update_row(self, rows):
        self.user_record.delete(*self.user_record.get_children())
        for i in rows:
            self.user_record.insert('', 'end', values=i)

    def delete(self):
        userid = self.user_entry.get()
        query = "delete from user_detail where userid =%s"
        self.query1.delete(query,(userid,))
        messagebox.showinfo("User Delete", "User deleted")

    def update(self):
        userid = self.user_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        address = self.Address_entry.get()
        email = self.email_entry.get()

        a = Model.model.user(userid, username, password, address, email)
        query = "Update user_detail set username=%s,password=%s,email=%s,address=%s where userid=%s"
        self.query1.update(query, (a.get_username(), a.get_password(), a.get_address(), a.get_email(), a.get_userId()))


    def search(self):
        userid = self.user_entry.get()
        query = "select * from user_detail where userid = %s"
        self.cur.execute(query,userid)
        rows = self.cur.fetchall()
        self.update_row(rows)











































