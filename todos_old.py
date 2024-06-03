
def read_and_write_todos(fn):
    def wrapper(*args):
        todos = read_todos("todos.csv")
        result = fn(todos,*args)
        write_todos(result,'todos.csv')
        return result
    return wrapper


def read_todos(filename):
    todos_file = open(filename, "r")
    file_contents = todos_file.read()
    todos = file_contents.split("\n")
    todos_file.close()
    todos_in_parts = []
    for todo in todos:
        todo_parts = todo.split(",")
        if len(todo_parts) > 1:
            todo_dict = {
                "done" : todo_parts[2],
                "todo_text" : todo_parts[1],
                "todo_id" : todo_parts[0]
            }
            todos_in_parts.append(todo_dict)
    return todos_in_parts[1:]


def write_todos(todos,filename):
    todos_file = open(filename, 'w')
    todos_file.write("id,todo_text,done\n")
    for todo in todos:        
        done = str(todo["done"])
        todo_text = str(todo["todo_text"])
        todo_id = str(todo["todo_id"])
        todo_parts = [todo_id,todo_text,done]
        put_back_together = ",".join(todo_parts)
        ## write to that file again
        todos_file.write(put_back_together + "\n")

@read_and_write_todos
def view_incomplete_todos(todos):
    for todo in todos:
        ## check to see if it's not done, if so:
        if todo["done"] == "0":
            print(todo["todo_id"] + ": " + todo["todo_text"])
    return todos

@read_and_write_todos
def complete_todo(todos,completed_todo_id):
    for todo in todos:        
        if completed_todo_id == todo["todo_id"]:
            todo["done"] = 1
    
    return todos
            
@read_and_write_todos
def add_todo(todos,todo_text):
    ## find the last ID number in the file
    for todo in todos:
        last_id = int(todo["todo_id"])
    print(last_id)
    ## append the new todo to the file
    new_todo = {
        "todo_text":todo_text,
        "todo_id": str(last_id + 1),
        "done": "0"
    }
    todos.append(new_todo)
    return todos



# print("---- adding todo ---")
# add_todo("finish todo app stuff")
# view_incomplete_todos()
# view_incomplete_todos()
# complete_todo('5')
# view_incomplete_todos()

## stretch goal- how do we make it so the user can enter commands more than one time?

user_input = input("> what would you like to do? view, add, do?")

if user_input == "view":
    view_incomplete_todos()
