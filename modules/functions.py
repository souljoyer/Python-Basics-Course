FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Читає текстовий файл і повертає список завдань,
     які потрібно виконати.а
    """
    with open(filepath, "r", encoding='utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Пише список справ у текстовому файлі."""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(todos_arg)

print(type(__name__))
if __name__ == "__main__":
    print("Привіт вам з функцій!")
