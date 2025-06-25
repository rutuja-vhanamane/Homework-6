from module1 import subject
class students:
    def __init__(self,name,roll_no,subjects_dict):
        self.name=name
        self.roll_no=roll_no
        self.subjects=subjects_dict
        self.percentage=0

    def calculate_percentage(self):
        total=sum(subj.marks for subj in self.subjects.values())
        total_subjects=len(self.subjects)
        self.percentage=total/(total_subjects*100)*100
        return self.percentage
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        for subject_name,subject_obj in self.subjects.items():
            print("Subjects and marks:",subject_name,subject_obj.marks)
        print("Percentage:",self.percentage)