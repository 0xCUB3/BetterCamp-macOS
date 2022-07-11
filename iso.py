import os
from pathlib import Path


def validate_iso():
    while True:
        iso_list = []
        os.system('clear')
        for file in Path(Path.home() / "Downloads").iterdir():
            try:
                if file.suffix == ".iso":
                    iso_list.append(file.name)
            except KeyError:
                pass

        for iso in iso_list:
            print(iso_list.index(iso) + 1, "-", iso)
        print("\n")

        selection_num = int(input("Please select an ISO ({}-{}): ".format(iso_list.index(iso_list[0]) + 1, iso_list.index(iso_list[-1]) + 1)))
        if selection_num in range(iso_list.index(iso_list[0]) + 1, iso_list.index(iso_list[-1]) + 1):
            globals.selected_iso = iso_list[selection_num - 1]
            break
