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

    cpu_result = subprocess.check_output(
        [
            "powershell",
            "-Command",
            "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"
        ]
    )

    disk = subprocess.check_output(
            'powershell -Command "$d=Get-PSDrive C; \'{0:N2}/{1:N2} Go\' -f ($d.Used/1GB),(($d.Used+$d.Free)/1GB)"',
            shell=True,
            text=True
    )

    cpu = cpu_result.decode("utf-8").splitlines()

    gpu_names = result.decode("utf-8").splitlines()

    for gpu in gpu_names:
        gpp = gpu

    for cpuu in cpu:
        cpp = cpuu

    ram = psutil.virtual_memory()

    total = ram.total / (1024 ** 3)
    used = ram.used / (1024 ** 3)

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
{Fore.BLUE}                ⢀⣤⡤⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⢠⣟⣤⣩⠟⠀⣀⡀⠉⠉⢉⣼⣿⣿⣿⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣀⠀⠂⠠⠐⠀⡁⠠⠀⣼⣿⣿⣿⡿⠁⠀ {Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}CPU{Fore.WHITE} : {Fore.BLUE}{cpp}{Fore.WHITE}
{Fore.BLUE}                ⠀⠉⠁⠀⣀⠀⡀⠀⠠⣾⣿⡿⠃⠀⠀⠀⠀⠉⠀⣼⠉⠭⣹⠏⣸⣷⣶⣶⣶⡞⣽⠣⡰⡐⠦⡘⡌⠭⣙⣿⣿⣿⣿⣿⣿⣷⣦⣁⠀⢂⠠⠐⣼⣿⣿⣿⡿⠁⠀⠀{Fore.BLUE} {Fore.WHITE}        {Fore.GREEN}GPU{Fore.WHITE} : {Fore.BLUE}{gpp}{Fore.WHITE}
{Fore.BLUE}                ⠀⠀⠀⠸⠿⠿⠃⠀⠀⠀⠀⠀⢠⡞⡍⢳⡞⠀⠈⠉⠙⠛⠋⣰⣿⣿⣿⣿⡟⣼⠣⢱⢡⡙⢦⠱⣘⢰⣿⣿⣿⡟⠀⠉⠛⢿⣿⣿⣷⣤⡀⣼⣿⣿⣿⡿⠃⠀⠀⠀{Fore.BLUE} {Fore.WHITE}        {Fore.GREEN}Ram{Fore.WHITE} : {Fore.BLUE}{used:.2f} / {total:.2f} ({ram.percent}%){Fore.WHITE}
{Fore.BLUE}                ⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⠆⠀⠈⠉⠙⠋⠀⡴⣋⠛⣳⠖⣺⣭⣭⣭⣭⡿⣶⢡⢃⠇⢦⡑⢎⡑⢢⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀{Fore.BLUE} {Fore.WHITE}       {Fore.GREEN}Disk{Fore.WHITE} : {Fore.BLUE}{disk.strip()}{Fore.WHITE}
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
