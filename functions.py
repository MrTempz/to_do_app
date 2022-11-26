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
    
if __name__ == "__main__":
    print("This is functions.py")
    print(read_file())