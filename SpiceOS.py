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
    import requests
    import shodan
    from proxyscrape import create_collector, get_collector
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
    print("\n\n")
    consolemessage("Powering Off . . .")
    time.sleep(3)
    exit()



banner = """\u001b[38;5;226m                                                                                             
  ██████  ██▓███   ██▓ ▄████▄  ▓█████     ▒█████    ██████ 
▒██    ▒ ▓██░  ██▒▓██▒▒██▀ ▀█  ▓█   ▀    ▒██▒  ██▒▒██    ▒ 
░ ▓██▄   ▓██░ ██▓▒▒██▒▒▓█    ▄ ▒███      ▒██░  ██▒░ ▓██▄   
  ▒   ██▒▒██▄█▓▒ ▒░██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒██   ██░  ▒   ██▒
▒██████▒▒▒██▒ ░  ░░██░▒ ▓███▀ ░░▒████▒   ░ ████▓▒░▒██████▒▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▓  ░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░▒ ░      ▒ ░  ░  ▒    ░ ░  ░     ░ ▒ ▒░ ░ ░▒  ░ ░
░  ░  ░  ░░        ▒ ░░           ░      ░ ░ ░ ▒  ░  ░  ░  
      ░            ░  ░ ░         ░  ░       ░ ░        ░  
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
        print("\nScanning ports for \u001b[38;5;208m" + str(ip) + "\u001b[0m...")
        r = requests.get('http://api.hackertarget.com/nmap/?q=' + ip)
        r = r.text[69:]
        print("\n" + r.title())
        print('- Scan Finished -')
        input("Press ENTER To Go Back.")

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

import ftplib
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
        print("[\u001b[38;5;208mCB\u001b[0m]\u001b[38;5;200m─►\u001b[0m " + str(message))



def clear():
        print("\n" * 300)


def boot():
        



        for line in Lines:
                print(line.strip())
                time.sleep(0.01)
#        print("""
#         .AMMMMMMMMMMA.
#       .AV. :::.:.:.::MA.
#      A' :..        : .:`A
#     A'..              . `A.
#    A' :.    :::::::::  : :`A
#    M  .    :::.:.:.:::  . .M
#    M  :   ::.:.....::.:   .M
#    V : :.::.:........:.:  :V
#   A  A:    ..:...:...:.   A A
#  .V  MA:.....:M.::.::. .:AM.M
# A'  .VMMMMMMMMM:.:AMMMMMMMV: A
#:M .  .`VMMMMMMV.:A `VMMMMV .:M:
# V.:.  ..`VMMMV.:AM..`VMV' .: V
#  V.  .:. .....:AMMA. . .:. .V
#   VMM...: ...:.MMMM.: .: MMV
#       `VM: . ..M.:M..:::M'
#         `M::. .:.... .::M
#          M:.  :. .... ..M
#          V:  M:. M. :M .V
#          `V.:M.. M. :M.V'                                           
# ooooo                   8   .oPYo. .oPYo. 
# 8                       8   8    8 8      
#o8oo   oPYo. .oPYo. .oPYo8   8    8 `Yooo. 
# 8     8  `' 8oooo8 8    8   8    8     `8 
# 8     8     8.     8    8   8    8      8 
# 8     8     `Yooo' `YooP'   `YooP' `YooP' 
#:..::::..:::::.....::.....::::.....::.....:
#:::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::""")
        clear()
        print("""
         .AMMMMMMMMMMA.
       .AV. :::.:.:.::MA.
      A' :..        : .:`A
     A'..              . `A.
    A' :.    :::::::::  : :`A
    M  .    :::.:.:.:::  . .M
    M  :   ::.:.....::.:   .M
    V : :.::.:........:.:  :V
   A  A:    ..:...:...:.   A A
  .V  MA:.....:M.::.::. .:AM.M
                """)
        time.sleep(1)
        clear()
        print("""
         .AMMMMMMMMMMA.
       .AV. :::.:.:.::MA.
      A' :..        : .:`A
     A'..              . `A.
    A' :.    :::::::::  : :`A
    M  .    :::.:.:.:::  . .M
    M  :   ::.:.....::.:   .M
    V : :.::.:........:.:  :V
   A  A:    ..:...:...:.   A A
  .V  MA:.....:M.::.::. .:AM.M
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A
:M .  .`VMM[║]MV.:A `V[║]MV .:M:
 V.:.  ..`VMMMV.:AM..`VMV' .: V
  V.  .:. .....:AMMA. . .:. .V
   VMM...: ...:.MMMM.: .: MMV
       `VM: . ..M.:M..:::M'
         `M::. .:.... .::M
          M:.  :. .... ..M
          V:  M:. M. :M .V
          `V.:M.. M. :M.V' 
                """)
        time.sleep(1)
        print("""
:..::::..:::::.....::.....::::.....::.....:
:::::::::: Developed By SpiceSouls ::::::::
:::::::::::::::::::::::::::::::::::::::::::
                """)
        time.sleep(3)
        clear()
        print(banner, end="", flush=True)
        time.sleep(3)
        flushletters("Version 1.0.0")
        print("\u001b[0m")

        






