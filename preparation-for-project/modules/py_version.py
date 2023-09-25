from sys import version_info


def py_version():
    print(f'Python {version_info[0]}.{version_info[1]}.{version_info[2]}')
