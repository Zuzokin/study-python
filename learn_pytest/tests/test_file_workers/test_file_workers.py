from my_funcs.file_workers import read_from_file


def create_test_data(test_data):
    with open("tests/test_db_file.txt", "a") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    test_data = ["one\n", "second\n", "three\n"]
    create_test_data(test_data)
    assert read_from_file("tests/test_db_file.txt") == test_data


def test_read_from_file2():
    test_data = ["1\n", "2\n", "3\n"]
    create_test_data(test_data)
    assert read_from_file("tests/test_db_file.txt") == test_data
