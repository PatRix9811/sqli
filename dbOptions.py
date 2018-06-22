import sqlite3

class DB:
	activeDb =''
	cursorDb=''
	nameDb=""
	contentDb=""
	b=[]
	
	def connect(self,name):
		self.nameDb=name
		self.activeDb = sqlite3.connect(self.nameDb+".db")
		self.cursorDb = self.activeDb.cursor()
		try:
			self.cursorDb.execute("CREATE TABLE {} (Imię text,Nazwisko text,Wiek text)".format(self.nameDb))
			self.activeDb.commit()
		except:
			return
			
		
	def disconnect(self):
		try:
			self.activeDb.close()
			self.cursorDb=''
		except:
			print("[!] Database is not open")
		
	def getData(self):
		data=()
		for row in self.cursorDb.execute("SELECT * FROM {}".format(self.nameDb)):
			data+=row
		return data
		
	def addRecord(self,un,us,ua):
		try:
			query ="INSERT INTO {} VALUES ('{}','{}','{}')".format(self.nameDb,un,us,ua)
			self.cursorDb.execute(query)
			self.activeDb.commit()
		except:
			print("[!] Record was not added")
			
	def delRecord(self,where,like):
		try:
			query ="DELETE FROM {} WHERE {} = '{}'".format(self.nameDb,where,like)
			self.cursorDb.execute(query)
			self.activeDb.commit()
		except:
			print("[!] Record was not deleted")
			
		