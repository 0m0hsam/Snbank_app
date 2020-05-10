from __future__ import print_function
import os, os.path
import re
from datetime import datetime
import random

print("Welcome to Snbank")
print("Enter Yes/No to use our bank app")
print("Enter STAFF for Staff Login")
print("Enter NEW to Create Staff Account")
print("Enter END to Close App\n")
user=input("Enter here: ").lower()
new_staff=" "
staff_data=" "
password=" "
not_loggedin=" "
new_staff=" "
path = '.'
name=" "
files=" "
if user== "end" :
	print("Thank you for using our bank app")
	exit()
	
elif  user == "new" :
	print("Welcome staff")

	username=input("Enter Username:")
	save_path='staff/'
	newfile_staff= os.path.join(save_path,username+".txt")  
	f= open(newfile_staff,"w+")
	f.write(f"Username : {username}\n")
	password=input("Enter Password:")
	f.write(f"Password : {password}\n")
	email=input("Enter Email:")
	f.write(f"Email: {email} \n")	
	fullname=input("Enter Fullname:")
	f.write(f"Fullname : {fullname} \n")
	f.close()
	print(f"{fullname} Welcome to Snbank \nDo you want to Sign in\nYes or No")
	new_staff=input().lower()
if user == "staff" or new_staff == "yes":
	print("Snbank Staff Login")
	username=input("Enter Username:")
	Password=input("Enter password:")
	#username=re.sub
	save_path='staff/'
	newfile_staff= os.path.join(save_path,username+".txt")  
	#read staff database
	f=open(newfile_staff,"r")
	data=f.readlines()
	for staff_data in data :
		username_ok = re.findall(username, staff_data)
		password_ok= re.findall(Password, staff_data)		
	if not password_ok:
		not_loggedin=True
		print("password not correct")
	else :
		not_loggedin=False
	f.close
		
if not_loggedin == False :
	dateTimeObj = datetime.now()
	print(f"Welcome {username} you have successfully logged in\n")
	print(f"Login Time : {dateTimeObj}")
	print("Which of our service would you like to use\n")
	print("\nEnter 1 to Open a bank account")
	print("\nEnter 2 to Check Your Bank Account")
	print("\nEnter 3 to Close Bank App")
	bank_user=input("\nEnter here: ").lower()
	if bank_user == "3" :
		print("Thank you for using Snbank App")
		exit()
	bank_user=re.sub(" ","",bank_user)
	if bank_user == "1":
		acct_name=input("\nEnter Account Name: ")
		open_bal=input("Enter Account Opening Balance: ")
		acct_type=input("Enter Account Type: ")
		acct_email=input("Enter Email: ")		
		acct=" "
		#Search account number
		path = 'customers/.'
		files = os.listdir(path)
		total_acct=len(files)+1
		random.seed(total_acct)
		acct=random.random()
		acct=str(acct)
		slice_object = slice(-1, -11, -1)
		new_account=acct[slice_object]
		save_path='customers/'
		new_file = os.path.join(save_path, new_account+".txt")         
		f=open(new_file,"w+")
		print(f"\n{acct_name} your new account number : {new_account}")
		
		f.write(f"Account Number: {new_account} \n")
		f.write(f"Account Name: {acct_name} \n")
		f.write(f"Account Email: {acct_email} \n")
		f.write(f"Opening Balance: {open_bal} \n")
		f.write(f"Account Type: {acct_type} \n")
		f.close
		print(f"\n{acct_name} You have successfully open your bank account")
	if bank_user == "2":
		#To check account balance
		acct_number=re.sub(" ","",input("\nEnter Account Number: "))
		acct_name=input("\nEnter Account Name: ")
	#Search account number
		path = 'customers/.'
		files = os.listdir(path)
		for name in files:
			if (f"{acct_number}.txt") == name :
				print(f"{acct_name} your acct details\n")			
#read account details from database
				save_path='customers/'
				newfile= os.path.join(save_path, name)  

				f=open(newfile,"r")
				data=f.readlines()
				for data in data :	
					print(data)
					f.close
user_end=(" ","",input(f"""   	  {username}
	To Logout enter 0
	To return to main menu enter 1
	                       """))
if user_end== "0" :
	print("Thank you for using Snbank App")
	exit()
