import os

def validate_iso(iso_path):
    if os.path.isfile(iso_path):
        return True
    else:
        return False