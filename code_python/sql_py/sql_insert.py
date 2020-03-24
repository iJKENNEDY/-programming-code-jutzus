import sqlite3

with sqlite3.connect("Phone.db") as db:
	cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
	id integer PRIMARY KEY,
	firstname text,
	surname text,
	phonenumber text);""")
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("1","Kenneth","Kennedhy","893201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("2","Ramik","Lockwer","321201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("3","Oprha","Huston","444201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("4","Jonas","Dybal","222201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("5","Lana","Enskin","122201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("6","Koby","Nash","900201231")""")
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
	VALUES("7","Promaski","Quillpo","999201231")""")
db.commit()
db.close()

##===================================##
import sqlite3

def viewphonebook():
	cursor.execute("SELECT * FROM Names")
	for x in cursor.fetchall():
		print(x)

def addtophonebook():
	newid = int(input("Enter ID: "))
	newfname = input("Enter first name: ")
	newsname = input("Enter surname: ")
	newpnum = input("Enter phone number: ")
	cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber)
	VALUES (?,?,?,?)""",(newid,newfname, newsname,newpnum))
	db.commit()

def selectname():
	selectsurname = input("Enter a surname: ")
	cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
	for x cursor.fetchall():
		print(x)

def deletedata():
	selectid = int(input("Enter ID: "))
	cursor.execute("DELETE FROM Names WHERE id = ?",[selectid])
	cursor.execute("SELECT * FROM Names")
	for x in cursor.fetchall():
		print(x)
	db.commit()

with sqlite3.connect("PhoneBook.db") as db:
	cursor = db.cursor()


def main():
	again = "y"
	while again == "y":
		print()
		print("Main Menu")
		print()
		print("1) View phone book")
		print("2) Add to phone book")
		print("3) Search for surname")
		print("4) Delete person from phone book")
		print("5) Quit")
		print()
		selection = int(input("Enter your selection: "))
		print()

		if selection == 1:
			viewphonebook()
		elif selection == 2:
			addtophonebook()
		elif selection == 3:
			selectname()
		elif selection == 4:
			deletedata()
		elif selection == 5:
			again = "n"
		else:
			print("Incorrect selection entered")
main()
db.close()