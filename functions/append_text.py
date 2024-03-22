import os


def append_text(name: str, text: str) -> None:
    if os.path.isfile(name):
        with open(name, 'a') as file:
            if file.tell() > 0:
                file.write('\n')
            file.write(text)
            print(f'Текст добавлен в файл {name}')

    else:
        print(f'Файл {name} не существует')


if __name__ == "__main__":
    file_name = input('Введите название файла: ')
    text = input('Введите текст для добавления: ')

    append_text(file_name, text)
