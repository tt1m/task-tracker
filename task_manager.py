import json
from datetime import datetime

class TaskManager:
    VALID_STATUSES = ['todo', 'in-progress', 'done']
    
    def __init__(self):
        try:
            with open('tasks.json', 'r') as f:      
                self.tasks = (json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
        self.next_id = max((task['id'] for task in self.tasks), default = -1) + 1
        
    def save(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)   
            
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    def add_task(self, task_description):
        formatted_description = task_description.strip()
        
        if not formatted_description:
            return False
        
        new_task = dict(id = self.next_id,
                        description = formatted_description,
                        status = 'todo',
                        createdAt = self.get_timestamp(),
                        updatedAt = self.get_timestamp())
        self.tasks.append(new_task)
        self.next_id += 1
        self.save()
        return new_task
        
    def get_tasks(self, status):
        if status == 'all':
            return self.tasks
        else:
            if status not in TaskManager.VALID_STATUSES:
                return []
            return [task for task in self.tasks if task['status'] == status]    
        
    def update_task(self, id, task_description):
        formatted_description = task_description.strip()
        
        if not formatted_description:
            return False
        
        for task in self.tasks:
            if task['id'] == id:
                task['description'] = formatted_description 
                task['updatedAt'] = self.get_timestamp()
                self.save()
                return task
        return False
                
    def mark_status(self, id, status):
        if status not in TaskManager.VALID_STATUSES:
            return False
        
        for task in self.tasks:
            if task['id'] == id:
                task['status'] = status
                task['updatedAt'] = self.get_timestamp()
                self.save()
                return task
        return False
    
    def delete_task(self, id):
        for task in self.tasks:
            if task['id'] == id:
                self.tasks.remove(task)
                self.save()
                return task
        return False