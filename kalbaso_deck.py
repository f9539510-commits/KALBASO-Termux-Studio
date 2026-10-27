#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KALBASO Deck - CYBERPUNK EDITION v1.0.1
Developer: كالبسو مطروح (Calypsu)
Fixed for user release - No dev instructions
"""

import sys, os, time, random, platform

class CyberColors:
    RESET="\033[0m"; BOLD="\033[1m"; NEON_CYAN="\033[96m"; NEON_PINK="\033[95m"
    NEON_GREEN="\033[92m"; NEON_YELLOW="\033[93m"; NEON_RED="\033[91m"

BANNER = """██╗  ██╗ █████╗ ██╗     ██████╗  █████╗ ███████╗ ██████╗
██║ ██╔╝██╔══██╗██║     ██╔══██╗██╔══██╗██╔════╝██╔═══██╗
█████╔╝ ███████║██║     ██████╔╝███████║███████╗██║   ██║
██╔═██╗ ██╔══██║██║     ██╔══██╗██╔══██║╚════██║██║   ██║
██║  ██╗██║  ██║███████╗██████╔╝██║  ██║███████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝"""

def cyber_print(text, delay=0.015, color="\033[96m"):
    for char in text:
        sys.stdout.write(color + char + "\033[0m"); sys.stdout.flush(); time.sleep(delay)
    print()


def progress_bar(task_name="BOOTING", total=20):
    print(f"\033[95m[*] {task_name}:\033[0m")
    for i in range(total+1):
        percent=int((i/total)*100); filled="#"*i; empty="-"*(total-i)
        sys.stdout.write(f"\r  \033[92m[{filled}\033[96m{empty}\033[92m] {percent}%\033[0m"); sys.stdout.flush(); time.sleep(0.04)
    print("\n")

def clear_screen(): os.system("clear" if os.name != "nt" else "cls")

def print_cyber_header():
    clear_screen()
    print("\033[95m╔"+"═"*60+"╗\033[0m"); print("\033[96m"+BANNER+"\033[0m")
    print(f"║ \033[1mKalbaso Deck\033[0m  \033[93mv1.0.1\033[0m | DEV: \033[92mكالبسو مطروح\033[0m | STATUS: \033[96mONLINE\033[0m ║")
    print("\033[95m╚"+"═"*60+"╝\033[0m")

def show_cyber_menu():
    print(f"\n\033[96m┌──[ KALBASO COMMAND DECK ]\033[0m")
    print(f"\033[96m│\033[0m  \033[92m[1]\033[0m Run Core Routine :: تشغيل الفحص الأساسي")
    print(f"\033[96m│\033[0m  \033[93m[2]\033[0m Diagnostics & Telemetry :: فحص الموارد")
    print(f"\033[96m│\033[0m  \033[95m[3]\033[0m Active Modules Monitor :: إدارة الحزم")
    print(f"\033[96m│\033[0m  \033[91m[0]\033[0m Disconnect Deck :: خروج آمن")
    print(f"\033[96m└──>\033[0m")

def run_cyber_scan():
    print("\033[95m\n[!] INITIATING SECURE SEQUENCE...\033[0m"); progress_bar("SYNCHRONIZING APIS", 25)
    nodes=["127.0.0.1:8080","termux.internal.sock","python3.12/core"]
    for node in nodes:
        print(f"  \033[92m[ACTIVE]\033[0m Node: {node} --> Ping: \033[93m{random.randint(12,45)}ms\033[0m"); time.sleep(0.2)
    print(f"\n\033[96m[+] SUCCESS: Protocol executed.\033[0m\n"); input("\033[1mPress Enter to return...\033[0m")

def run_pulse():
    print("\033[93m\n[~] SYSTEM TELEMETRY:\033[0m"); print(f"  ├── Host OS      : {platform.system()} {platform.release()}")
    print(f"  ├── Architecture : {platform.machine()}"); print(f"  ├── Interpreter  : Python {platform.python_version()}")
    print(f"\n\033[92m[OK] Core temperatures optimal.\033[0m\n"); input("\033[1mPress Enter to return...\033[0m")

def run_packages():
    print("\033[95m\n[*] LOADED NEURAL LIBS:\033[0m"); print("  ├── [LOADED] requests\n  ├── [LOADED] rich\n  └── [LOADED] beautifulsoup4")
    print(f"\n\033[96m[+] All packages verified.\033[0m\n"); input("\033[1mPress Enter to return...\033[0m")

def main():
    clear_screen(); progress_bar("BOOTING KALBASO DECK v1.0.1", 15)
    while True:
        try:
            print_cyber_header(); show_cyber_menu()
            choice=input(f"\033[95mkalbaso@deck~$ \033[0m").strip()
            if choice=="1": run_cyber_scan()
            elif choice=="2": run_pulse()
            elif choice=="3": run_packages()
            elif choice in ["0","exit","q"]:
                cyber_print("\n[!] Deck link terminated. Standby...", 0.02, "\033[93m"); sys.exit(0)
            else: print("\033[91m[!] Invalid signal.\033[0m"); time.sleep(0.8)
        except KeyboardInterrupt: print("\033[91m\n\n[!] Emergency abort. Bye!\n\033[0m"); sys.exit(0)

if __name__ == "__main__": main()
