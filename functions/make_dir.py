import os


def make_dir(name: str) -> None:
    try:
        os.mkdir(name)
        print(f'Папка {name} создана')
    except FileExistsError:
        print(f'Папка {name} уже существует')


if __name__ == "__main__":
    dir_name = input('Введите название папки: ')

    make_dir(dir_name)