import functions
import PySimpleGUI as sg
import time

sg.theme("Black")  # we can use it to change the GUI theme

clock = sg.Text("", key="clock")

label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

# the aim of [label], [input_box] is to separate label and input_box in two different lines
# if we use [label, input_box], they will be in one line
window = sg.Window(title="My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

# we can use while statement to keep the window open
while True:
    # it displays the window on the screen
    # it suspends the execution and waits the user action
    event, values = window.read(timeout=200)  # the loop will run every 200 million seconds to update the current time
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%m:%S"))

    # if we enter the 'Hi' in input_box, and press Add button
    print(event)  # it displays "Add"
    print(values)  # it displays a dictionary which is {'todo': 'Hi'}
    # if we click one element of the todos list which in list_box, ex: clean the room
    # it displays {'todo': '', 'todos': ['clean the room\n']}
    # note that 'todo' is the key of input_box, 'todos' is the key of list_box

    print(values["todos"])  # it will display a List which is ['clean the room\n']

    # this is used to identify which button we pressed
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'  # values is a dictionary
            todos.append(new_todo)
            functions.write_todos(todos)

            window["todos"].update(values=todos)

        case "Edit":
            # we need to notice that if we don't select an item in list_box and click the "Edit" button directly
            # the program will exit and throw an error, we have to solve it by using try...except statement
            try:
                # if we not add [0], values["todos"] returns a List, but we need a String
                todo_to_edit = values["todos"][0]

                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)

                # we would like to when we edit todos, the window will refresh todos list in list_box
                window["todos"].update(values=todos)
            except IndexError:
                # it will raise a new window to show the message
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window["todos"].update(values=todos)
                # in this case, we would like to when we complete one todo, it will not show in the input_box
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":
            break

        # this is used to when we click one element in list_box, it will display in the input_box
        case "todos":
            # note that the key of the input_box is "todo"
            window["todo"].update(value=values["todos"][0])

        # this case is used to when we click the exit 'x' button, then we will not get error
        case sg.WIN_CLOSED:
            break

window.close()