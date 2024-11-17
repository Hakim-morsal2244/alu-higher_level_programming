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
        if assignment_type not in ["Formative", "Summative"]:
            raise ValueError("Invalid assignment type. Must be 'Formative' or 'Summative'.")
        if weight <= 0 or weight > 100:
            raise ValueError("Invalid weight. Must be between 1 and 100.")
        assignment = Assignment(name, assignment_type, score, weight)
        self.assignments.append(assignment)

    def calculate_scores(self):
        formative_assignments = [a for a in self.assignments if a.assignment_type == "Formative"]
        summative_assignments = [a for a in self.assignments if a.assignment_type == "Summative"]

        formative_weight = sum(a.weight for a in formative_assignments)
        summative_weight = sum(a.weight for a in summative_assignments)

        if formative_weight > 60:
            raise ValueError("Total weight of Formative assignments exceeds 60%.")
        if summative_weight > 40:
            raise ValueError("Total weight of Summative assignments exceeds 40%.")

        formative_total = sum(a.score * (a.weight / 100) for a in formative_assignments)
        summative_total = sum(a.score * (a.weight / 100) for a in summative_assignments)

        return formative_total, summative_total

    def check_progression(self):
        formative_score, summative_score = self.calculate_scores()
        passed = formative_score >= 30 and summative_score >= 20
        if passed:
            print("Congratulations! You have passed the course.")
        else:
            print("You have failed the course and must retake it.")

    def check_resubmission(self):
        resubmissions = [
            a for a in self.assignments
            if a.assignment_type == "Formative" and a.score < 50
        ]
        if not resubmissions:
            print("No assignments eligible for resubmission.")
        else:
            print("Assignments eligible for resubmission:")
            for a in resubmissions:
                print(f"{a.name}: {a.score}%")

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

    # Adding sample assignments for demonstration
    student.add_assignment("Assignment 1", "Formative", 45, 15)
    student.add_assignment("Assignment 2", "Summative", 90, 20)
    student.add_assignment("Assignment 3", "Formative", 48, 10)
    student.add_assignment("Final Exam", "Summative", 35, 20)

    # Display transcript
    student.display_transcript(order="asc")

    # Calculate scores and check progression
    formative_score, summative_score = student.calculate_scores()
    print(f"Formative Total: {formative_score:.2f}%")
    print(f"Summative Total: {summative_score:.2f}%")
    student.check_progression()

    # Check resubmission eligibility
    student.check_resubmission()
