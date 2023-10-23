from pathlib import Path
import pathlib
from some_files import db_helper


def read_from_file(path):
    with open(path, "r") as f_o:
        return f_o.readlines()


if __name__ == "__main__":
    filepath = db_helper.DB_PATH
    print(read_from_file(filepath))
