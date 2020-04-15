import sqlite3 

db = sqlite3.connect("bank_database.db") #create the file of database(database handle)
db.execute("drop table if exists client_data") # The DROP TABLE statement deletes the specified table(client_data), and any data associated with it, from the database. The IF EXISTS clause allows the statement to succeed even if the specified tables does not exist. If the table does not exist and you do not include the IF EXISTS clause, the statement will return an error.
db.execute("create table client_data(name text, acc_id int, money_value real)") # create a table(client_data) inside my database

# to insert values
def insert_c():
	c_name = input("ُEnter client first & last name: ")
	c_acc_number = input("Enter client account number: ")
	c_money_value = input("Enter Money Value: ")
	db.execute("insert into client_data (name, acc_id, money_value) values (?, ?, ?)", (c_name, c_acc_number, c_money_value))
	db.commit()

# create an iterator(cursor) that has all the rows
def show_all():
	cursor = db.execute("select * from client_data")
	for row in cursor: # each row is a tuple
		print(row)

# retreave~ one row
def show_c():
	c_acc_number = input("Enter client account number: ")
	cursor = db.execute("select * from client_data where acc_id = ?", (c_acc_number,))
	print(cursor.fetchone())

# to delete rows 
def del_c():
	c_acc_number = input("Enter client account number: ")
	db.execute("delete from client_data where acc_id = ?", (c_acc_number,))
	db.commit()

# update a cirten~ row
def update_c():
	c_acc_number = input("Enter client account number: ")
	new_money_value = input("Enter the new money value: ")
	db.execute('update client_data set money_value = ? where acc_id = ?', (new_money_value, c_acc_number))
	db.commit()
