from module1 import subject
from module2 import students
subjects={
    "Math": subject("Math", 90),
    "Science": subject("Science", 85),
    "English": subject("English", 88),
    "History": subject("History", 91),
    "Computer": subject("Computer", 95)}
student1 = students("Rutuja", 101,subjects )
student1.calculate_percentage()
student1.display()


#OUTPUT
Name: Rutuja
Roll no: 101
Subjects and marks: Math 90
Subjects and marks: Science 85
Subjects and marks: English 88
Subjects and marks: History 91
Subjects and marks: Computer 95
Percentage: 89.8
