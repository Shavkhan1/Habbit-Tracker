from datetime import date, datetime, timedelta


class Habit:
    def __init__(self, name):
        self.name = name
        self.created_at = date.today()
        self.completed_dates = []

    def mark_completed(self):
        today = date.today()
        if today not in self.completed_dates:
            self.completed_dates.append(today)
            print(f"Habit '{self.name}' marked as completed for {today}.")
        else:
            print(f"Habit '{self.name}' was already marked as completed for {today}.")

    def count_streak(self):
        if not self.completed_dates:
            return 0

        sorted_dates = sorted(self.completed_dates, reverse=True)

        streak = 0
        current_date = date.today()

        for completed_date in sorted_dates:
            if completed_date == current_date:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break

        return streak

    def to_dict(self):
        return {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "completed_dates": [d.isoformat() for d in self.completed_dates]
        }
    
    def longest_streak(self):
        if not self.completed_dates:
            return 0

        sorted_dates = sorted(self.completed_dates)
        
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i] - sorted_dates[i - 1]).days == 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        longest_streak = max(longest_streak, current_streak)
        return longest_streak
    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"])
        habit.created_at = datetime.fromisoformat(data["created_at"]).date()
        habit.completed_dates = [
            datetime.fromisoformat(d).date()
            for d in data["completed_dates"]
        ]
        return habit
