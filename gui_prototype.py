import todos
import PySimpleGUI as sg
import time
from os import path

todo_list = todos.Todos()

GUI_font = ('Helvatica', 20)
sg.theme('DarkBlack1')
layout = []

#clock at the top of GUI
clock_label = sg.Text('', key='clock')
layout.append([clock_label])

#label row
label = sg.Text('Type in a to-do')
layout.append([label])

#input row
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button(size=2, image_source=path.join(path.curdir, 'App1', 'add.png'),
    mouseover_colors='LightBlue2', tooltip='Press to add new to-do', key='Add')
layout.append([input_box, add_button])

#list section with edit and complete buttons
todos_box = sg.Listbox(values=todo_list.todos, key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button(size=2, image_source=path.join(path.curdir, 'App1', 'complete.png'),
    mouseover_colors='LightBlue2', tooltip='Press to complete selected to-do', key='Complete')
layout.append([todos_box, edit_button, complete_button])

#exit row
exit_button = sg.Button('Exit')
layout.append([exit_button])

window = sg.Window('My To-Do App', layout=layout, font=GUI_font)

#logic
while True:
    event, values = window.read(timeout=100)
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window['clock'].update(value=now)

    print(event)
    print(values)
    match event:
        case 'Add':
            new_todo = values['todo']
            todo_list.add(new_todo)
            window['todos'].update(values=todo_list.todos)
        case 'Edit':
            try:
                todo = values['todos'][0]
                new_todo = values['todo']
                todo_list.edit_by_element(todo, new_todo)
                window['todos'].update(values=todo_list.todos)
            except IndexError:
                sg.popup('Select item first.', font=GUI_font)
        case 'Complete':
            try:
                todo = values['todos'][0]
                todo_list.complete_by_element(todo)
                window['todos'].update(values=todo_list.todos)
            except IndexError:
                sg.popup('Select item first.', font=GUI_font)
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
    

window.close()