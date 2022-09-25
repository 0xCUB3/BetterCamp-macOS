import glob
from src import global_vars
import os
from time import sleep


def validate_iso():
    while True:
        iso = (
            os.popen(
                """osascript -e 'return (choose file of type {"iso"} with prompt "Select a Windows ISO that you wish to use for the installation") as string'"""
            )
            .read()
            .strip()
            .split(":", 1)[-1]
            .replace(":", "/")
        )
        iso = f"/{iso}"
        if iso == "/":
            exit()
        print(iso)
        if iso_validator(iso):
            sleep(3)
            break


def iso_validator(iso):
    try:
        output = os.popen(f"hdiutil mount {iso}").read().split()
        for i in output:
            if "/Volumes/" in i:
                volumeName = i
                os.popen(f"hdiutil unmount {volumeName}")
                break
    except:
        print("Invalid ISO. Please select a valid Windows ISO.")
        sleep(3)
        return False
    print(iso)
    print(f"Checking {iso} for setup.exe...")
    if glob.glob(f"{volumeName}/setup.exe"):
        print("Found setup.exe!")
        global_vars.selected_iso = iso
        return True
    else:
        print("Invalid ISO. Please select a valid Windows ISO.")
        sleep(3)
        return False
