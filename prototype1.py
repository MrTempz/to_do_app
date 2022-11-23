messages = {'input':'Type add, show, edit, complete or exit: ',
    'add': 'Enter a todo: ',
    'edit_choice': 'Number of todo to edit: ',
    'edit_new': 'Enter a new todo: ',
    'complete': 'Number of todo to complete: '}

todo_file = 'todos.txt'
todos = []

def write_file(todos, todo_file = todo_file):
    with open(todo_file, 'w') as f:
        f.writelines(todos)

def read_file(todo_file = todo_file):
    with open(todo_file, 'r') as f:
        todos = f.readlines()
        return todos

todos = read_file()
print(todos)
while True:
    user_action = input(messages['input'])

    match user_action.lower():
        case 'add':
            todo = input(messages['add']) + '\n'
            todos.append(todo)
            write_file(todos)
        case 'show':
            for index, todo in enumerate(todos):
                print(f'{index + 1} - {todo.capitalize().strip()}')
        
        case 'edit':
            todo_no = int(input(messages['edit_choice'])) - 1
            new_todo = input(messages['edit_new']) + '\n'
            todos[todo_no] = new_todo
            write_file(todos)

        case 'complete':
            todo_no = int(input(messages['edit_choice'])) - 1
            todos.pop(todo_no)
            write_file(todos)
        case 'exit':
            break

print('Bye!')

