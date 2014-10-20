from Tkinter import *
import ttk
import os 
import serial
import time
import MySQLdb as mdb
from time import sleep
from compiler.pycodegen import EXCEPT


def check():
	global shutdown
	shutdown = connection(1)
	global restart
	restart = connection(2)
	global logout
	logout = connection(3)
	global lock
	lock = connection(4)
	global connect
	connect = connection(5)
	global switch
	switch = connection(6)
	global hibernate
	hibernate = connection(7)
	if(shutdown == "shutdown"):
		shutdown()
	elif(restart == "restart"):
		Restart()
	elif(logout == "logout"):
		Logout()
	elif(lock == "lock"):
		Lock()
	elif(hibernate == "hibernate"):
		Hibernate()
	elif(switch == "switch_on"):
		Switch_on()
	elif(switch == "switch_off"):
		Switch_off()
	
		#hibernate()

	print("Check")
	sleep(5)
	check()



def con():
	con = mdb.connect('host', 'db_user', 'db_password', 'db_name')
	        
	with con: 
		cur = con.cursor()
	   	return cur

#Connection to the global database
def connection(id):

	cur = con()
	try:
		cur.execute("UPDATE module SET action = %s WHERE Id = %s", 
	        	("connect", "5"))
		cur.execute("SELECT action FROM module WHERE id = %s" %(id))
			
		rows = cur.fetchall()
				
		for row in rows:
			result = row[0]
			cur.close()
			return result
	except:
		print("Check DataBase Connection or Contact Tanusha")
		check()
		
				# disconnect from server
				
	#print("Connection")


		#Create Status Code and the Reset Code
def status_reset(value, st):
		cur = con()
		cur.execute("UPDATE module SET action = %s WHERE Id = %s", 
        (value, st))
		sleep(1)
		#status of the Pc as on

		#status hibernate as not_hibernate

		#status shutdown as not_shutdown

		#status logout as not_logout

		#status logoff as not_lock

		#Reset Done
			




	#Restart
def shutdown():
		#send the shutdown code to database
	status_reset("not_shutdown", "1")
		#shutdown
	os.system("shutdown -s -t 00")	


	#Restart
def Restart():
		#send restart code to server
	status_reset("not_restart", "2")
		#Restart

	os.system("shutdown -r -t 00")

	#Logout
def Logout():
		#send logout code to server
	status_reset("not_logout", "3")
		#logout
	os.system("shutdown -f -l")

	#Logoff
def Lock():
	sleep(3)
	status_reset("not_lock", "4")
	print("Hi")

	
			#lock
			#os.system("shutdown -r -t 00")
	
		#Hibernate
def Hibernate():
		#send hibernate code to server
		#hibernate
	status_reset("not_hibernate", "7")
	os.system("shutdown -h")

	#switchon
def Switch_on():
		#send switch on to server

		#on
	ser.write("off")
	#print("Switch On")

	#switch off
def Switch_off():
		#send off to server

		#off
	ser.write("on")
	#print("Switch Off")



class automation:
	def __init__(self, master):
		self.label_main = ttk.Label(master, text = "Control Panel")
		self.label_main.grid(row = 1, column = 1, columnspan = 2, rowspan = 3)
		self.bt1 = ttk.Button(master, text = "Control on", command = Switch_on)
		self.bt1.grid(row = 2, column = 0)
		self.bt2 = ttk.Button(master, text = "Control off", command = Switch_off)
		self.bt2.grid(row = 2, column = 1)
		check()

def main():
	root = Tk()
	global ser
	ser = serial.Serial("COM15", 9600)
	#print("Doen")
	#print("Please Connect the Arduino")	
	app = automation(root)
	root.mainloop()
	#db.close()
if __name__ == "__main__" : main()
