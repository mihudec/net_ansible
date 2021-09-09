import os
import pathlib
import net_templates

COLLECTION_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = pathlib.Path(net_templates.__file__).resolve().parent.joinpath("templates")
COLLECTION_TEMPLATES_DIR = COLLECTION_DIR.joinpath("templates")

def create_templates_symlink():
    print(f"Templates Directory is: {TEMPLATES_DIR}")
    print(f"Collection Directory is: {COLLECTION_DIR}")
    print(f"Collection Templates Directory is: {COLLECTION_TEMPLATES_DIR}")
    if not COLLECTION_TEMPLATES_DIR.exists():
        print("Creating Collection Templates directory...")
        COLLECTION_TEMPLATES_DIR.mkdir()
    
    for device_type_dir in [x for x in TEMPLATES_DIR.iterdir() if x.is_dir()]:
        print(device_type_dir)
        print(f"Linking {device_type_dir.name}...")
        os.symlink(src=device_type_dir, dst=COLLECTION_TEMPLATES_DIR.joinpath(device_type_dir.name), target_is_directory=True)

if __name__ == '__main__':
    create_templates_symlink()