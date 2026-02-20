from planner.task import Task
from planner.allocator import allocate_time

def get_task_input():
    name = input("Enter subject name: ")

    difficulty = int(input("Enter difficulty (1-5): "))
    days_left = int(input("Enter days left: "))
    past_score = int(input("Enter your past score (0-100): "))
    priority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low): "))

    return Task(name, difficulty, days_left, past_score, priority)

def main():
    tasks = []

    num_tasks = int(input("How many tasks do you want to add? "))

    for i in range(num_tasks):
        print(f"\n--- Task {i+1} ---")
        task = get_task_input()
        tasks.append(task)

    print("\nStudy Plan:\n")
    allocate_time(tasks)

if __name__ == "__main__":
    main()