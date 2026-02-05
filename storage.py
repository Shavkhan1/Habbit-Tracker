import json
from habit import Habit

FILE_NAME="data.json"

def save_habits(habits):
    with open (FILE_NAME, "w") as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)        

def load_habits():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Habit.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
