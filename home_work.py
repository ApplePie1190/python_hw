import os
import sys
import logging
from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])


def get_file_info(file_path):
    name = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(file_path)[1] if not os.path.isdir(file_path) else None
    is_dir = os.path.isdir(file_path)
    parent_directory = os.path.basename(os.path.dirname(file_path))
    return FileInfo(name, extension, is_dir, parent_directory)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        sys.exit(1)

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = get_file_info(file_path)
            logging.info(f"Name: {file_info.name}, Extension: {file_info.extension}, Is Directory: {file_info.is_dir}, Parent Directory: {file_info.parent_directory}")
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            dir_info = get_file_info(dir_path)
            logging.info(f"Name: {dir_info.name}, Extension: {dir_info.extension}, Is Directory: {dir_info.is_dir}, Parent Directory: {dir_info.parent_directory}")


if __name__ == "__main__":
    main()
