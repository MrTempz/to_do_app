import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")



while True:
    user_action = input(functions.MESSAGES['input']).lower()
    user_choice = user_action.split(' ',1)[0]
    
    
    if user_choice in functions.ACTIONS.keys():
        action = functions.ACTIONS[user_choice]
        todos = functions.get_todos(functions.FILEPATH)
        if user_choice == user_action:
            action(todos)
        else:
            user_params = user_action.split(' ', 1)[1]
            if user_params.split()[0].isdigit():
                todo_choice = user_params.split()[0]
                todo_no = functions.validate_todo_no(todos, todo_choice, user_action)
                if todo_no:
                    if todo_choice == user_params:
                        action(todos, todo_no)
                    else:
                        action(todos, todo_no, user_params.split(' ', 1)[1])

            else:
                action(todos, user_params)
    
    elif user_choice == 'exit':
        break
    else:
        print('Incorrect command, try again')

print('Bye!')

