import socket
import threading
import os
from queue import Queue
import time


print('_____  _    _   ___  _____ \n')
print('/  ___|| |  | | / _ \|_   _|\n')
print('\ `--. | |  | |/ /_\ \ | |  \n')
print('`--. \| |/\| ||  _  | | |  \n')
print('/\__/ /\  /\  /| | | |_| |  \n')
print('\____(_)\/  \(_)_| |_(_)_/  \n')
print("Security.Web.Analysis.Tool\n\n[1]Host2IP\n[2]PScan\n")
print("Select Program")
x = input(">>>")
          
if x == 1:
  pass
if x == 2:
print_lock = threading.Lock()
os.system('cls')
print("Enter Site")
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
