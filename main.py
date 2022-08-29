import os
from time import sleep

import globals
import iso
import usb
import maker

# 1) Welcome message
# 2) Ask for type of installation (only supports USB for now)
# 3) Ask for Windows ISO (to be added - Windows downloader tool)
# 4) Ask for USB drive to install to
# 5) Create USB Installer


def welcome_menu():
    while True:
        os.system("clear")
        print(
            """
##########################
# Welcome to BetterCamp! #
##########################

This script will help you create a USB installer for Windows 7/8/8.1/10/11 and will prepare you with the necessary patches for your device.

Your current model: """
            + globals.macModel
            + """
If you wish to install to a different model, please select the "Change Model" option in the menu.

1. Start Process
2. Change Model
3. Exit
        """
        )
        x = input("Please select an option: ")
        if x == "1":
            break
        elif x == "2":
            break
        elif x == "3":
            exit()
        else:
            continue


def select_type():
    while True:
        os.system("clear")
        print(
            """
############################
# Select Installation Type #
############################

1. USB Installer
2. Install to Hard Drive
3. Exit
        """
        )
        x = input("Please select an option: ")
        if x == "1":
            break
        elif x == "2":
            print("Sorry, this feature is not yet available.")
            sleep(3)
        elif x == "3":
            exit()
        else:
            continue


def select_iso():
    while True:
        os.system("clear")
        print(
            """
#######################
# Select/Download ISO #
#######################

1. Select ISO
2. Download ISO
3. Exit
        """
        )
        x = input("Please select an option: ")
        if x == "1":
            iso.validate_iso()
            break
        elif x == "2":
            print("Sorry, this feature is not yet available.")
            sleep(3)
        elif x == "3":
            exit()
        else:
            continue


def select_usb():
    while True:
        os.system("clear")
        print(
            """
####################
# Select USB Drive #
####################

1. Select USB Drive
2. Exit
        """
        )
        x = input("Please select an option: ")
        if x == "1":
            usb.validate_usb()
            break
        elif x == "2":
            exit()
        else:
            continue


def create_usb():
    os.system("clear")
    warning = os.system(
        """osascript -e 'return (display dialog "Warning! If you continue, """
        + globals.selected_usb
        + """ will be erased!" buttons {"Cancel", "Continue"} default button "Continue" with icon caution)'"""
    )
    if warning == 256:
        exit()
    maker.make_usb_installer(globals.selected_usb, globals.selected_iso)

def finish():
    os.system("clear")
    print("""
##########################
# Installation Complete! #
##########################
    """)
    print("\nReboot your Mac and hold the [Option] key to boot into the USB Installer!")
    sleep(3)
    exit()


def main():
    # Run Other Functions
    welcome_menu()
    select_type()
    select_iso()
    select_usb()
    create_usb()


if __name__ == "__main__":
    main()
