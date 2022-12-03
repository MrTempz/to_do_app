FILEPATH = 'App1\\todos.txt'

class Todos():
    def __init__(self, filepath=FILEPATH):
        self.filepath = filepath
        self.get_todos()

    def save_todos(self):
        """Write to-do list into a file."""
        with open(self.filepath, 'w') as f:
            f.writelines(self.todos_list)

    def get_todos(self):
        """Read to-do list from a file into a variable."""
        with open(self.filepath, 'r') as f:
            self.todos = f.readlines()

    def add(self, new_todo):
        self.todos.append(new_todo + '\n')
        self.save_todos()

    def edit(self, todo_no, new_todo):
        self.todos[todo_no] = new_todo + '\n'
        self.save_todos()

    def complete(self, todo_no):
        self.todos.pop(todo_no)
        self.save_todos()
    
if __name__ == "__main__":
    print("This is todos.py")
    todo_list = Todos()
    todo_list.show()