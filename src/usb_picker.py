from src import global_vars
import os
from time import sleep


def validate_usb():
    while True:
        os.system("clear")
        drives = (
            os.popen('diskutil list | grep /dev/ | grep external | cut -d " " -f1')
            .read()
            .strip()
            .split("\n")
        )
        for i in range(len(drives)):
            drives[
                i
            ] = f"""{drives[i]} - {os.popen(f'diskutil info {drives[i]} | grep "Media Name"').read().split(":")[-1].strip()}"""
        driveString = '{"' + '", "'.join(drives) + '"}'
        usb = os.popen(
            f"""osascript -e 'return (choose from list {driveString} with prompt "Select a USB drive that you would like to use for the Windows installer") as string'"""
        ).read()
        usb = usb.split()[0].strip()

        if usb == "false":
            exit()

        if float(
            os.popen("diskutil info " + usb + " | grep 'Disk Size' | awk '{print $3}'")
            .read()
            .strip()
        ) < float(7.5):
            print(
                "USB drive too small. Please select a USB drive that is at least 8GB in size."
            )
            sleep(3)
            continue

        global_vars.selected_usb = usb

        print("Selected USB drive!")
        sleep(3)
        break
