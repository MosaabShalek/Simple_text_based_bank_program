"""
This is text base bank program
"""

from MSK_Bank import *
from random import randint
from database_funcs import *


while True:
	x = input("1 to entering a new client\n2 to delete client\n3 to show all\n enter here: ")
	if x == "1":
		insert_c()
	elif x == "2":
		del_c()
	elif x == "3":
		show_all()
	else:
		print("wrong entry!! \nPlz try again")