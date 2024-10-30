import random
from faker import Faker
from .models import *
from django.db.models import Sum


fake = Faker()


def generate_unique_student_id():
    # Keep generating new IDs until one that is not in the database is found
    while True:
        student_id = str(random.randint(70,1000))  # Using a string because student_id is a CharField
        if not StudentID.objects.filter(student_id=student_id).exists():
            return student_id

def seed_db(n=10):
    for i in range(0, n):
        dep = Department.objects.all()
        if dep.exists():
            random_index = random.randint(0, len(dep)-1)
            department = dep[random_index]
        else:
            continue

        student_id = generate_unique_student_id()  # Ensures unique student_id
        name = fake.name()
        age = random.randint(18, 30)
        email = fake.email()
        address = fake.address()

        # Create unique StudentID object
        student_id_obj, created = StudentID.objects.get_or_create(student_id=student_id)

        # Create Student object linked to StudentID
        Student.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=name,
            student_age=age,
            student_email=email,
            student_address=address
        )


def student_marks(n):
    students = Student.objects.all()
    for student in students:
        subjects = Subject.objects.all()
        for subject in subjects:
            SubjectMarks.objects.create(student = student, subject = subject , marks = random.randint(30 , 100)
)
            
def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(
        mark=Sum('marks__marks')).order_by('-marks', '-student_age')

    i = 1
 
    for rank in ranks:
        ReportCard.objects.create(
            student=rank,
            student_rank=i
        )
        i = i + 1