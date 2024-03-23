while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            """
            # file is an Object
            file = open("files/todos.txt", 'r')
            # it returns a List, each line is an element of the List
            todos = file.readlines()
            file.close()
            """
            # we can replace the previous one with this 'with' expression, and we don't need write file.close()
            # (The close() method is called implicitly even though we don't call it explicitly.
            # The Python interpreter will call the method when it sees that we have written a with-context manager.)
            with open("../files/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            """
            # it will overwrite todos.txt
            file = open("files/todos.txt", 'w')
            file.writelines(todos)
            file.close()
            """
            # we can replace the previous one with this 'with' expression, and we don't need write file.close()
            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

        case "show":
            """
            file = open("files/todos.txt", 'r')
            todos = file.readlines()
            file.close()
            """
            with open("../files/todos.txt", 'r') as file:
                todos = file.readlines()

            """
            new_todos = []
            for item in todos:
                # remove '\n' in String
                new_item = item.strip('\n')
                new_todos.append(new_item)
            """
            # List Comprehension: we can replace the previous one with this brief expression
            # new_todos = [item.strip('\n') for item in todos]

            """
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
            """

            # or we simply use this by using only one loop
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            number -= 1

            with open("../files/todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("../files/todos.txt", 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case "exit":
            break

        case _:
            print("Hey, you entered an unknown command")

print("Bye!")