class Assignment:
    def __init__(self, name, assignment_type, score, weight):
        self.name = name
        self.assignment_type = assignment_type
        self.score = score
        self.weight = weight

class Student:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, name, assignment_type, score, weight):
        assignment = Assignment(name, assignment_type, score, weight)
        self.assignments.append(assignment)

    def calculate_scores(self):
        formative_total = sum(
            a.score * (a.weight / 100) for a in self.assignments if a.assignment_type == "Formative"
        )
        summative_total = sum(
            a.score * (a.weight / 100) for a in self.assignments if a.assignment_type == "Summative"
        )
        return formative_total, summative_total

    def display_transcript(self, order="asc"):
        sorted_assignments = sorted(
            self.assignments,
            key=lambda x: x.score,
            reverse=(order == "desc")
        )
        print("Transcript Breakdown:")
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-----------------------------------------------------------")
        for a in sorted_assignments:
            print(f"{a.name:<20} {a.assignment_type:<15} {a.score:<10} {a.weight}")
        print("-----------------------------------------------------------")

# Main program
if __name__ == "__main__":
    student = Student()
    # Add sample assignments for testing
    student.add_assignment("Assignment 1", "Formative", 45, 15)
    student.add_assignment("Assignment 2", "Summative", 90, 20)
    formative_score, summative_score = student.calculate_scores()
    print(f"Formative Total: {formative_score}")
    print(f"Summative Total: {summative_score}")
    student.display_transcript(order="asc")
