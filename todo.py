#tasks
#add delete update tasks progress
from turtle import update
from typing import List, Tuple
from datetime import date

taskCount = 0
task = Tuple[int, str, str, date, date]
table: List[task]

class tasks:

    def __init__(self):
        self.taskCount = 0
        self.progress = True
        self.table: List[task] = []
        

    def addtask(self, description:str ):
        self.taskCount += 1
        createdAt = date.today()
        new_task: task = [self.taskCount, description, "todo", createdAt, createdAt]
        self.table.append(new_task)

    def listTask(self):
        current_table = self.table
        for id, desc,state, start, end in current_table:
            print(f"id: {id}, description: {desc}, state: {state}, created at: {start}, updated at: {end}\n")
    
    def deleteTask(self, delIndex):
        for tasks in self.table:
            if(tasks[0] == delIndex):
                self.table.remove(tasks)

    def updateTask(self, updateIndex, status):
        
        for tasks in self.table:
            if(tasks[0] == updateIndex):
                new_task: task = [tasks[0], tasks[1], status, tasks[3], date.today()]
                self.table.remove(tasks)
        self.table.append(new_task)
        

            


if  __name__ == "__main__":
    
    t = tasks()
    t.addtask("first task")
    
    t.addtask("2nd task")
    t.listTask()

    t.deleteTask(1)
    t.updateTask(2, "on-going")
    t.listTask()