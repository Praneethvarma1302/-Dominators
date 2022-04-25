from tkinter import *
from tkinter import messagebox
import sqlite3
import app

f = ('Times', 14)

con = sqlite3.connect('hm_proj.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS user(
                    id number primary key,
                    name text, 
                    email text, 
                    contact number, 
                    gender text, 
                    password text,
                    superAdmin boolean
                )
            ''')
con.commit()



def insert_user(register_name,register_email,register_mobile,var,register_pwd,pwd_again):
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 7:        
        try:
            con = sqlite3.connect('hm_proj.db')
            cur = con.cursor()
            cur.execute("select id from user order by id desc")
            x = cur.fetchone()
            if x is None:
                cid = 0
            else:
                cid = int(x[0])
            cid+=1
            cur.execute("INSERT INTO user VALUES (:id, :name, :email, :contact, :gender, :password, :superAdmin)", {
                            'id': cid,
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'password': register_pwd.get(),
                            'superAdmin': False

            })
            con.commit()
            messagebox.showinfo('confirmation', 'user Saved')
            return "successs"

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

def login_response(email_tf, pwd_tf, ws):
    
    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        try:
            con = sqlite3.connect('hm_proj.db')
            c = con.cursor()
            username = None
            pwd = None
            login_id = None
            for row in c.execute("Select * from user where email = ? and password = ?",(uname,upwd)):
                print(row)
                login_id = row[0]
                username = row[2]
                pwd = row[5]
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
                ws.destroy()
                print(login_id)
                app.mainroot(login_id)
                return "trueeeeeeeeeeeee"
            else:
                messagebox.showerror('Login Status', 'invalid username or password, If you dont have registered user please register')
            
        except Exception as ep:
            messagebox.showerror('', ep)
        
    else:
        messagebox.showerror('', warn)


def login_widget(ws):
    left_frame = Frame(ws, bd=2, bg='#CCCCCC',  relief=SOLID, padx=10, pady=10)

    Label(left_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)

    Label(left_frame, text="Enter Password", bg='#CCCCCC',font=f).grid(row=1, column=0, pady=10)

    email_tf = Entry(left_frame, font=f)
    pwd_tf = Entry(left_frame, font=f,show='*')
    login_btn = Button(left_frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=lambda:login_response(email_tf,pwd_tf,ws))
    # widgets placement
    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.place(x=50, y=50)


# widgets
def register_widget(ws):
    var = StringVar()
    var.set('male')
    right_frame = Frame(ws, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)

    Label(right_frame, text="Enter Name", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)

    Label(right_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

    Label(right_frame, text="Contact Number", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)

    Label(right_frame, text="Select Gender", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)

    Label(right_frame, text="Enter Password", bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)

    Label(right_frame, text="Re-Enter Password", bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)

    gender_frame = LabelFrame(right_frame,bg='#CCCCCC',padx=10, pady=10,)

    register_name = Entry(right_frame, font=f)

    register_email = Entry(right_frame, font=f)

    register_mobile = Entry(right_frame, font=f)

    male_rb = Radiobutton(gender_frame, text='Male',bg='#CCCCCC',variable=var,value='male',font=('Times', 10))
    female_rb = Radiobutton(gender_frame,text='Female',bg='#CCCCCC',variable=var,value='female',font=('Times', 10))
    others_rb = Radiobutton(gender_frame,text='Others',bg='#CCCCCC',variable=var,value='others',font=('Times', 10))

    register_pwd = Entry(right_frame, font=f,show='*')
    pwd_again = Entry(right_frame, font=f,show='*')

    register_btn = Button(right_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',
                command=lambda:insert_user(register_name,register_email,register_mobile,var,register_pwd,pwd_again))
    # widgets placement
    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_btn.grid(row=7, column=1, pady=10, padx=20)
    right_frame.place(x=500, y=50)

    gender_frame.grid(row=3, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=LEFT)
    female_rb.pack(expand=True, side=LEFT)
    others_rb.pack(expand=True, side=LEFT)

def login(ws):
    ws.title('Login Page')
    ws.geometry('940x500')
    ws.config(bg='#0B5A81')
    login_widget(ws)
    register_widget(ws)
    # ws.mainloop()
    return 

