# Задача 1
def get_content(file_name: str):
    with open(file_name, 'r') as text_file:
        return text_file.read()


# Задача 2
def get_first_line(file_name: str):
    with open(file_name, 'r') as text_file:
        return text_file.readline()


# Задача 3
def get_list_of_lines(file_name: str):
    with open(file_name, 'r') as text_file:
        return text_file.readlines()


# Задача 4
def get_list_of_lines_wo_seporator(file_name: str):
    with open(file_name, 'r') as text_file:
        return text_file.read().split('\n')


# Задача 5
def print_content(file_name: str):
    for line in get_list_of_lines_wo_seporator(file_name):
        print(line)


# Задача 6
def get_content_in_one_line(file_name: str):
    list_of_lines = get_list_of_lines_wo_seporator(file_name)
    return ' '.join(list_of_lines)


# Задача 7
def remove_seporators_from_end(line: str):
    return line.rstrip()


# Задача 8
def remove_punctuation_char_from_end(line: str):
    return line.rstrip().rstrip(' ?.!')


# Задача 9
def write_line(file_name: str, s: str):
    with open(file_name, 'w') as f:
        f.write(s)


# Задача 10
def write_new_line(file_name: str, s: str):
    with open(file_name, 'w') as f:
        f.write(s)
        f.write('\n')


# Задача 11
def write_lines(file_name: str, list_of_str):
    with open(file_name, 'w') as f:
        f.writelines(list_of_str)


# Задача 12
def copy_content_to_file(file_name_to_copy: str, file_name_to_write: str):
    with open(file_name_to_copy, 'r') as file_to_copy, open(file_name_to_write, 'w') as file_to_write:
        for line in file_to_copy:
            print(line.rstrip(), file=file_to_write)


# Задача 13
def write_to_file_all_hello_world(file_name_to_read: str, file_name_to_write: str):
    with open(file_name_to_read, 'r') as file_to_read, open(file_name_to_write, 'w') as file_to_write:
        for line in file_to_read:
            temp_line = line.rstrip()
            if temp_line.startswith('hello') and temp_line.endswith('world'):
                file_to_write.write(line)


# Задача 14
def get_dict_from_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        pets_info_dict = dict()
        for line in file:
            if line == 'Имя Питомец Возраст_питомца\n':
                continue
            name, pet, age_of_pet = line.split()
            pets_info_dict[name] = (pet, age_of_pet)
        print(pets_info_dict)
