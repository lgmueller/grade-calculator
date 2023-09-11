

from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Set grades achieved so far
my_grades.quiz_1 = 0.78 # Received 78% in the first quiz

# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')


# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

my_grades.quiz_1= 1
my_grades.quiz_2= 1
my_grades.midterm= 1
my_grades.project= 1

# calculate grade needed for A on final
forA = .91
gradeNeeded = (forA - (
                ((my_grades.quiz_1 + my_grades.quiz_2) * weights.quizzes)
                + (my_grades.project * weights.project)
                + (my_grades.midterm * weights.midterm)
                )) / weights.final

# test calculate grade for one assignment
print(
    gradeNeeded, 
    " = ", 
    GradeCalculator.calculate_min_average_for_A(my_grades, weights, .91)
)

# test calculate grade for three assignments
my_grades.set_all(1, 1, None, None, None)
gradeNeeded = (forA - (
                ((my_grades.quiz_1 + my_grades.quiz_2) * weights.quizzes)
            )) / ( weights.final + weights.midterm + weights.project)
print(
    gradeNeeded, 
    " = ", 
    GradeCalculator.calculate_min_average_for_A(my_grades, weights, .91)
)