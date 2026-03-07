class StudentScores:
    def __init__(self, scores):
        if not isinstance(scores, list):
            raise TypeError("Scores must be a list.")
        self.scores = scores

    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores to find highest value")
            last_two_scores = self.scores[-2:]
            return max(last_two_scores)
        except ValueError as e:
            print(str(e))
            return None
        
scores = [45, 67, 89, 72]
student = StudentScores(scores)
print("Highest score among last two is:",student.highest_last_two())