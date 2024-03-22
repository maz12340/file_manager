import os

def rename_file(first_name: str, second_name: str) -> None:
    if os.path.isfile(first_name):
        os.rename(first_name, second_name)
        print(f'Файл {first_name} был успешно переименован в {second_name}')
    else:
        print(f'Файл {first_name} не существует')

if __name__ == "__main__":
    first_name = input('Введите текущее имя файла: ')
    second_name = input('Введите новое имя файла: ')

    rename_file(first_name, second_name)