from datetime import date
from logging import raiseExceptions

import pytest
from todo import tasks
import os
from unittest.mock import patch

@pytest.fixture
def temp_tasks():
    """Fixture that creates a temporary expense file and tracker."""
    tr = tasks("tmp.json")
    yield tr

    os.remove("tmp.json")  # cleanup after test


def test_addtask(temp_tasks):
   todos = temp_tasks
   tasktitle = "new test task"
   todos.addtask(tasktitle)
   assert todos.taskCount == 1
   assert todos.table[0][0] == 1
   assert todos.table[0][1] == tasktitle
   assert todos.table[0][3].isoformat() == date.today().isoformat()


def test_listtask(temp_tasks):
    todos = temp_tasks
    todos.addtask("this is a print test")
    assert todos.taskCount == 1


def test_deletetask(temp_tasks):
    todos = temp_tasks
    todos.addtask("this is 1st add")
    todos.addtask("this is 2nd add")
    todos.deleteTask(1)

    assert todos.table[0][0] == 2
    assert todos.table[0][1] != "this is 1st add"


def test_statustpdate(temp_tasks):

    todos = temp_tasks
    todos.addtask("this is 1st add")

    todos.statusUpdate(1, "done")
    assert todos.table[0][2] == 'done'

def test_updatetask(temp_tasks):
    todos = temp_tasks
    todos.addtask("this is 1st add")
    todos.updateTask(1, "this is now the 2nd add")
    assert todos.table[0][1] == "this is now the 2nd add"


def test_storetask(temp_tasks):
    todos = temp_tasks
    todos.addtask("this is 1st add")
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            todos.storetask("filename.json")


        




