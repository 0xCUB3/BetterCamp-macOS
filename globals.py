import os
from subprocess import run

# Global Scripts
def exec_applescript(script) -> None:
    p = run(['osascript', '-e', script])


# Global Variables
macModel = os.popen("sysctl hw.model").read().split(":")[1].strip()
selected_iso = ""
selected_usb = ""
