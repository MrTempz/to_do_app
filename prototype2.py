import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")



while True:
    user_action = input(functions.MESSAGES['input']).lower()
    user_choice = user_action.split(' ',1)[0]
    if user_choice!= user_action:
        user_params = user_action.split(' ',1)[1]
    else:
        user_params = None
    
    if user_choice in functions.ACTIONS.keys():
        action = functions.ACTIONS[user_choice]
        todos = functions.read_file(functions.FILEPATH)
        action(todos, user_params)
    
    elif user_choice == 'exit':
        break

print('Bye!')

