#tasks
#add delete update tasks progress
import json
from turtle import update
from typing import List, Tuple
from datetime import date

task = Tuple[int, str, str, date, date]
table: List[task]

class tasks:

    def __init__(self, fileName):
        self.taskCount = 0
        self.progress = True
        self.table: List[task] = []
        self.filename = fileName
        self.loadtask()
        

    def addtask(self, description:str ):
        self.taskCount += 1
        createdAt = date.today()
        new_task: task = [self.taskCount, description, "todo", createdAt, createdAt]
        self.table.append(new_task)
        self.storetask()

    def listTask(self):
        current_table = self.table
        for id, desc,state, start, end in current_table:
            print(f"id: {id}, description: {desc}, state: {state}, created at: {start}, updated at: {end}\n")
    
    def deleteTask(self, delIndex):
        for tasks in self.table:
            if(tasks[0] == delIndex):
                self.table.remove(tasks)
        self.storetask()

    def updateTask(self, updateIndex, status):
        
        for tasks in self.table:
            if(tasks[0] == updateIndex):
                new_task: task = [tasks[0], tasks[1], status, tasks[3], date.today()]
                self.table.remove(tasks)
        self.table.append(new_task)
        self.storetask()
        
    def loadtask(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.table = [
                    (
                        item["id"],
                        item["desc"],
                        item["state"],
                        date.fromisoformat(item["created at"]),
                        date.fromisoformat(item["updated at"])
                        
                    )
                    for item in data
                ]
                if self.table:
                    self.taskCount = max(task[0] for task in self.table)
        except FileNotFoundError:
            self.table = []
            self.taskCount = 0

    def storetask(self):
        data = [
            {
                "id":item[0],
                "desc":item[1],
                "state":item[2],
                "created at":item[3].isoformat(),
                "updated at":item[4].isoformat()
            }
            for item in self.table
        ]
        with open(self.filename, "w") as f:
            json.dump(data, f)
            


if  __name__ == "__main__":
    
    t = tasks("tasks.json")
    t.addtask(input())
    t.listTask()