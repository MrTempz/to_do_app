import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
layout = [[label]]

input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
layout.append([input_box, add_button])

window = sg.Window('My To-Do App', layout=layout, font=('Helvatica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos(filepath=functions.FILEPATH)
            new_todo = values['todo']
            functions.add(todos, new_todo)
        case sg.WIN_CLOSED:
            break

window.close()