from src import global_vars, downloader
import os
from time import sleep


def make_usb_installer(usb, iso):
    print("Formatting USB drive...")
    format_usb(usb)
    print("Checking for Homebrew...")
    check_for_homebrew()
    print("Checking for required packages...")
    print("Checking for rsync...")
    check_for_rsync()
    if check_wim_size():
        print("Checking for wimlib...")
        check_for_wimlib()
        print("Copying ISO to USB drive...")
        os.system(
            f"rsync -avh --progress --exclude=sources/install.wim {iso}/* /Volumes/BETTERCAMP/"
        )
        print("Splitting install.wim...")
        os.system(
            f"wimlib-imagex split {iso}/sources/install.wim /Volumes/BETTERCAMP/sources/install.swm 3000"
        )
    else:
        print("Copying ISO to USB drive...")
        os.system(f"rsync -avh --progress {iso}/* /Volumes/BETTERCAMP/")
    print("Downloading Apple's BootCamp drivers for " + global_vars.macModel)
    if global_vars.macModel in global_vars.pre_2011:
        downloader.download_file(global_vars.bc_pre_2011, "drivers")
    elif global_vars.macModel in global_vars._2011_2012:
        downloader.download_file(global_vars.bc_2011_2012, "drivers")
    else:
        downloader.download_file(global_vars.bc_post_2012, "drivers")
    print("Done!")
    sleep(3)


# Formats USB drive
def format_usb(usb) -> None:
    print("Formatting USB drive...")
    os.system(f"diskutil eraseDisk MS-DOS BETTERCAMP GPT {usb}")
    print("USB drive formatted!")
    sleep(3)


# Checks for Homebrew and installs it if it is not found.
def check_for_homebrew() -> None:
    if "brew" in os.popen("which brew").read():
        print("Homebrew already installed!")
    else:
        print(
            "Homebrew not found. Running install script (will require administrator password input)..."
        )
        os.system(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        )
        print("Homebrew successfully installed!")
        print("Ensuring Homebrew is installed properly...")
        # This is not comprehensive and is a terrible way to do this. Please suggest a better alternative to make sure that brew is installed...
        if "not found" in os.popen("which brew").read():
            print("Homebrew not installed correctly. Exiting...")
            exit()
        sleep(3)


# Checks for rsync and installs it if it is not found.
def check_for_rsync() -> None:
    if "rsync" in os.popen("which rsync").read():
        print("rsync already installed!")
    else:
        print("rsync not found. Installing...")
        os.system("brew install rsync")
        print("rsync successfully installed!")
        print("Ensuring rsync is installed properly...")
        # This is not comprehensive and is a terrible way to do this. Please suggest a better alternative to make sure that rsync is installed...
        if "not found" in os.popen("which rsync").read():
            print("rsync not installed correctly. Exiting...")
        sleep(3)


# Checks if wimlib splitting is needed
def check_wim_size() -> bool:
    if os.path.getsize(f"{global_vars.selected_iso}/sources/install.wim") >= 4294967295:
        return True
    return False


# Checks for wimlib and installs it if it is not found.
def check_for_wimlib() -> None:
    if "wimlib" in os.popen("which wimlib-imagex").read():
        print("wimlib already installed!")
    else:
        print("wimlib not found. Installing...")
        os.system("brew install wimlib")
        print("wimlib successfully installed!")
        print("Ensuring wimlib is installed properly...")
        # This is not comprehensive and is a terrible way to do this. Please suggest a better alternative to make sure that wimlib is installed...
        if "not found" in os.popen("which wimlib-imagex").read():
            print("wimlib not installed correctly. Exiting...")
        sleep(3)
