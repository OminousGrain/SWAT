import socket
import threading
import requests
import os
import time
from bs4 import BeautifulSoup
from queue import Queue

print(
	"\n ______     __     __     ______     ______  \n"
	"\n/\  ___\   /\ \  _ \ \   /\  __ \   /\__  _\ \n"
	'\n\ \___  \  \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \n'
	'\n \/\_____\  \ \__/".~\_\  \ \_\ \_\    \ \_\ \n'
	"\n  \/_____/   \/_/   \/_/   \/_/\/_/     \/_/ \n"
)
print("Security. Web.Analysis. Tool\n\n[1]H2IP\n[2]PScan\n")
print("Select Program")
x = input(">>>")

if x == '1':
    os.system('cls')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(
	"\n ____  ____   _____   _____  _______   \n"
	"\n|_   ||   _| / ___ `.|_   _||_   __ \  \n"
	"\n  | |__| |  |_/___) |  | |    | |__) | \n"
	"\n  |  __  |   .'____.'  | |    |  ___/  \n"
	"\n _| |  | |_ / /_____  _| |_  _| |_     \n"
	"\n|____||____||_______||_____||_____|    \n"
	)
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
else:
 print("[!]Error[!]")

if x == '2':
 print_lock = threading.Lock()
 os.system('cls')
 print(
	'\n______  _____                 \n'
	'\n| ___ \/  ___|                \n'
	'\n| |_/ /\ `--.  _____  ___ __  \n'
	"\n|  __/  `--. \/ __\ \/ / '_ \ \n"
	'\n| |    /\__/ / (__ >  <| | | |\n'
	'\n\_|    \____/ \___/_/\_\_| |_|\n'
 )
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
else:
 print("[!]Error[!]")

if x == '3':
     pass
#    os.system('cls')
#    print(
#			"\n   _____                       __  \n"
#			"\n  / ___/_________ __________ _/ /_ \n"
#			"\n  \__ \/ ___/ __ `/ ___/ __ `/ __ \\n"
#			"\n ___/ / /__/ /_/ / /  / /_/ / /_/ /\n"
#			"\n/____/\___/\__,_/_/   \__,_/_.___/ \n"
#		)
#    print("Crawl The Web...catch your prey\n")
#    print("Enter Site To Crawl")
#    xs = input(">>>")
#    page = requests.get(xs)
#    soup = BeautifulSoup(page.text, 'html.parser')

#    last_links = soup.find(class_='AlphaNav')
#    last_links.decompose()
#    artist_name_list = soup.find(class_='BodyText')
#    artist_name_list_items = artist_name_list.find_all('a')

#    for artist_name in artist_name_list_items:
#     names = artist_name.contents[0]
#     print(names)
#else:
# print("[!]Error has occured")
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxies = get_proxies()
proxy_pool = cycle(proxies)

url = 'https://httpbin.org/ip'
for i in range(1,11):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
        print("Skipping. Connnection error")
        
        
if x == 'h':
    print(
		"\n______  __    ______        \n"
		"\n___  / / /_______  /_______ \n"
		"\n__  /_/ /_  _ \_  /___  __ \ \n"
		"\n_  __  / /  __/  / __  /_/ /\n"
		"\n/_/ /_/  \___//_/  _  .___/ \n"
		"\n                   /_/      \n\n\n"
	)
    print("[h] - Displays Help Menu\n")
    print("[1]/H21P - Gives the IP address for a specified URL\n")
    print("[2]/PScan - Scans for open ports on specified website/ip address")
#    print("[3]/Scarab - Crawls a specified website and outputs items")
else:
 print("[!]Error has occured")
