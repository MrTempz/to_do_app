import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
layout = [[label]]

input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
layout.append([input_box, add_button])

todos_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
layout.append([todos_box, edit_button, complete_button])

exit_button = sg.Button('Exit')
layout.append([exit_button])

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
            window['todos'].update(values=functions.get_todos())
        case 'Edit':
            todos = functions.get_todos(filepath=functions.FILEPATH)
            todo = values['todos'][0]
            todo_no = todos.index(todo)
            new_todo = values['todo']
            functions.edit(todos, todo_no, new_todo)
            window['todos'].update(values=functions.get_todos())
        case 'Complete':
            todos = functions.get_todos(filepath=functions.FILEPATH)
            todo = values['todos'][0]
            todo_no = todos.index(todo)
            functions.complete(todos, todo_no)
            window['todos'].update(values=functions.get_todos())
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
    

window.close()