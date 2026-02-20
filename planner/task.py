from predictor import predict_hours

class Task:
    def __init__(self, name, difficulty, days_left, past_score, priority):
        self.name = name
        self.difficulty = difficulty        # 1–5
        self.days_left = days_left          # integer
        self.priority = priority            # numeric (1 = highest)
        self.past_score = past_score        # 0–100

        self.hours_needed = predict_hours(
            difficulty,
            days_left,
            past_score,
            priority
        )

    def __str__(self):
        return (
            f"{self.name} | Difficulty: {self.difficulty} | "
            f"Days Left: {self.days_left} | Priority: {self.priority} | "
            f"AI Hours: {self.hours_needed}"
        )