from tkinter import Tk, Entry, mainloop, Label, Button, Listbox, Frame
from dbOptions import *

def destroy():
	for child in frame.winfo_children():
		child.destroy()

def reloadTable():
	data=base.getData()
	e=0
	l0=Label(frame,text="Id").grid(row=2,column=0)
	l1=Label(frame,text="Imię",width=15).grid(row=2,column=1)
	l2=Label(frame,text="Nazwisko",width=15).grid(row=2,column=2)
	l3=Label(frame,text="Wiek",width=15).grid(row=2,column=3)
	if len(data)>0:
		r=int(len(data)/4)
		for i in range(r):  # Rows
			for j in range(4):  # Columns
				b = Entry(frame)
				b.grid(row=i+3, column=j)
				b.insert("0",str(data[e]))
				e+=1

def conn():
	name = dbName.get()
	if len(name) >0:
		try:
			base.connect(name)
			window.title(name+".db")
			
		except:
			print("[!] Connect Error")
			
		reloadTable()
		
def disc():
	base.disconnect()
	window.title('sqlite')
	destroy()
		
def addRec():
	un =userName.get()
	us = userSurname.get()
	ua = userAge.get()
	if len(dbName.get())>0:
		conn()
		
	if len(un)>0 or len(us)>0 or len(ua)>0:
		base.addRecord(un,us,ua)
		reloadTable()
		
def delRec():
	opotions=("Id","Imię","Nazwisko","Wiek") 
	h1=record.curselection()
	lb = opotions[h1[0]]
	e=where.get()
	try:
		base.delRecord(lb,e)
	except:
		print("[!] Record was not deleted")
	
	destroy()
	reloadTable()
		

window = Tk()
window.title('sqlite')
frame1 = Frame(window)
frame = Frame(window)
base = DB()

name = Label(frame1,text="Nazwa bazy:")
dbName = Entry(frame1)
user = Label(frame1,text="Imię:")
userName = Entry(frame1)
surname = Label(frame1,text="Nazwisko:")
userSurname = Entry(frame1)
age = Label(frame1,text="Wiek:")
userAge = Entry(frame1)

createDb = Button(frame1,text="Nowa Baza/Połącz",command=conn)
disconnect = Button(frame1,text="Rozłącz",command=disc)
addRecord = Button(frame1,text="Nowy Rekord",command=addRec)
deleteRecord = Button(frame1,text="Usuń Rekord gdzie ->",command=delRec)

record = Listbox(frame1,height=4)
record.insert(1,"Id")
record.insert(2,"Imię")
record.insert(3,"Nazwisko")
record.insert(4,"Wiek")

l=Label(frame1,text="=")
where = Entry(frame1)
		
		
name.grid(row=0,column=0)
dbName.grid(row=0,column=1)
user.grid(row=0,column=2)
userName.grid(row=0,column=3)
surname.grid(row=0,column=4)
userSurname.grid(row=0,column=5)
age.grid(row=0,column=6)
userAge.grid(row=0,column=7)
createDb.grid(row=1,column=0)
disconnect.grid(row=1,column=1)
addRecord.grid(row=1,column=2)
deleteRecord.grid(row=1,column=3)
record.grid(row=1,column=4)
l.grid(row=1,column=5)
where.grid(row=1,column=6)
frame1.grid(row=0)
frame.grid(row=2)

mainloop()