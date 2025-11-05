import json
import datetime

FILE_NAME = "output.json"
def load_all_task():
    try:
        with open(FILE_NAME,"r",encoding = "utf-8") as f:
            all_task = json.load(f)
            return all_task
    except FileNotFoundError:
        return []
def writeinfile(task_list):
    with open (FILE_NAME,"w",encoding="utf-8") as f:
        json.dump(task_list, f , indent= 4, ensure_ascii= False)
        
def create_new_task_content(task_content):
    now = datetime.datetime.now()
    current_time_str = now.strftime("%d/%m/%Y  %H:%M:%S")
    new_task_disk = {
        "task": task_content ,
        "time added" : current_time_str
    }
    return new_task_disk