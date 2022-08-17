from tokenize import String
import globals
import os
from pathlib import Path
from time import sleep


def validate_iso():
    while True:
        iso_list = []
        os.system("clear")
        for file in Path(Path.home() / "Downloads").iterdir():
            try:
                if file.suffix == ".iso":
                    iso_list.append(file.name)
            except KeyError:
                pass

        for iso in iso_list:
            print(iso_list.index(iso) + 1, "-", iso)
        print("\n")

        selection_num = int(
            input(
                "Please select an ISO ({}-{}): ".format(
                    iso_list.index(iso_list[0]) + 1, iso_list.index(iso_list[-1]) + 1
                )
            )
        )
        if selection_num in range(
            iso_list.index(iso_list[0]) + 1, iso_list.index(iso_list[-1]) + 2
        ):
            globals.selected_iso = iso_list[selection_num - 1]
            if iso_validator(globals.selected_iso):
                break
        else:
            print("Invalid selection.")
            sleep(3)


def iso_validator(iso) -> bool:
    text = os.popen(f"hdiutil mount ~/Downloads/{iso}").read().split()[-1]
    print(text)
    if "CCC" in text:
        return True
    else:
        print("Invalid ISO. Please select a valid Windows ISO.")
        sleep(3)
        return False
