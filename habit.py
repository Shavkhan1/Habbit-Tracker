
from datetime import date

class Habit:
    def __init__(self, name):
        self.name = name
        self.created_at = date.today () 
        self.completed_dates = []

    def mark_completed(self):
        today = date.today()
        if today not in self.completed_dates:
            self.completed_dates.append(today)
            print(f"Habbit '{self.name}' marked as completed for {today}.")
        else:
            print(f"Habbit '{self.name}' was already marked as completed for {today}.")
    
    def count_streak(self):
        if not self.completed_dates:
            return 0
        
        sorted_dates = sorted(self.completed_dates, reverse=True)
        
        streak = 0
        current_date = date.today()

        for completed_date in sorted_dates:
            if completed_date == current_date:
                streak += 1
                current_date = current_date.replace(day=current_date.day - 1)
            else:
                break
        
        return streak
        