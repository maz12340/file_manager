def make_file(files: list) -> None:
    for name in files:
        my_file = open(name, "w")
        my_file.close()
        print(f'Файл {name} создан')

 

