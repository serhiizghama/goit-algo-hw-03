import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Copy files to a folder")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Source folder with files"
    )
    parser.add_argument(
        "-d", "--dist", type=Path, default=Path("dist"), help="Folder for copying"
    )
    return parser.parse_args()


def recursive_copy(source: Path, dist: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, dist)
            else:
                folder = el.suffix
                folder = dist / folder
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, folder)
                print(f"Copied file: {el} to folder: {folder}")
    except FileNotFoundError:
        # Handling error if file is not found
        print("File Not Found Error: No such file or directory")
        exit()
    except PermissionError:
        # Handling error if there are permission issues accessing the file
        print("Permission Denied Error: Access is denied")
        exit()


def main():
    args = parse_argv()
    recursive_copy(args.source, args.dist)
    # print(args)


if __name__ == "__main__":
    main()
