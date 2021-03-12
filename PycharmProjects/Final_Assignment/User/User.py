#importing modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
"""
page class helps the user determine what is the interface and how it is different is it depending on shape, size and color
"""
class page:
    def __init__(self,window):
        self.window = window
        self.window.title("User Management System")
        self.window.geometry("800x700+300+0")
        self.window.resizable(False,False)

        Main_frame = Frame(self.window, bd = 10, width = 770, height = 700, relief = RIDGE, bg = "lavender")
        Main_frame.grid()
         '''
        Python takes this frame to take the user interface to be suitable with the backgroun
        '''

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
        # values
        UserID = StringVar()
        username = StringVar()
        email = StringVar()
        password = StringVar()
        age = StringVar()

       """
       these buttons such as add_btn, reset, delete, update can do with function to determine 
       what a single button can do. For example; Add_btn can add database to the table, reset can remove the data from
       the box and delete button can delete the required information based on Primary Key.
       """
        def add_btn():
            if UserID.get() == '' or username.get() == '' or email == '' :
                messagebox.showerror("Empty Field", "plz fill correct details")
            else:
                querycon = pymysql.connect(host = 'localhost', user = 'Kyser', password = 'Sarthak1', database = 'users')
                cur = querycon.cursor()
                cur.execute("insert into user_table values(%s,%s,%s,%s,%s)",(
                UserID.get(),
                username.get(),
                email.get(),
                password.get(),
                age.get(),
                ))

                querycon.commit()
                querycon.close()
                messagebox.showinfo("User Management System", "User is registered")


        def display_data():
                querycon = pymysql.connect(host = 'localhost', user = 'Kyser', password = 'Sarthak1', database = 'users')
                cur = querycon.cursor()
                cur.execute("select * from user_table")
                results = cur.fetchall()
                if len(results) != 0:
                    self.user_record.delete(*self.user_record.get_children())
                    for row in results:
                        self.user_record.insert('', END, values = row)
                querycon.commit()
                querycon.close()
        def reset():
            self.email_entry.delete(0, END)
            self.email_entry.insert(0, "")
            self.user_entry.delete(0, END)
            self.user_entry.insert(0, "")
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, "")
            self.Age_entry.delete(0, END)
            self.Age_entry.insert(0, "")
            self.username_entry.delete(0,END)
            self.username_entry.insert(0,"")

        def userinfo(ev):
            viewinfo = self.user_record.focus()
            data1 = self.user_record.item(viewinfo)
            row = data1['values']
            UserID.set(row[0])
            username.set(row[1])
            email.set(row[2])
            password.set(row[3])
            age.set(row[4])


        def update():
            querycon = pymysql.connect(host='localhost', user='Kyser', password='Sarthak1', database='users')
            cur = querycon.cursor()
            cur.execute("update user_table set username = %s, email = %s, password1 = %s, Age = %s where user_id = %s",(
                username.get(),
                email.get(),
                password.get(),
                age.get(),
                UserID.get()
            ))
            querycon.commit()
            querycon.close()
            messagebox.showinfo("student management system","Data Updated")

        def delete():
            querycon = pymysql.connect(host='localhost', user='Kyser', password='Sarthak1', database='users')
            cur = querycon.cursor()
            cur.execute("delete from user_table where user_id = %s",UserID.get())
            querycon.commit()
            querycon.close()
            messagebox.showinfo("User management system","Record deleted sucessfully")



        def search():
            try:
                querycon = pymysql.connect(host='localhost', user='Kyser', password='Sarthak1', database='users')
                cur = querycon.cursor()
                cur.execute("select * from user_table where user_id = %s ", UserID.get() )
                row = cur.fetchone()

                UserID.set(row[0])
                username.set(row[1])
                email.set(row[2])
                password.set(row[3])
                age.set(row[4])

                querycon.commit()
            except:
                messagebox.showinfo("User management system", "Records are here")
                reset()
            querycon.close()



        '''
        Label help to determine that what is the name of the thing that is used for 
        adding or fill datas in and also what grid is it in to write or type the data.
        Entry helps to write or type the data in the required boxes.
        '''
        self.lbltitle = Label(Title_frame, font = ("Times New Roman", 40, 'bold'), text = "User Management System", bd = 7)
        self.lbltitle.grid(row = 0, column = 0, padx = 132)

        self.userId = Label(L_frame, font = ("Times New Roman", 12, 'bold'), text = "User ID", bd = 7)
        self.userId.grid(row = 1, column = 0, sticky = W, padx = 5)
        self.user_entry = Entry(L_frame, font = ("Times New Roman", 12, 'bold'), bd = 5, width = 40, justify = 'left', textvariable = UserID )
        self.user_entry.grid(row = 1, column = 1, sticky = W, padx = 5)

        self.user = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="username", bd=7)
        self.user.grid(row=2, column=0, sticky=W, padx=5)
        self.username_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left', textvariable = username)
        self.username_entry.grid(row=2, column=1, sticky=W, padx=5)

        self.emailId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Email", bd=7)
        self.emailId.grid(row=3, column=0, sticky=W, padx=5)
        self.email_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left', textvariable = email)
        self.email_entry.grid(row=3, column=1, sticky=W, padx=5)

        self.passwordId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Password", bd=7)
        self.passwordId.grid(row=4, column=0, sticky=W, padx=5)
        self.password_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left', textvariable = password)
        self.password_entry.grid(row=4, column=1, sticky=W, padx=5)

        self.ageId = Label(L_frame, font=("Times New Roman", 12, 'bold'), text="Age", bd=7)
        self.ageId.grid(row=5, column=0, sticky=W, padx=5)
        self.Age_entry = Entry(L_frame, font=("Times New Roman", 12, 'bold'), bd=5, width=40, justify='left', textvariable = age)
        self.Age_entry.grid(row=5, column=1, sticky=W, padx=5)

        '''
        Since, there are going to be numberous amount of the data, a scrollbar is needed to
        help with the interface.
        '''
        scroll_y = Scrollbar(Left_Frame, orient = VERTICAL)
        self.user_record = ttk.Treeview(Left_Frame, height = 14, columns = ('uid','uname','email','passw','age'), xscrollcommand = scroll_y.set)

        scroll_y.pack(side = RIGHT, fill = Y)
       # heading and columns
        self.user_record.heading('uid', text = 'userid')
        self.user_record.heading('uname', text='username')
        self.user_record.heading('email', text='Email')
        self.user_record.heading('passw', text='password')
        self.user_record.heading('age', text='Age')

        self.user_record['show'] = 'headings'

        self.user_record.column('uid', width = 60)
        self.user_record.column('uname', width = 90)
        self.user_record.column('email', width = 90)
        self.user_record.column('passw', width = 70)
        self.user_record.column('age', width = 60)

        self.user_record.pack(fill = BOTH, expand = 1)
        self.user_record.bind('<ButtonRelease-1>', userinfo)

        '''
        the required buttons would help to determine what are the functions and can be used with the command to determine it.
        '''
        self.add_button = Button(R_frame,font=("Times New Roman", 16, 'bold'), text= "insert data" ,bd = 5, pady = 2, padx = 25, width = 6, height = 2, command = add_btn ).grid(row = 0, column = 0, padx = 1)
        self.display_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="display data", bd=5, pady=2,
                                padx=25, width=6, height=2,command = display_data).grid(row=1, column=0, padx=1)
        self.update_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="update data", bd=5, pady=2,
                                padx=25, width=6, height=2, command = update).grid(row=2, column=0, padx=1)
        self.delete_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="delete data", bd=5, pady=2,
                                padx=25, width=6, height=2, command = delete).grid(row=3, column=0, padx=1)
        self.search_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="search data", bd=5, pady=2,
                                padx=25, width=6, height=2, command = search).grid(row=4, column=0, padx=1)
        self.search_button = Button(R_frame, font=("Times New Roman", 16, 'bold'), text="Reset", bd=5, pady=2,
                                padx=25, width=6, height=2, command = reset).grid(row=5, column=0, padx=1)


# calling windows
if __name__ == '__main__':
    window = Tk()
    app = page(window)
    window.mainloop()

# due to having no parameters unit test cant be done properly.
