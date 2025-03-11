import os


FILENAME_DEFAULT = "todos.txt"


def read_todos(filename=FILENAME_DEFAULT):
    if not os.path.exists(filename):
        with open(filename, "w") as _:
            local_todos = []
    else:
        with open(filename, "r") as f:
            local_todos = [x.rstrip("\n") for x in f.readlines()]
    return local_todos


def write_todos(local_todos, filename=FILENAME_DEFAULT):
    local_todos = [(x + "\n") for x in local_todos]
    with open(filename, "w") as f:
        f.writelines(local_todos)


if __name__ == "__main__":
    test_todos = ["Clean room", "Write program", "Walk a little"]
    print(test_todos)
    write_todos(test_todos)
    test_todos = []
    print(test_todos)
    test_todos = read_todos()
    print(test_todos)



