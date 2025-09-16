#tasks
#add delete update tasks progress
from asyncio.windows_events import NULL
import json
import argparse
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

    def listTask(self, status:str = "NULL"):
        current_table = self.table
        if(status == NULL):
            for id, desc,state, start, end in current_table:
                print(f"id: {id}, description: {desc}, state: {state}, created at: {start}, updated at: {end}\n")
        elif status != NULL:
            for id, desc, state, start, end in current_table:
                if(status == state):
                    print(f"id: {id}, description: {desc}, state: {state}, created at: {start}, updated at: {end}\n")

    
    def deleteTask(self, delIndex):
        for tasks in self.table:
            if(tasks[0] == delIndex):
                self.table.remove(tasks)
        self.storetask()

    def updateTask(self, updateIndex, description):
        
        for tasks in self.table:
            if(tasks[0] == updateIndex):
                new_task: task = [tasks[0], description, tasks[2], tasks[3], date.today()]
                self.table.remove(tasks)
        self.table.append(new_task)
        self.storetask()

    def statusUpdate(self, index:int, newstatus:str):

        for tasks in self.table:
            if(tasks[0] == index):
                new_task: task = [tasks[0], tasks[1], newstatus, tasks[3], date.today()]
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


    parser = argparse.ArgumentParser(prog="todo", description="A task list application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("filter", type=str, help = "list tasks")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Update command
    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="New description")

    # New-status command
    status_parser = subparsers.add_parser("status", help="Change task status")
    status_parser.add_argument("id", type=int, help="Task ID")
    status_parser.add_argument("state", type=str, help="New status")


    args = parser.parse_args()

    t = tasks("tasks.json")

    
        
    if args.command == "add":
        t.addtask(args.description)
    elif args.command == "update":
        t.updateTask(args.id, description=args.description)
    elif args.command == "delete":
        t.deleteTask(args.id)
    elif args.command == "list":
        if args.filter is None:
            t.listTask()
        else:
            t.listTask(args.filter)
    elif args.command == "status":
        t.statusUpdate(args.id, args.state)
    else:
        parser.print_help()
