def allocate_time(tasks):
    print("\nStudy Plan:\n")

    # Sort tasks based on priority ranking
    tasks_sorted = sorted(tasks, key=lambda task: task.priority)

    for task in tasks_sorted:
        print(f"Work on {task.name} for {task.hours_needed} hours")