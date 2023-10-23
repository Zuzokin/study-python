import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open("tests/test_db_file.txt", "w"):
        pass
