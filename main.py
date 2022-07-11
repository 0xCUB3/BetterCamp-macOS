import os
from time import sleep
import osascript

# 1) Welcome message
# 2) Ask for type of installation (only supports USB for now)
# 3) Ask for Windows ISO (to be added - Windows downloader tool)
# 4) Ask for USB drive to install to
# 5) Create USB Installer

# Variables
macModel = os.popen('sysctl hw.model').read().split(':')[1].strip()

def welcome_menu():
    while True:
        os.system('clear')
        print('''
##########################
# Welcome to BetterCamp! #
##########################

This script will help you create a USB installer for Windows 7/8/8.1/10/11 and will prepare you with the necessary patches for your device.

Your current model: ''' + macModel + '''
If you wish to install to a different model, please select the "Change Model" option in the menu.

1. Start Process
2. Change Model
3. Exit
        ''')
        x = input("Please select an option: ")
        if x == '1':
            break
        elif x == '2':
            break
        elif x == '3':
            exit()
        else:
            continue

def select_type():
    while True:
        os.system('clear')
        print('''
############################
# Select Installation Type #
############################

1. USB Installer
2. Install to Hard Drive
3. Exit
        ''')
        x = input("Please select an option: ")
        if x == '1':
            break
        elif x == '2':
            print("Sorry, this feature is not yet available.")
            sleep(3)
        elif x == '3':
            exit()
        else:
            continue

# Run functions
welcome_menu()
select_type()