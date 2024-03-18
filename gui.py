import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# the aim of [label], [input_box] is to separate label and input_box in two different lines
# if we use [label, input_box], they will be in one line
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])

# it displays the window on the screen
# it suspends the execution and waits the user action
window.read()
window.close()