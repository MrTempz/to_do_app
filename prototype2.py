from functions import MESSAGES, FILEPATH, read_file, write_file
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")

todos = read_file(FILEPATH)

while True:
    user_action = input(MESSAGES['input']).lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos.append(todo + '\n')
        write_file(todos, FILEPATH)

    elif user_action.startswith('edit'):
        try:
            todo_no = int(user_action[5:]) - 1
            new_todo = input(MESSAGES['edit_new']) + '\n'
            todos[todo_no] = new_todo
            write_file(todos, FILEPATH)
        except ValueError as e:
            print('Number expected after "edit"')
            continue
        except IndexError as e:
            print(f"Could not edit todo No. {todo_no+1}, max possible todo No. is {len(todos)}")
            continue
        
    elif user_action.startswith('complete'):
        try:
            todo_no = int(user_action[9:]) - 1
            todos.pop(todo_no)
            write_file(todos, FILEPATH)
        except ValueError as e:
            print('Number expected after "complete"')
            continue
        except IndexError as e:
            print(f"Could not complete todo No. {todo_no+1}, max possible todo No. is {len(todos)}")
            continue

    elif user_action.startswith('show'):
        for index, todo in enumerate(todos):
            print(f'{index + 1} - {todo.capitalize().strip()}')
    
    elif user_action.startswith('exit'):
        break

print('Bye!')

