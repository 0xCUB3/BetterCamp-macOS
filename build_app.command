#!/usr/bin/env python3

import os


class build_app:
    def __init__(self):
        self.build_app()
        self.add_terminal_launcher()

    def build_app(self):
        if "." not in os.popen("pyinstaller --version").read().strip():
            print("pyinstaller not found. Installing...")
            if "." not in os.popen("pip3 --version").read().strip():
                print("pyinstaller not installed. Exiting...")
                os.system("pip3 install pyinstaller")
            else:
                os.system("pip install pyinstaller")
        os.system("pyinstaller BetterCamp_Assistant.spec --noconfirm")

    def add_terminal_launcher(self):
        print("Adding Terminal launcher...")
        os.system(
            "cp ./resources/terminal.sh ./dist/BetterCamp\ Assistant.app/Contents/MacOS/Terminal"
        )
        print("Terminal launcher added!")
        print("Making Terminal launcher executable...")
        os.system("chmod +x ./dist/BetterCamp\ Assistant.app/Contents/MacOS/Terminal")
        print("Done!")

if __name__ == "__main__":
    build_app()
