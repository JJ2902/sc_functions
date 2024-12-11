class Task_tracker():
    def __init__(self):
        self.todo_list = []
        self.completed = []

    def add_task(self, task):
        if task == "":
            raise Exception("Empty string given")
        
        if type(task) != str:
            raise TypeError("input must be a string") 
        
        self.todo_list.append(task)
        return f"{task} added to todo list."
    
    def display_todo_list(self):
        if len(self.todo_list) == 0:
            raise Exception ("Todo list is empty.")
        
        todo_list_str = "Todo list:"
        for task in self.todo_list:
            todo_list_str += f"\n{task}"
        return todo_list_str
    
    def mark_complete(self, task):
        for task in self.todo_list:
            if task != None:
                self.completed.append(task)
            else:
                "Task not found!"
        return "Task marked as complete!"
    
    def display_completed_list(self):
        if len(self.completed) == 0:
            raise Exception("Completed list is empty.")
        
        completed_list_str = "Completed list:"
        for task in self.completed:
            completed_list_str += f"\n{task}"
        return completed_list_str
    
    def delete_task_fr_todo_list(self,task):
        if task in self.todo_list:
            self.todo_list.remove(task)
            return "Task deleted."
        else:
            return "Task not found!"
        

task_tracker = Task_tracker()
task_tracker.add_task("Orange")

print(task_tracker.display_todo_list())
print(task_tracker.delete_task_fr_todo_list("Orange"))
#print(task_tracker.display_todo_list())