try:
        boot()
        loop = True
        while loop == True:
                firstchoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] InfoSec
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Weapon Lab
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Proxies
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.os\u001b[38;5;50m──►\u001b[0m """))
        

                if firstchoice == "1":          
                        infosecchoice = str(input("""
\u001b[38;5;50m┌\u001b[0m[\u001b[38;5;208m01\u001b[0m] IP Geolocator
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Port Scanner
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m03\u001b[0m] Reverse DNS
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m04\u001b[0m] Site Scanner
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m05\u001b[0m] Banner Grabber
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m06\u001b[0m] Phone Number Lookup
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.os/infosec\u001b[38;5;50m──►\u001b[0m """))

                        if infosecchoice == "1":
                                ip = input("\n\u001b[38;5;50mIP GEOLOCATER\u001b[0m\n\nWhat IP Would You Like To Locate : ")
                                ipgeolocate(ip)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "2":
                                ip = input("\n\u001b[38;5;50mPORT SCANNER\u001b[0m\n\nWhat IP Would You Like To Scan : ")
                                portscanner(ip)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "3":
                                dns = input("\n\u001b[38;5;50mREVERSE DNS\u001b[0m\n\nWhat DNS Would You Like To Reverse : ")
                                reversedns(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "4":
                                dns = input("\n\u001b[38;5;50mSITE SCANNER\u001b[0m\n\nWhat Website Would You Like To Scan : ")
                                sitescanner(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "5":
                                dns = input("\n\u001b[38;5;50mBANNER GRABBER\u001b[0m\n\nWhere Would You Like To Grab A Banner From : ")
                                bannergrabber(dns)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "6":
                                number = input("\n\u001b[38;5;50mPHONE NUMBER LOOKUP\u001b[0m\n\nWhat Number Would You Like To Reverse [FORMAT: '+447410490080 / +44 Is My Dialing Code'] : ")
                                phonenumberlookup(number)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")
                        if infosecchoice == "99":
                                pass




                if firstchoice == "2":
                        weaponlabchoice = str(input("""
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m01\u001b[0m] Anonymous FTP Connection
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m02\u001b[0m] Shodan Lookup
\u001b[38;5;50m|\u001b[0m[\u001b[38;5;208m99\u001b[0m] Back
\u001b[38;5;50m|\u001b[0m[ \u001b[38;5;226mCNTRL + C TO EXIT\u001b[0m ]\u001b[38;5;50m
|
└──\u001b[38;5;208musr@spice.os/weaponslab\u001b[38;5;50m──►\u001b[0m """))                      



                        if weaponlabchoice == "1":
                                host = input("\n\u001b[38;5;50mANONYMOUS FTP CONNECTOR\u001b[0m\n\nWhat Host Would You Like to Connect To : ")
                                anonftplogin(host)
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")

                        if weaponlabchoice == "2":
                                shodanlookup()
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
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
└──\u001b[38;5;208musr@spice.os/proxies\u001b[38;5;50m──►\u001b[0m """)) 
            
                        if proxieschoice == "1":
                                scrapeproxies('http')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")

                        if proxieschoice == "2":
                                scrapeproxies('socks4')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")     


                        if proxieschoice == "3":
                                scrapeproxies('socks5')
                                clear()
                                print(banner, end="", flush=True)
                                time.sleep(3)
                                flushletters("Version 1.0.0")
                                print("\u001b[0m")



except KeyboardInterrupt:
        print("\n\n")
        consolemessage("Powering Off . . .")
        time.sleep(3)
