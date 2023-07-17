import os
import sys
from time import sleep

from src import global_vars, iso_picker, usb_picker, usb_maker

# 1) Welcome message
# 2) Ask for type of installation (only supports USB for now)
# 3) Ask for Windows ISO (to be added - Windows downloader tool)
# 4) Ask for USB drive to install to
# 5) Create USB Installer


class BetterCamp_Assistant:
    def __init__(self):
        self.main()

    def welcome_menu(self):
        while True:
            os.system("clear")
            print(
                """
##########################
# Welcome to BetterCamp! #
##########################

This script will help you create a USB installer for Windows 7/8/8.1/10/11 and will prepare you with the necessary patches for your device.

Your current model: """
                + global_vars.macModel
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
                # TODO: Add model changer
                break
            elif x == "3":
                sys.exit()
            else:
                continue

    def select_type(self):
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
                sys.exit()
            else:
                continue

    def select_iso(self):
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
                iso_picker.validate_iso()
                break
            elif x == "2":
                print("Sorry, this feature is not yet available.")
                sleep(3)
            elif x == "3":
                sys.exit()
            else:
                continue

    def select_usb(self):
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
                usb_picker.validate_usb()
                break
            elif x == "2":
                sys.exit()
            else:
                continue

    def create_usb(self):
        os.system("clear")
        warning = os.system(
            """osascript -e 'return (display dialog "Warning! If you continue, """
            + global_vars.selected_usb
            + """ will be erased!" buttons {"Cancel", "Continue"} default button "Continue" with icon caution)'"""
        )
        if warning == 256:
            sys.exit()
        usb_maker.make_usb_installer(global_vars.selected_usb, global_vars.selected_iso)

    def finish(self):
        os.system("clear")
        print(
            """
##########################
# Installation Complete! #
##########################
        """
        )
        print(
            "\nReboot your Mac and hold the [Option] key to boot into the USB Installer!"
        )
        sleep(3)
        sys.exit()

    def main(self):
        # Run Other Functions
        self.welcome_menu()
        self.select_type()
        self.select_iso()
        self.select_usb()
        self.create_usb()
        self.finish()
