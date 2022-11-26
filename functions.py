MESSAGES = {'input':'Type add, show, edit, complete or exit: ',
    'add': 'Enter a todo: ',
    'edit_choice': 'Number of todo to edit: ',
    'edit_new': 'Enter a new todo: ',
    'complete': 'Number of todo to complete: '}

FILEPATH = 'App1\\todos.txt'


def write_file(todos_list, filepath=FILEPATH):
    """Write to-do list into a file."""
    with open(filepath, 'w') as f:
        f.writelines(todos_list)

def read_file(filepath=FILEPATH):
    """Read to-do list from a file into a variable."""
    with open(filepath, 'r') as f:
        todos_list = f.readlines()
        return todos_list

def add(todos, user_params):
    todo = user_params
    todos.append(todo + '\n')
    write_file(todos, FILEPATH)

def validate_todo_no(todos, todo_no, action):
    try:
        todo_no = int(todo_no) - 1
        return todo_no
    except ValueError as e:
        print('Number expected after "{action}"')
        return None
    except IndexError as e:
        print(f"Could not {action} todo No. {todo_no+1}, max possible todo No. is {len(todos)}")
        return None

def edit(todos, user_params):
    todo_no, new_todo = user_params.split(' ', 1)
    todo_no = validate_todo_no(todos, todo_no, 'edit')
    if todo_no:
        todos[todo_no] = new_todo + '\n'
        write_file(todos, FILEPATH)

def complete(todos, user_params):
    todo_no = validate_todo_no(todos, user_params, 'complete')
    if todo_no:
        todos.pop(todo_no)
        write_file(todos, FILEPATH)

def show(todos, user_params):
    for index, todo in enumerate(todos):
        print(f'{index + 1} - {todo.capitalize().strip()}')

ACTIONS = {'add':add, 'edit':edit, 'complete':complete, 'show':show}

if __name__ == "__main__":
    print("This is functions.py")
    print(read_file())