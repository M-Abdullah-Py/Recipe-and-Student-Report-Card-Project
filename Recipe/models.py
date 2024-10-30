from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank= True)
    recipe_name = models.CharField(max_length= 50)
    recipe_description = models.CharField(max_length= 500)
    recipe_image = models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default=1) # for filter querries 


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering =['name']



class StudentID(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students")
    student_id = models.OneToOneField(StudentID, related_name="student", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=20)
    student_email = models.EmailField(unique=True, null=True)
    student_address = models.TextField()
    student_age = models.IntegerField(default=18)


    # Access 
    # fetch department
    # department_computer = Department.objects.get(name = "computer")
    # computer_students = department_computer.students.all()
    # computer_students[0].student_name 

    # students_in_math = Student.objects.filter(department__name="Math")

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.subject_name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE , related_name= "marks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"

    class Meta:
        unique_together = ['student', "subject"]



class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard",  on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation']