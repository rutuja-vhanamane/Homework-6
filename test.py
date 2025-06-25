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