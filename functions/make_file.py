def make_file(files: list) -> None:
    for name in files:
        my_file = open(name, "w")
        my_file.close()
        print(f'Файл {name} создан')


if __name__ == "__main__":
    file_name = input('Введите название файлов через запятую: ').split(',')

    make_file(file_name)
