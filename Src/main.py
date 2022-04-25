from tkinter import *
from tkinter import ttk
import time
import datetime
from PIL import ImageTk as ImageTk
from PIL import Image as Image
import os
import sqlite3 as sqlite3
from tkinter import messagebox
import login




now = datetime.datetime.now()
#----------- importing sqlite for server side operations---------------------------------------------------------------------------------
con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()
cur.execute("create table if not exists hoteld(t_r number,r_r number,t_s number)")
cur.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")

#pmethod=0

#rstatus extra column
#for i in range (1,21):
#cur.execute("update roomd set tv='Yes' where rn = ? ",(19,))
cur.execute("create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")
cur.execute("create table if not exists bookings(id number  primary key,f_name varchar,l_name varchar,phone_number number,email varchar, room_num number, day varchar, month varchar, year varchar, time varchar, payment_method varchar, user_id number, num_of_days number, totalamt varchar )")
#cur.execute("insert into paymentsf values(1,'Shubhank','Khare','9589861196','Shubhank7673@gmail.com',2,'1','11','2018','11:20:27 PM','Cash','3500')")
#cur.execute("alter table paymentsf add totalamt varchar")
con.commit()
#cur.execute("drop table paymentsf")
#cur.execute("insert into hoteld values(20,11,30)")
con.commit()
cur.execute("select * from payments")
con.commit()
x=cur.fetchall()
con.commit()

#----------- main project------------------------------------------------------------------------------------------------------------------
def main():
	sroot = Tk()
	app = login.login(sroot)
	sroot.mainloop()
if __name__ == '__main__':
    main()
	# mainroot()
#LD def call_mainroot():
#LD 	sroot.destroy()
#LD 	mainroot()
#LD sroot.after(3000,call_mainroot)
#LD mainloop()