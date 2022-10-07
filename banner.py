import sys
import platform,os
from platform import system
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)

def banner():
    print(r"""

    ╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╔═╗┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐
    ╚═╗││││├─┘│  ├┤   ╠═╝│ │├┬┘ │   ╚═╗│  ├─┤││││││├┤ ├┬┘
    ╚═╝┴┴ ┴┴  ┴─┘└─┘  ╩  └─┘┴└─ ┴   ╚═╝└─┘┴ ┴┘└┘┘└┘└─┘┴└─
 
    Developed By

    ███╗   ███╗     ██╗ ██████╗ ██╗     ███╗   ██╗ ██╗██████╗ 
    ████╗ ████║     ██║██╔═████╗██║     ████╗  ██║███║██╔══██╗
    ██╔████╔██║     ██║██║██╔██║██║     ██╔██╗ ██║╚██║██████╔╝
    ██║╚██╔╝██║██   ██║████╔╝██║██║     ██║╚██╗██║ ██║██╔══██╗
    ██║ ╚═╝ ██║╚█████╔╝╚██████╔╝███████╗██║ ╚████║ ██║██║  ██║
    ╚═╝     ╚═╝ ╚════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═╝╚═╝  ╚═╝
    ----------------------------------------------------------
    Github : https://github.com/themj0ln1r
    Blog : https://themj0ln1r.github.io
    Website : https://themj0ln1r.github.io/mj0ln1rs-website/
    ----------------------------------------------------------
""")
