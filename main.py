from habit import Habit

habit = Habit("Workout")
habit.mark_completed()

print("Streak:", habit.count_streak())
