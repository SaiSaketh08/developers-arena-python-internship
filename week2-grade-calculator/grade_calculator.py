# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Created by: Saketh


# ==============================
# FUNCTION: CALCULATE GRADE
# ==============================

def calculate_grade(average):
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You are doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from your teacher.'


# ==============================
# FUNCTION: GET VALID MARKS
# ==============================

def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f'{subject} Marks (0-100): '))

            if 0 <= marks <= 100:
                return marks
            else:
                print('Error: Marks must be between 0 and 100.')

        except ValueError:
            print('Error: Please enter a valid number.')


# ==============================
# FUNCTION: GET NUMBER OF STUDENTS
# ==============================

def get_number_of_students():
    while True:
        try:
            num_students = int(input('Enter Number of Students: '))

            if num_students > 0:
                return num_students
            else:
                print('Error: Number of students must be greater than 0.')

        except ValueError:
            print('Error: Please enter a whole number.')


# ==============================
# MAIN PROGRAM
# ==============================

print('=' * 50)
print('           STUDENT GRADE CALCULATOR')
print('=' * 50)


# Get number of students
num_students = get_number_of_students()


# Lists to store student information
student_names = []
student_marks = []
student_results = []


# ==============================
# COLLECT STUDENT DATA
# ==============================

for i in range(num_students):

    print()
    print('=' * 18)
    print(f'     STUDENT {i + 1}')
    print('=' * 18)

    # Get student name
    while True:
        student_name = input('Student Name: ').strip()

        if student_name != '':
            break
        else:
            print('Error: Student name cannot be empty.')

    # Get marks
    english = get_valid_marks('English')
    science = get_valid_marks('Science')
    math = get_valid_marks('Math')
    history = get_valid_marks('History')

    # Store student name
    student_names.append(student_name)

    # Store marks in a list
    marks = [english, science, math, history]
    student_marks.append(marks)

    # Calculate average
    average = sum(marks) / len(marks)

    # Calculate grade and comment
    grade, comment = calculate_grade(average)

    # Store result
    student_results.append({
        'average': average,
        'grade': grade,
        'comment': comment
    })


# ==============================
# DISPLAY RESULTS
# ==============================

print()
print('=' * 70)
print('                    RESULTS SUMMARY')
print('=' * 70)

print(f'{"Name":<20} | {"Avg":>6} | {"Grade":^5} | Comment')
print('-' * 70)


for i in range(num_students):

    name = student_names[i]
    average = student_results[i]['average']
    grade = student_results[i]['grade']
    comment = student_results[i]['comment']

    print(f'{name:<20} | {average:>6.2f} | {grade:^5} | {comment}')


# ==============================
# CLASS STATISTICS
# ==============================

averages = []

for result in student_results:
    averages.append(result['average'])


class_average = sum(averages) / len(averages)
highest_average = max(averages)
lowest_average = min(averages)

highest_index = averages.index(highest_average)
lowest_index = averages.index(lowest_average)


print()
print('=' * 50)
print('                CLASS STATISTICS')
print('=' * 50)

print(f'Total Students:   {num_students}')
print(f'Class Average:    {class_average:.2f}')
print(
    f'Highest Average:  {highest_average:.2f} '
    f'({student_names[highest_index]})'
)
print(
    f'Lowest Average:   {lowest_average:.2f} '
    f'({student_names[lowest_index]})'
)


# ==============================
# END
# ==============================

print()
print('=' * 50)
print('Thank you for using the Student Grade Calculator!')
print('=' * 50)