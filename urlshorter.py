from pystyle import *
import time
import pyshorteners as short
dragon_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠿⢿⣿⣿⣷⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⠀⠀⠀⠀⠹⣿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣉⣉⣉⡉⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠃
⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⣠⣾⣿⣿⠟⠁
⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⣉⣉⠉⠻⣿⠿⠃⣠⣾⣿⣿⠟⠁
⠀⠀⢀⣴⣿⣿⡿⠋⠀⠘⢿⣿⣷⣦⣤⣴⣾⣿⣿⠟⠁
⠀⣴⣿⣿⡿⠋⠀⠀⠀⠀⠈⠙⠿⠿⠿⠿⠿⠛⠁
⣼⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⣠⣶⣦⣤⠔
⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁
⠘⣿⣿⣷⣤⣀⣀⣤⣾⣿⣿⠟⠁
⠀⠈⠻⢿⣿⣿⣿⣿⡿⠟⠁
⠀⠀⠀⠀⠀⠈⠁
"""

print(dragon_art)
Write.Print('[-] this programm for short urls [-] \n',Colors.blue_to_purple)

url = Write.Input(' [+] url link : ',Colors.blue_to_red)

sh = short.Shortener()


Write.Print(sh.tinyurl.short(url),Colors.dark_blue)

time.sleep(2)

input('\npress any key to exit ...')

