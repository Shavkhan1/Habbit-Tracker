from habit import Habit
from storage import save_habits, load_habits

def main():
    habits = load_habits()

    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Habit Complete")
        print("4. Delete Habit")
        print("5. Show Streaks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter habit name: ").strip()

            if any(h.name.lower() == name.lower() for h in habits):
                print("Habit already exists.")
            else:
                habit = Habit(name)
                habits.append(habit)
                save_habits(habits)
                print(f"Habit '{name}' added.")

        elif choice == "2":
            for habit in habits:
                print(f"- {habit.name}")

        elif choice == "3":
            name = input("Enter habit name to mark complete: ")
            for habit in habits:
                if habit.name == name:
                    habit.mark_completed()
                    save_habits(habits)
        
        elif choice == "4":
            name = input("Enter habit name to delete: ").strip().lower()

            for habit in habits:
               if habit.name.lower() == name:
                  habits.remove(habit)
                  save_habits(habits)
                  print(f"Habit '{habit.name}' deleted.")
                  break
               else:
                   print("Habit not found.")

        elif choice == "5":
            for habit in habits:
                print(f"{habit.name}")
                print(f"  Current streak: {habit.count_streak()}")
                print(f"  Longest streak: {habit.longest_streak()}")
        elif choice == "6":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
