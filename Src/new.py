from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
root = Tk()
root.title("Login System")
root.resizable(1000,1000)
bg = Image.open('Images/Amrita.png')
bg1 = Image.open('Images/ATTENDANCE MANAGEMENT SYSTEM.png')
bg2 = Image.open('Images/login.png')
newsize = (300, 120)
bg = bg.resize(newsize)
bg2 = bg2.resize((400,400))
bg = ImageTk.PhotoImage(bg)
bg1 = ImageTk.PhotoImage(bg1)
bg2 = ImageTk.PhotoImage(bg2)
def new():
    if user_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get()=="" and password_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    else:
        name = user_entry.get()
        password = password_entry.get()
        conn = connect()
        cur = conn.cursor()
        query ='SELECT roll,password from public."studentData" where roll=\''+name+'\';'
        print(query)
        cur.execute(query)
        data = cur.fetchone()
        print(data)
        if data==None:
            messagebox.showinfo("Login System", 'Incorrect username or password')
        elif data[0]==name and data[1]==password:
            
            messagebox.showinfo("Login System", 'Logged in Successfully')
            root.withdraw()
            paswd.set("")
            new_window = Toplevel(root)
            def home_page():
                new_window.withdraw()
                root.deiconify()
                    
                home = Button(new_window, text="Go to Login page", font=("Ariel 22 bold"), relief=GROOVE, bd=2, command=home_page)
                home.pack(padx=30, pady=30)
        else:
            messagebox.showinfo('Incorrect username or password')

        
        # close the communication with the PostgreSQL
        cur.close()
        

        
        
canvas = Canvas(root, width=1200, height=700, bg='#FFFFFF',bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(0, 0, 600, 700, fill='#503284', outline='white')
canvas.create_image(770, 30, image=bg, anchor='nw')
canvas.create_image(700, 250, image=bg1, anchor='nw')
canvas.create_image(0, 0, image=bg2, anchor='nw')

user_label = Label(root, text="Username ", font=("Ariel 20 bold"),bg='#503284', fg='white')
canvas.create_window(80, 250, anchor="nw", window=user_label)
user_entry = Entry(root, font=("Ariel 18 bold"))
user_entry.focus()
canvas.create_window(80, 300, anchor="nw", window=user_entry)
password_label = Label(root, text="Password ", font=("Ariel 20 bold"),bg='#503284', fg='white')
canvas.create_window(80, 360, anchor="nw", window=password_label)
paswd=StringVar()
password_entry = Entry(root, textvar=paswd, font=("Ariel 18 bold"), show="*")
canvas.create_window(80, 410, anchor="nw", window=password_entry)
login = Button(root, text="Log In", font=("Ariel 22 bold"),
               width=8, bg="white", fg='#FFC331', relief=FLAT, command=new)
canvas.create_window(180, 500, anchor="nw", window=login)
root.mainloop()