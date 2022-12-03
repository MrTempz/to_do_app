FILEPATH = 'App1\\todos.txt'

class Todos():
    def __init__(self, filepath=FILEPATH):
        self.filepath = filepath
        self.get_todos()

    def save_todos(self):
        """Write to-do list into a file."""
        with open(self.filepath, 'w') as f:
            f.writelines(self.todos)

    def get_todos(self):
        """Read to-do list from a file into a variable."""
        with open(self.filepath, 'r') as f:
            self.todos = f.readlines()

    def add(self, new_todo):
        self.todos.append(new_todo + '\n')
        self.save_todos()

    def edit_by_no(self, todo_no, new_todo):
        self.todos[todo_no] = new_todo + '\n'
        self.save_todos()

    def edit_by_element(self, todo, new_todo):
        try:
            todo_no = self.todos.index(todo)
            self.edit_by_no(todo_no, new_todo)
        except IndexError:
            print('To-do does not exist on the list')

    def complete_by_no(self, todo_no):
        self.todos.pop(todo_no)
        self.save_todos()

    def complete_by_element(self, todo):
        try:
            todo_no = self.todos.index(todo)
            self.complete_by_no(todo_no)
        except IndexError:
            print('To-do does not exist on the list')
    
    def bulk_complete(self, todos_to_complete):
        for todo in todos_to_complete:
            self.complete_by_element(todo)
    
if __name__ == "__main__":
    print("This is todos.py")
    todo_list = Todos()
    todo_list.show()