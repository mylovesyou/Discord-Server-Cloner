import requests
import threading
import asyncio
import base64
from pystyle import *
import random
from datetime import datetime
import os
import time

def logo():
    l = """                             
          ██╗  ██╗   ██╗██╗  ██╗███████╗ ██████╗ █████╗ 
          ██║  ╚██╗ ██╔╝╚██╗██╔╝██╔════╝██╔════╝██╔══██╗
          ██║   ╚████╔╝  ╚███╔╝ ███████╗██║     ███████║
          ██║    ╚██╔╝   ██╔██╗ ╚════██║██║     ██╔══██║
          ███████╗██║   ██╔╝ ██╗███████║╚██████╗██║  ██║
          ╚══════╝╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                           
    """
    c = Colorate.Horizontal(Colors.blue_to_purple, l)
    print(c)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def current_time():
    return datetime.now().strftime("%H:%M:%S")

b = Colors.dark_blue
r = Colors.red
g = Colors.green
y = Colors.yellow
w = Colors.white
    