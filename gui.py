import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# the aim of [label], [input_box] is to separate label and input_box in two different lines
# if we use [label, input_box], they will be in one line
window = sg.Window(title="My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

# we can use while statement to keep the window open
while True:
    # it displays the window on the screen
    # it suspends the execution and waits the user action
    event, values = window.read()
    # if we enter the 'Hi' in input_box, and press Add button
    print(event)  # it displays "Add"
    print(values)  # it displays a dictionary which is {'todo': 'Hi'}

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'  # values is a dictionary
            todos.append(new_todo)
            functions.write_todos(todos)
        # this case is used to when we click the exit 'x' button, then we will not get error
        case sg.WIN_CLOSED:
            break

window.close()