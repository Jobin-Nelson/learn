'''A Todoist command line app'''
from typing import NoReturn
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import sys, os

load_dotenv()
TODOIST_API_TOKEN = os.getenv('TODOIST_API_TOKEN')
if not TODOIST_API_TOKEN:
    print('API Token is not found in environment variables')
    sys.exit(1)

api = TodoistAPI(TODOIST_API_TOKEN)
active_tasks = {}

def main() -> None:
    print('Your active tasks ...')
    print('a: Add, u: Update, d: delete, c: complete, q: quit => ')
    while True:
        show_task()

        choice = input('[a/u/d/c/q] => ')
        choices = {
            'a': add_task,
            'u': update_task,
            'd': delete_task,
            'c': complete_task,
            'q': quit_program,
        }

        if choice in choices:
            choices[choice]()
        else:
            print(f'Invalid input recieved {choice}')

def show_task() -> None:
    try:
        tasks = api.get_tasks(filter='!/*')
        print()
        for i, task in enumerate(tasks, 1):
            task = task.to_dict()
            active_tasks[i] = task['id']
            print(f'{i} {task["content"]} | {(task.get("due") or {}).get("date")}')
        print()
    except Exception as error:
        print('Could not get active tasks')
        print(error)

def add_task() -> None:
    print('Eg -> Task name|due string')
    task_to_create = input('=> ')
    content, _, due_string = task_to_create.partition('|')
    try:
        api.add_task(
            content=content.strip(),
            due_string=due_string.strip() or None,
        )
    except Exception as error:
        print('Could not add task')
        print(error)

def update_task() -> None:
    print('Which task do you wish to edit?')
    try:
        task_number = int(input('=> '))
        task_id = active_tasks.get(task_number)
        if not task_id:
            print('Not a valid task number')
            return
        print('Eg -> Task name|due string')
        updated_task = input('=> ')
        content, _, due_string = updated_task.partition('|')
        api.update_task(
            task_id=task_id,
            content=content.strip(),
            due_string=due_string.strip() or None,
        )
    except Exception as error:
        print(error)

def delete_task() -> None:
    print('Which task do you wish to delete?')
    try:
        task_number = int(input('=> '))
        task_id = active_tasks.get(task_number)
        if not task_id:
            print('Not a valid task number')
            return
        api.delete_task(task_id=task_id)
    except Exception as error:
        print(error)

def complete_task() -> None:
    print('Which task do you wish to complete?')
    try:
        task_number = int(input('=> '))
        task_id = active_tasks.get(task_number)
        if not task_id:
            print('Not a valid task number')
            return
        api.close_task(task_id=task_id)
    except Exception as error:
        print(error)

def quit_program() -> NoReturn:
    print('Goodbye !')
    sys.exit()

if __name__ == '__main__':
    main()
