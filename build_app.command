#!/usr/bin/env python3

import os


class build_app:
    def __init__(self):
        self.build_app()
        self.add_terminal_launcher()
        self.lower_minimum_os_version()

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

    def lower_minimum_os_version(self):
        print("Lowering minimum OS version...")
        path = "./dist/BetterCamp Assistant.app/Contents/MacOS/BetterCamp Assistant"
        high_sierra = b"\x00\x0D\x0A\x00"
        yosemite = b"\x00\x0A\x0A\x00"
        with open(path, "rb") as binary:
            data = binary.read()
            data = data.replace(high_sierra, yosemite, 1)
            with open(path, "wb") as binary:
                binary.write(data)
        print("Done!")


if __name__ == "__main__":
    build_app()
