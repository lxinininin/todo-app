todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # remove the trailing space
    # ex: "  add " -> "add"
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                # each word will be capitalized
                item = item.title()
                # this will print String with space, ex: "0 . Shower"
                # print(index, '-', item)
                # if we would like to remove the trailing space, we should use f-String
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            # todos.remove() accepts String as an argument to remove the specific String
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")