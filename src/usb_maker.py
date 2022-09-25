from src import global_vars
import os
from time import sleep


def make_usb_installer(usb, iso):
    print("Formatting USB drive...")
    format_usb(usb)
    print("Unmounting USB drive because of weird bug...")
    os.system(f"diskutil unmountDisk {usb}")
    print("Copying Windows ISO to USB drive...")
    os.system(
        f"sudo dd if={iso} of={usb} bs=8M status=progress"
    )
    print("Done!")
    sleep(3)


# Formats USB drive
def format_usb(usb) -> None:
    os.system(f"diskutil eraseDisk ExFAT BETTERCAMP GPT {usb}")
    print("USB drive formatted!")
    sleep(3)