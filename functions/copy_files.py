import os
import shutil


def copy_files(dir1: str, dir2: str, files: list) -> None:
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        print('Одна из указанных папок не существует')
        return

    for file in files:
        if os.path.isfile(os.path.join(dir1, file)):
            shutil.copy(os.path.join(dir1, file), dir2)
            print(f'Файл {file} успешно скопирован из {dir1} в {dir2}')
        else:
            print(f'Файл {file} не существует в папке {dir1}')


if __name__ == "__main__":
    dir1 = input('Введите путь к исходной папке: ')
    dir2 = input('Введите путь к папке, куда нужно скопировать: ')
    files = input('Введите название файлов через запятую: ').split(',')

    copy_files(dir1, dir2, files)
