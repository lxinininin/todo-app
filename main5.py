while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # check if the String of user_action contains "add"
    # ex: user_action = "add play guitar"
    if "add" in user_action:
        # it returns a String that from index 4 to the end of the String of user_action
        # ex: user_action = "add play guitar" -> todo = "play guitar"
        # user_action[4:9] returns a String that from index 4 to 8 (9 NOT included) of the String of user_action
        # same as Java String.substring()
        todo = user_action[4:]

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        number -= 1

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Hey, you entered an unknown command")

print("Bye!")