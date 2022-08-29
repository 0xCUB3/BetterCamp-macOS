import glob
import globals
import os
from pathlib import Path
from time import sleep


def validate_iso():
    while True:
        iso = (
            os.popen(
                """osascript -e 'return (choose from list (get paragraphs of (do shell script "ls ~/Downloads/*.iso")) with prompt "Select a Windows ISO to use for your Windows installation") as string'"""
            )
            .read()
            .strip()
        )
        if iso_validator(iso):
            sleep(3)
            globals.selected_iso = iso
            break


def iso_validator(iso):
    try:
        volumeName = os.popen(f"hdiutil mount {iso}").read().split()[-1]
    except:
        print("Invalid ISO. Please select a valid Windows ISO.")
        sleep(3)
        return False
    print(volumeName)
    print(f"Checking {volumeName} for setup.exe...")
    if glob.glob(f"{volumeName}/setup.exe"):
        print("Found setup.exe!")
        return True
    else:
        print("Invalid ISO. Please select a valid Windows ISO.")
        sleep(3)
        return False
