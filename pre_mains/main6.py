"""
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
"""
# the advantage is that if you call the function, you can use the default argument or change it
# we can call it just using get_todos() or if we would like to change the argument by using ex: get_todos("todos2.txt")
def get_todos(filepath="files/todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


"""
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
"""
# Non-default argument should be listed first (i.e., todos_arg)
# then the default arguments (i.e., filepath)
def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # more accurate, in case of "edit add more sugar"
    if user_action.startswith("add"):
        todo = user_action[4:]

        # we do not need to pass the argument because this function has its default argument
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        # in case of user enter "edit add more sugar", the program will throw the ValueError and stop immediately
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        # we can give the user an opportunity to enter the command again rather than stop the program
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Hey, you entered an unknown command")

print("Bye!")