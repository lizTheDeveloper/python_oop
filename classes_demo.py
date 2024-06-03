
class ToDo():
    """
    A class that holds todos and can display them
    """
    def __init__(self,todo_text,todo_id,done):
        self.todo_text = todo_text
        self.todo_id = todo_id 
        self.done = done

    
    def __str__(self):
        if self.done == 1:
            done_status = "Done!"
        else:
            done_status = "Not Complete"
        return self.todo_text + " " + done_status



class ToDoList():
    """
    A class for reading a specific todos CSV file, that will create todos from the file, and hold them in a list
    """
    def __init__(self,filename):
        self.todos = []
        self.filename = filename

    def read_todos():
        todos_file = open(self.filename, "r")
        file_contents = todos_file.read()
        todos = file_contents.split("\n")
        todos_file.close()
        
        for todo in todos:
            todo_parts = todo.split(",")
            if len(todo_parts) > 1:
                new_todo = ToDo(todo_parts[1],todo_parts[0],todo_parts[2])
                self.todos.append(new_todo)
        return self.todos


    def write_todos():
        todos_file = open(self.filename, 'w')
        todos_file.write("id,todo_text,done\n")
        for todo in self.todos:        
            done = str(todo["done"])
            todo_text = str(todo["todo_text"])
            todo_id = str(todo["todo_id"])
            todo_parts = [todo_id,todo_text,done]
            put_back_together = ",".join(todo_parts)
            ## write to that file again
            todos_file.write(put_back_together + "\n")
    
    def __str__(self):
        output = self.filename + "\n"
        for todo in self.todos:
            output = output + str(todo) + "\n"
        
        return output
    



new_todo = ToDo("buy coffee creamer", 1, 0)
another_new_todo = ToDo("teach oop", 2, 0)

print(new_todo)
print(another_new_todo)

todo_list = ToDoList("todos.csv")

print(todo_list)
