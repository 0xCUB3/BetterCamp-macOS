import os


# Global Variables
macModel = os.popen('sysctl hw.model').read().split(':')[1].strip()
selected_iso = ""
