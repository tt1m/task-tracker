import argparse
from task_manager import TaskManager
    
taskManager = TaskManager()

def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"[{t['id']}] {t['description']} ({t['status']}) - Created: {t['createdAt']} Updated: {t['updatedAt']}")

def add_command(args):
    task = taskManager.add_task(args.description)
    if task:
        print(f"Task added: [{task['id']}] {task['description']}")  
    else:
        print("Error: Task description cannot be empty.") 
    
def delete_command(args):
    task = taskManager.delete_task(args.id) 
    if task:
        print(f"Task[{task['id']}] deleted successfully.")
    else:
        print("Error: Task not found.")
    
def list_command(args):
    if args.todo:
        tasks = taskManager.get_tasks('todo')
    elif args.inprogress:
        tasks = taskManager.get_tasks('in-progress')
    elif args.done:
        tasks = taskManager.get_tasks('done')
    else:
        tasks = taskManager.get_tasks('all')
    print_tasks(tasks)    
    
def update_command(args):
    updated = False
    if args.status:
        status_map = {0: 'todo', 1: 'in-progress', 2: 'done'}
        task = taskManager.mark_status(args.id, status_map[args.status])
        if task:
            print(f"Updated status to {task['status']} for task [{task['id']}]")
            updated = True
    if args.description:
        task = taskManager.update_task(args.id, args.description)
        if task:
            print(f"Updated description for task [{task['id']}]")
            updated = True
    if not updated:
        print("Error: Nothing updated. Provide --status or --description.")
    
    if args.description:
        taskManager.update_task(args.id, args.description)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add')
parser_add.add_argument('description', type=str)
parser_add.set_defaults(func=add_command)

parser_delete = subparsers.add_parser('delete')
parser_delete.add_argument('id', type=int)
parser_delete.set_defaults(func=delete_command)

parser_list = subparsers.add_parser('list')
parser_list.add_argument('-t', '--todo', action='store_true')
parser_list.add_argument('-i', '--inprogress', action='store_true')
parser_list.add_argument('-d', '--done', action='store_true')
parser_list.set_defaults(func=list_command)

parser_update = subparsers.add_parser('update')
parser_update.add_argument('id', type=int)
parser_update.add_argument('-d', '--description', type=str)
parser_update.add_argument('-s', '--status', type=int, choices=[0, 1, 2])
parser_update.set_defaults(func=update_command)

args = parser.parse_args()
try:
    args.func(args)
except AttributeError:
    pass