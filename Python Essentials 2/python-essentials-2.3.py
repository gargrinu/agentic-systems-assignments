class StudentPerformance:
    def __init__(self, scores):
        if not isinstance(scores, list):
            raise TypeError("Scores must be a list.")
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores to find highest value")
            first_score = self.scores[0]
            last_score = self.scores[-1]
            return last_score - first_score
        except ValueError as e:
            print(str(e))
            return None
        
scores = [55, 65, 75, 85]
student = StudentPerformance(scores)
print("Difference between last and first score is:",student.score_difference())