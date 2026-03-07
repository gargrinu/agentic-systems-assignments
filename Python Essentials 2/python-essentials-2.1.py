class StudentMarks:
    def __init__(self, marks):
        if not isinstance(marks, list):
            raise TypeError("Marks must be a list.")
        self.marks = marks

    def last_three_avg(self):
        try:
            if len(self.marks) < 3:
                raise ValueError("List has fewer than 3 marks.")
            last_three = self.marks[-3:]
            return sum(last_three)/3
        except ValueError as e:
            print("Error:", {e})
            return None
        
marks = [50, 60, 70, 80, 90]
student = StudentMarks(marks)
print("Average of last 3 marks is:",student.last_three_avg())