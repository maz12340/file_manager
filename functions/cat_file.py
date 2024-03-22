import os


def cat_file(name: str) -> None:
    if os.path.isfile(name):
        with open(name, 'r') as file:
            print(f'Содержимое файла {name}:')
            print(file.read())

    else:
        print(f'Файл {name} не существует')


if __name__ == "__main__":
    file_name = input('Введите название файла: ')

    cat_file(file_name)
