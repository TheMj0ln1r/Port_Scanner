from banner import *
banner()
import sys
import socket
import re 
import threading
from platform import system
import subprocess
target_ip = ""

def islive():
	try:
		if "Linux" in system():
			p = subprocess.run(["ping","-c","1",target_ip],capture_output=True,text=True)
			if p.returncode == 0:
				return True

		if "Windows" in system():
			p = subprocess.run(["ping","-n","1",target_ip],capture_output=True,text=True)
			if p.returncode == 0:
				return True

	except subprocess.CalledProcessError:
		return False

def input_check(start_port,end_port):
	global target_ip
	ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',target_ip)
	if not ip:
		try :
			target_ip = socket.gethostbyname(target_ip)
		except socket.gaierror :
			print("Unable resolve host address")
			sys.exit()
	if ((start_port < 1) or (end_port > 65535)):
		print("Port numbers are invalid.. \n")
		sys.exit()

def single_port(port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		status = s.connect_ex((target_ip,port))
		if(not status):
			print("\tOpen port ",port)
			s.close()
		s.close()

def single_host_scan(start_port,end_port):

	if islive():
		for port in range(start_port,end_port+1):
			thread = threading.Thread(target = single_port,args = (port,))
			thread.start()
			thread.join()
	else:
		print("\t Not reachable.\n")

def host_check(start_host,end_host):
	if (start_host < 1 or end_host > 255):
		print("Host range in not valid..\n")
		sys.exit()
def multi_host_scan(start_host,end_host,start_port,end_port):
	global target_ip
	tmp = target_ip
	ip = tmp.split(".")
	ip = ".".join(ip[0:3])+"."
	for host in range(start_host,end_host+1):
		target_ip = ip + str(host)
		print("Scannig Host : "+target_ip+"\n")
		single_host_scan(start_port,end_port)
	sys.exit()
def main():

	print("""
	1 > Scan one device
	2 > Scan Entire network
		""")
	choice = int(input("Enter your choice(1/2) : "))

	if choice == 1:

		print("Scanning only one target.. \n")
		global target_ip
		target_ip = input("Enter Target IP or URL : ")

		start_port = int(input("Enter start port : "))
		end_port = int(input("Enter end port : "))
		
		input_check(start_port,end_port)
		single_host_scan(start_port,end_port)
		sys.exit()
	elif choice == 2:

		print("Scanning Entire Network..\n")
		target_ip = input("Enter your IP address : ")
		start_host = int(input("Enter start host : "))
		end_host = int(input("Enter end host : "))
		start_port = int(input("Enter start port : "))
		end_port = int(input("Enter end port : "))
		
		input_check(start_port,end_port)
		host_check(start_host,end_host)
		multi_host_scan(start_host,end_host,start_port,end_port)
		sys.exit()
	else :
		print("Invalid choice.")
		sys.exit()
main()