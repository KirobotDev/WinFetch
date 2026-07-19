import os
import socket
import platform
import subprocess
import psutil
from datetime import datetime
import winreg
import GPUtil
import wmi
from colorama import Fore
import time

def fastfetch() -> str:
    name = os.environ['COMPUTERNAME'].lower()
    
    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    )

    oss, _ = winreg.QueryValueEx(key, "ProductName")
    dmrg = datetime.fromtimestamp(psutil.boot_time())
    aff = (datetime.now() - dmrg)

    name = socket.gethostname()
    ip = socket.gethostbyname(name)

    result = subprocess.check_output(
    [
        "powershell",
        "-Command",
        "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
        ]
    )

    gpu_names = result.decode("utf-8").splitlines()

    for gpu in gpu_names:
        gpp = gpu

    os.system("cls")
    print(f"""{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             {Fore.BLUE} {Fore.WHITE} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} ⠀⠀⠀
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣰⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} ⠀⠀
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⠆⠀⠀⠉⠉⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} ⠀
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⣾⣿⠟⠀⠈⠉⠉⠩⢀⣷⣶⣶⣴⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⠋⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠛⠛⠿⠿⠇⣼⣶⣶⣶⣶⢦⣀⣀⣀⣀⣄⢠⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⣶⣦⡆⠀⠀⠛⠛⠛⠀⣀⣀⣀⡀⠀⣼⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⣶⣶⣶⠀⠀⠈⠋⠉⠀⢀⠀⠀⠀⠀⠸⢿⣬⡿⠋⢀⣀⣀⣀⡀⣠⣾⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⢠⣄⣂⡄⠀⠰⠿⣿⠟⠀⡀⠀⠀⠀⠀⢠⣯⡹⣜⡽⢉⣿⣷⣷⣷⣾⣿⡟⣬⢣⢇⢯⡙⣏⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀  {Fore.BLUE} {Fore.WHITE}     {Fore.GREEN}{name}@{name}{Fore.GREEN}
{Fore.BLUE}                ⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠺⠟⠻⠃⠀⠀⠀⠀⠀⣰⣝⣫⣿⠃⢀⡉⠉⠉⠉⢁⣾⣿⣿⣿⣿⢯⡟⡜⢦⣋⠞⣦⠹⣌⣻⣿⣿⣿⠋⠉⠙⠿⣿⣿⣿⣿⣿⣶⣄⠀⠀{Fore.BLUE} {Fore.WHITE}    
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⣴⣶⣶⡶⠀⠀⠉⠉⠉⠁⢠⢯⡝⣫⣿⠓⣿⣭⣯⣯⣭⢿⡟⡼⣙⢦⡙⡞⡴⢫⣼⣿⣿⣿⠇⠀⡐⠠⠀⠈⠙⢿⣿⣿⣿⣿⣦⡀{Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}Name{Fore.WHITE} : {Fore.BLUE}{name}{Fore.WHITE}
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⠟⠀⠀⠉⠉⠉⢀⣶⣶⣶⣶⠆⠀⠙⠛⠛⠓⢃⣾⣿⣿⣿⣿⢧⢿⡸⡱⢎⠶⣙⠼⣘⣳⣾⣿⣿⠋⠀⠠⠀⡐⠀⡁⠄⢀⢹⣿⣿⣿⣿⡟{Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}Os{Fore.WHITE} : {Fore.BLUE}{oss}{Fore.WHITE}
{Fore.BLUE}                ⠀⠀⠀⠚⠊⠀⠀⠀⠀⠀⠀⢠⣤⢤⡄⠀⠚⠛⠛⠿⠏⣰⣿⣷⣶⣶⠶⣾⣻⣻⣟⣻⢯⡟⢦⡓⡝⣎⠳⣍⢞⣱⣿⣿⣿⠏⠀⠠⠁⠠⠀⠐⠀⡀⢂⣾⣿⣿⣿⡟⠀{Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}Uptime{Fore.WHITE} : {Fore.BLUE}{aff}{Fore.WHITE}
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⣀⣶⡆⠀⠀⠿⠿⠿⠁⢀⣀⡀⠀⠀⢰⣿⣿⣿⣿⡏⣹⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣾⣷⣎⣎⣿⣿⣿⡏⠀⢀⠁⠰⠀⠁⢀⠁⠀⣾⣿⣿⣿⡿⠀⠀{Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}Local_IP{Fore.WHITE} : {Fore.BLUE}{ip}{Fore.WHITE}
{Fore.BLUE}                ⢀⣤⡤⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⢠⣟⣤⣩⠟⠀⣀⡀⠉⠉⢉⣼⣿⣿⣿⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣀⠀⠂⠠⠐⠀⡁⠠⠀⣼⣿⣿⣿⡿⠁⠀ {Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}GPU{Fore.WHITE} : {Fore.BLUE}{gpp}{Fore.WHITE}
{Fore.BLUE}                ⠀⠉⠁⠀⣀⠀⡀⠀⠠⣾⣿⡿⠃⠀⠀⠀⠀⠉⠀⣼⠉⠭⣹⠏⣸⣷⣶⣶⣶⡞⣽⠣⡰⡐⠦⡘⡌⠭⣙⣿⣿⣿⣿⣿⣿⣷⣦⣁⠀⢂⠠⠐⣼⣿⣿⣿⡿⠁⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠸⠿⠿⠃⠀⠀⠀⠀⠀⢠⡞⡍⢳⡞⠀⠈⠉⠙⠛⠋⣰⣿⣿⣿⣿⡟⣼⠣⢱⢡⡙⢦⠱⣘⢰⣿⣿⣿⡟⠀⠉⠛⢿⣿⣿⣷⣤⡀⣼⣿⣿⣿⡿⠃⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⠆⠀⠈⠉⠙⠋⠀⡴⣋⠛⣳⠖⣺⣭⣭⣭⣭⡿⣶⢡⢃⠇⢦⡑⢎⡑⢢⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠉⠙⠋⠋⣰⣶⣦⣤⡤⠀⠘⠓⠶⠷⠏⣰⣿⣿⣿⣿⡟⣼⠃⢦⣉⠚⡔⡘⢆⣙⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⠿⠿⠟⢁⣶⣶⣶⣶⡶⣼⣛⣛⣛⣛⡿⣼⡃⢍⠢⢌⠓⠬⡑⢊⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀ ⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⡟⣽⣿⣿⣿⣿⣶⣿⣦⣭⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀  {Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢿⢿⣿⣿⡟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⣿⣿⣿⣿⣿⣿⣷⡄⢰⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE} 
          """)
    time.sleep(10)

if __name__ == "__main__":
    fastfetch()