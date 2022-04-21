# Importing modules
from importlib.resources import contents
from tkinter import *
from tkinter import ttk #TK themed 
from tkinter import Scrollbar 
import pymysql
from tkinter import messagebox
# from tkcalendar import Calendar
from tkcalendar import DateEntry
import datetime 
#Creating a class
class student:
    def __init__(self,root): #object and passing root
        self.root=root #initialising the root
        self.root.title('Library Management System - Sai Ankith - 193213') #Title of window
        self.root.geometry("1366x768+0+0") #Window size and position from (0,0)

        main_title = Label(self.root,text = 'Library Management System - Dept. of Physics, SSSIHL',font = ("arial",30,"bold"),bd=10,relief=RAISED, bg = 'royalblue2', fg = 'white') #title format - bd:border, relief: border effect
        main_title.pack(side=TOP,fill=X) #Packing to the TOP




#----------------All Variables - mysql reqd.-------------------
        self.regd_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.year_var=StringVar()
        self.issue_date_var=StringVar()
        self.due_date_var=StringVar()
        self.author_var=StringVar()
        self.title_var=StringVar()
        self.search=StringVar()
        self.search_txt=StringVar()


        #First frame  
        manage_frame = Frame(self.root, bd=4, relief=RAISED, bg='royalblue2')
        manage_frame.place(x=20,y=100, width=373, height=560)

        m_title=Label(manage_frame, text= 'Enter the details here:',bg = 'ivory3', fg='black', relief=RAISED, font = ("Arial",26,"bold")) #title of first frame
        m_title.grid(row=0,columnspan=2,pady=1) #grid arrangement (row, column), pax,pady: padding of x,y positions around widgets
        main_title.pack(side=TOP,fill=X) #packing the title to the to the top.


        label_regd=Label(manage_frame, text='Regd. No.:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Adding regd. No. Label
        label_regd.grid(row=1,column=0,pady=10, padx =10, sticky = 'w' ) #w- stick towards the west side.

        txt_regd=Entry(manage_frame, textvariable=self.regd_var, font = ("arial",12,"bold"), bd=5, relief=GROOVE) #Adding regd. No. text
        txt_regd.grid(row=1,columns=2,pady=10, padx =20, sticky = 'e' ) #e- stick towards the west side.

        label_name=Label(manage_frame,text='Name:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Name label
        label_name.grid(row=2,column=0,pady=10, padx =20, sticky = 'w' )

        txt_name=Entry(manage_frame, textvariable=self.name_var,font = ("arial",12,"bold"), bd=5, relief=GROOVE) #Name text
        txt_name.grid(row=2,columns=2,pady=10, padx =20, sticky = 'e' )

        label_email=Label(manage_frame,text='Email ID:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Email label
        label_email.grid(row=3,column=0,pady=10, padx =20, sticky = 'w' ) 

        txt_email=Entry(manage_frame, textvariable=self.email_var,font = ("arial",12,"bold"), bd=5, relief=GROOVE) #Email Text
        txt_email.grid(row=3,columns=2,pady=10, padx =20, sticky = 'e' )

        label_year=Label(manage_frame,text='Year:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Year label
        label_year.grid(row=4,column=0,pady=10, padx =20, sticky = 'w' )

        combox_year = ttk.Combobox(manage_frame, textvariable=self.year_var, font = ("arial",10,"bold"), state='readonly') #Drop-down menu initialisation, cannot be psuedo-written on the top (read-only state)
        combox_year['values'] = ('First Year','Second Year','Third Year') #Elements of the drop down menu
        combox_year.grid(row=4,columns=2,pady=10, padx = 25, sticky = 'e' )   

        # txt_issuedate=Entry(manage_frame, textvariable=self.issue_var,font = ("arial",15,"bold"), bd=5, relief=GROOVE) #Issue date Text
        # txt_issuedate.grid(row=5,columns=2,pady=10, padx =20, sticky = 'e' )

        # cal = DateEntry(root, width=50, year=2022, month=6, day=24, 
        # background='black', foreground='ivory3', borderwidth=2)
        # cal.pack(padx=15, pady=15)

        label_title=Label(manage_frame,text='Title',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Due date label
        label_title.grid(row=5,column=0,pady=10, padx =20, sticky = 'w' )

        txt_title=Entry(manage_frame, textvariable=self.title_var,font = ("arial",12,"bold"), bd=5, relief=GROOVE) #Due date text
        txt_title.grid(row=5,columns=2,pady=10, padx =20, sticky = 'e' )

        label_author=Label(manage_frame,text='Author',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Due date label
        label_author.grid(row=6,column=0,pady=10, padx =20, sticky = 'w' )

        txt_author=Entry(manage_frame, textvariable=self.author_var,font = ("arial",12,"bold"), bd=5, relief=GROOVE) #Due date text
        txt_author.grid(row=6,columns=2,pady=10, padx =20, sticky = 'e' )

        label_issuedate=Label(manage_frame,text='Issue Date:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #issue date label
        label_issuedate.grid(row=7,column=0,pady=10, padx =20, sticky = 'w' )

        issue_cal = DateEntry(manage_frame,textvariable = self.issue_date_var,fontwidth=10, year=2022, month=6, day=24, 
        background='black', foreground='ivory3', borderwidth=1)          
        issue_cal.grid(row=7,column=1,pady=10, padx =20, sticky = 'w' )

        label_duedate=Label(manage_frame,text='Due Date:',bg = 'ivory3', fg='black', font = ("arial",12,"bold")) #Due date label
        label_duedate.grid(row=8,column=0,pady=10, padx =20, sticky = 'w' )

        due_cal = DateEntry(manage_frame,textvariable = self.due_date_var,fontwidth=10, year=2022, month=6, day=24, 
        background='black', foreground='ivory3', borderwidth=1)          
        due_cal.grid(row=8,column=1,pady=10, padx =20, sticky = 'w' )



        # label_title=Label(manage_frame,text='Title',bg = 'ivory3', fg='black', font = ("arial",15,"bold")) #Due date label
        # label_title.grid(row=2,column=0,pady=10, padx =20, sticky = 'w' )

        # txt_title=Entry(manage_frame, textvariable=self.title_var,font = ("arial",15,"bold"), bd=5, relief=GROOVE) #Due date text
        # txt_title.grid(row=2,columns=2,pady=10, padx =20, sticky = 'e' )

        # label_author=Label(manage_frame,text='Author',bg = 'ivory3', fg='black', font = ("arial",15,"bold")) #Due date label
        # label_author.grid(row=2,column=0,pady=10, padx =20, sticky = 'w' )

        # txt_author=Entry(manage_frame, textvariable=self.author_var,font = ("arial",15,"bold"), bd=5, relief=GROOVE) #Due date text
        # txt_author.grid(row=2,columns=2,pady=10, padx =20, sticky = 'e' )






        #Click Buttons 
        #Creating a button frame inside the manage frame

        # button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg='ivory3')
        # button_frame.place(x=20,y=450, width=326)

        button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg='ivory3')
        button_frame.place(x=20,y=490, width=326)

        #Button to add records into database
        add_button = Button(button_frame, text='Add', width = 10, command=self.add_student).grid(row=0,column=0, padx=0, pady=10)

        #Button to update records into database
        update_button = Button(button_frame, text='Update', width = 10,  command=self.update_data).grid(row=0,column=1, padx=0, pady=10)

        #Button to delete records into database
        delete_button = Button(button_frame, text='Delete', width = 10, command=self.delete_data).grid(row=0,column=2, padx=0, pady=10)

        #Button to clear the text fields in the manage frame
        clear_button = Button(button_frame, text='Clear', width = 10, command=self.clear).grid(row=0,column=3, padx=0, pady=10)

        #Creating a data frame inside the main self root frame
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        detail_frame.place(x=500,y=100, width=800, height=560)

        #Creating a search variable Label

        label_search=Label(detail_frame,text='Search by:', bg = 'grey30', fg= 'white', relief  = RAISED, font = ("arial",12,"bold"))
        label_search.grid(row=0,column=0,pady=10, padx =20, sticky = 'w' )

        #Drop down menu using ttk module to filter search
        combox_search = ttk.Combobox(detail_frame,textvariable=self.search, width = 12, font = ("arial",15,"bold"), state='readonly')
        combox_search['values'] = ('Regd. No.','Name') # 'Issue Date','Due Date') 
        combox_search.grid(row=0,columns=1,pady=10, padx = 150, sticky = 'e' )

        #Text box to enable manual filtering
        txt_search=Entry(detail_frame, width = 10, textvariable=self.search_txt, font = ("arial",15,"bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0,columns=2,pady=10, padx =20, sticky = 'e' )
        search_button = Button(detail_frame, padx =3, pady=5, text='Search',command=self.search_data, width = 10).grid(row=0,column=3, padx=0, pady=10)
        show_all_button = Button(detail_frame, padx =3, pady=5, text='Show', command=self.fetch_data, width = 10).grid(row=0,column=4, padx=0, pady=10)
        #command= to assign reqd. functions to buttons

#Creating a tabular column showing the data records:
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg='black')
        table_frame.place(x=10,y=80, width=775, height=450)

#Adding a scrollbar to scroll through the records horizontally and vertically
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.stu_table=ttk.Treeview(table_frame, columns=("regd","name","email","year","Title","Author","Issue Dt.","Due Dt."), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) #defining a student table to scroll through student records

#Packing the scrollbars:
        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y)

#Assigning the scrollbars
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

#Adding columns to data frame
        self.stu_table.heading('regd', text='Regd. No.')
        self.stu_table.heading('name', text='Name')
        self.stu_table.heading('email', text='Email ID')
        self.stu_table.heading('year', text='Year')
        self.stu_table.heading('Author', text='Author')
        self.stu_table.heading('Title', text='Title')
        self.stu_table.heading('Issue Dt.', text='Issue Dt.')
        self.stu_table.heading('Due Dt.', text='Due Dt.')
        # stu_table.heading('Book', text='Book')
        # stu_table.heading('author', text='Author')
        # stu_table.heading('Due', text='Due Dt.')
        # stu_table.heading('issue', text='Issue Dt.')

        # stu_table.column('regd',width=100)
        # stu_table.column('name',width=100)
        # stu_table.column('email',width=100)
        # stu_table.column('year',width=100)

        self.stu_table.pack(fill=BOTH,expand=1) #packing the table

        self.stu_table.bind('<ButtonRelease-1>',self.get_cursor) #Callback function - binding a key with a value
        self.stu_table['show']='headings' 
        self.stu_table.pack()
        self.fetch_data() #Fetch data request

#Defining a function to add records 
    def add_student(self):
        if self.regd_var.get()==''or self.name_var.get()=='':
            #Error handling
            messagebox.showerror('Error','All the fields are required!')
        else:    
            #mysql connection with phylib database:
            con=pymysql.connect(host='localhost',user='root',password='', database="phylib") 

            #Cursor object executes the query and fetches data from the database

            cur=con.cursor() #Creates a cursor object
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.regd_var.get(),self.name_var.get(),self.email_var.get(),self.year_var.get(), self.title_var.get(),self.author_var.get(), self.issue_date_var.get(), self.due_date_var.get())) #Inserting values for the cursor object to fetch
            
            con.commit() #confirms (commits) the changes made
            self.fetch_data() #fetch data inside class
            self.clear() #Clears the cached views
            messagebox.showinfo('Sucess','Added succesfully')
        con.close() #Pop-up message

#Defining a function to fetch data from the database
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='', database="phylib")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall() #Fetches all the rows of the query result
        
        #Delete and insert, if the length of the row is not equal/not equal to zero.
        if len(rows) !=0: 
            self.stu_table.delete(*self.stu_table.get_children())
            for row in rows:
                self.stu_table.insert('', END, values=row)
            con.commit()
        con.close()   #close the mysql connection port 
#Defining a clear function 
    def clear(self):
        self.regd_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.year_var.set("")
        self.title_var.set("")
        self.author_var.set("")
        self.issue_date_var.set("")
        self.due_date_var.set("")

    def get_cursor(self, event): #event in any second argument
        cursor_row=self.stu_table.focus() #sets focus to desired widget
        contents=self.stu_table.item(cursor_row) #assigning content values
        row=contents['values'] #Transferring content values to the row
        ###print(row)

        #List indexing of row
        self.regd_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.year_var.set(row[3])
        self.title_var.set(row[4])
        self.author_var.set(row[5])
        self.issue_date_var.set(row[6])
        self.due_date_var.set(row[7])
        


        # con=pymysql.connect(host='localhost',user='root',password='', database="phylib")
        # cur=con.cursor()
        # cur.execute("select * from students where regd= %s",)
        # rows=cur.fetchall()
        # if len(rows) !=0:
        #     self.stu_table.delete(*self.stu_table.get_children())
        #     for row in rows:
        #         self.stu_table.insert('', END, values=row)
        #     con.commit()
        # con.close()    

#defining the update data function:
# #------------------NOT WORKING------------------
    def update_data(self):
        messagebox.showerror('Note','Feature coming soon!')    
        # con=pymysql.connect(host='localhost',user='root',password='', database="phylib")
        # cur=con.cursor()
        # # query="UPDATE students SET 'name=%s,email=%s,year=%s,regd = %s', WHERE" +str(self.name_var.get())+str(self.email_var.get())+str(self.year_var.get())+str(self.regd_var.get())

        # query = "UPDATE students SET name=%s, email=%s, year=%s, regd=%s, WHERE" % (self.name_var.get(), self.email_var.get(), self.year_var.get(), self.regd_var.get())
        
        # cur.execute(query)
    
        # print(cur.execute)


        # con.commit()
        # self.fetch_data()
        # self.clear()
        # con.close()

#Defining a delete data function:
    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='', database="phylib")
        cur=con.cursor()
        cur.execute("delete from students where regd=%s", self.regd_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

#Defining a search data function
    def search_data(self):
        messagebox.showerror('Note','Feature coming soon!')  
        # con=pymysql.connect(host='localhost',user='root',password='', database="phylib")
        # cur=con.cursor()
        # cur.execute("select * from students where"+str(self.search.get())+"LIKE '%"+str(self.search_txt.get())+"%'") #Search result filtering
        # rows=cur.fetchall()
        
        # if len(rows) !=0:
        #     self.stu_table.delete(*self.stu_table.get_children())
        #     for row in rows:
        #         self.stu_table.insert('', END, values=row)

        #     con.commit()
        # con.close()


root=Tk() #Root window creation
obj = student(root)
root.mainloop() #To execute the instructions in the program