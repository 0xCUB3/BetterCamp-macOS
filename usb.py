import globals
import os
from pathlib import Path
from time import sleep


def validate_usb():
    while True:
        os.system("clear")
        usb = (
            os.popen(
                """osascript -e 'return (choose from list (get paragraphs of (do shell script "ls /Volumes")) with prompt "Select a USB drive that you would like to use for the Windows installer") as string'"""
            )
            .read()
            .strip()
            .replace(" ", "\ ")
        )

        if usb == "false":
            break

        if not os.path.isdir(f"/Volumes/{usb}"):

            print(f"/Volumes/{usb}")
            print(
                "Selected USB drive not mounted. Please select a valid, mounted USB drive."
            )
            sleep(3)
            continue

        globals.selected_usb = f"/Volumes/{usb}"

        print("Selected USB drive is valid!")
        sleep(3)
