import socket
import threading
import os
import time
from queue import Queue

print(" ______     __     __     ______     ______  ")
print("/\  ___\   /\ \  _ \ \   /\  __ \   /\__  _\ ")
print('\ \___  \  \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ ')
print(' \/\_____\  \ \__/".~\_\  \ \_\ \_\    \ \_\ ')
print("  \/_____/   \/_/   \/_/   \/_/\/_/     \/_/ ")
print("Security. Web.Analysis. Tool\n\n[1]H2IP\n[2]PScan\n")
print("Select Program")
x = int(input(">>>"))

if x == 1:
    os.system('cls')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(" ____  ____   _____   _____  _______   ")
    print("|_   ||   _| / ___ `.|_   _||_   __ \  ")
    print("  | |__| |  |_/___) |  | |    | |__) | ")
    print("  |  __  |   .'____.'  | |    |  ___/  ")
    print(" _| |  | |_ / /_____  _| |_  _| |_     ")
    print("|____||____||_______||_____||_____|    ")
    print("Host 2 IP\nTake a sites URL and outputs its IP address\n\n")
    print("Enter Host")
    server = input(">>>")
    #print("Specify Port")
    #port = int(input(">>>"))
    server_ip = socket.gethostbyname(server)
    print("The sites IP address is : " + server_ip)
    #request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
    #s.connect((server, port))
    #s.send(request.encode())
    #results = s.recv(1024)
    #print(results)
if x == 2:
 print_lock = threading.Lock()
 os.system('cls')
 print('______  _____                 ')
 print('| ___ \/  ___|                ')
 print('| |_/ /\ `--.  _____  ___ __  ')
 print("|  __/  `--. \/ __\ \/ / '_ \ ")
 print('| |    /\__/ / (__ >  <| | | |')
 print('\_|    \____/ \___/_/\_\_| |_|')
 print("PScan. Your average threaded socket port scanner.\n")
 print("Enter Target Site")
 target = input(">>>")
 ip = socket.gethostbyname(target)

 def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port)
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

 for worker in range(1, 100):
    q.put(worker)

 q.join()
