from planner.task import Task
from planner.allocator import allocate_time
from predictor import predict_hours

def main():
    task1 = Task("Math", 5, 2, 40, 3)
    task2 = Task("Physics", 4, 3, 60, 2)
    task3 = Task("Chemistry", 3, 5, 75, 1)

    tasks = [task1, task2, task3]

    allocate_time(tasks)
    
if __name__ == "__main__":
    main()