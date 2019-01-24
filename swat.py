import socket
import threading
import os
from queue import Queue
import time


print('███████╗   ██╗    ██╗    █████╗ ████████╗\n')
print('██╔════╝   ██║    ██║   ██╔══██╗╚══██╔══╝\n')
print('███████╗   ██║ █╗ ██║   ███████║   ██║   \n')
print('╚════██║   ██║███╗██║   ██╔══██║   ██║   \n')
print('███████║██╗╚███╔███╔╝██╗██║  ██║██╗██║   \n')
print('╚══════╝╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝   \n')
print("Security.Web.Analysis.Tool\n\n[1]H2IP\n[2]PScan\n")
print("Select Program")
x = int(input(">>>"))
          
if x == 1:
  os.system('cls')
  print(" ____  ____   _____   _____  _______   \n")
  print("|_   ||   _| / ___ `.|_   _||_   __ \  \n")
  print("  | |__| |  |_/___) |  | |    | |__) | \n")
  print("  |  __  |   .'____.'  | |    |  ___/  \n")
  print(" _| |  | |_ / /_____  _| |_  _| |_     \n")
  print("|____||____||_______||_____||_____|    \n")
  print("Host 2 IP\nTake a sites URL and outputs its IP address\n\n")
  print("Enter Host)
  target = input(">>>")
  ip = socket.gethostbyname(target)
  print(ip)
        
if x == 2:
print_lock = threading.Lock()
os.system('cls')
print('▀▀▄▀▀▀▄  ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄ \n')
print('█   █   █ █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █  █ █ █ \n')
print('▐  █▀▀▀▀     ▀▄   ▐ █        █▄▄▄█ ▐  █  ▀█ \n')
print('   █      ▀▄   █    █       ▄▀   █   █   █  \n')
print('   █      ▀▄   █    █       ▄▀   █   █   █  \n')
print(' ▄▀        █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  ▄▀   █   \n')
print('█          ▐      █     ▐  ▐   ▐   █    ▐   \n')
print('▐                 ▐                ▐        \n')
print("PScan. Your average threaded socket port scanner.\n")
print("Enter Target Site")
target = input(">>>")
ip = socket.gethostbyname(target)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
        
q = Queue()

for x in range(30):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()
    
start = time.time()
for worker in range(1,100):
    q.put(worker)
    
q.join()
