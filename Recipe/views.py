import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.db.models import Q, Sum
from Recipe.seed import generate_report_card

# Create your views here.

def home(request):
    return render(request, "home/home.html")

# def recipe(request):
#     return render(request, "recipe/recipe.html")
# @login_required
def recipe(request):
    recipies = Recipe.objects.all()
    if request.method == "GET":
        
        return render(request, "recipe/recipe.html" , {"recipies": recipies})
    else:
        if request.method == "POST":
            recipe_name = request.POST.get("recipe_name")
            recipe_description = request.POST.get("recipe_description")
            recipe_image = request.FILES.get("recipe_image")
            
            recipe = Recipe.objects.create(recipe_name = recipe_name, recipe_description = recipe_description, recipe_image= recipe_image)

            return render(request, "recipe/recipe.html",{"recipies": recipies} )
        
    
    
    
    
# @login_required
def update_recipe(request, id):
    recipe=Recipe.objects.get(id=id)

    if request.method == "GET":
        return render( request, "recipe/update_recipe.html", {"recipe": recipe})
    else:
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
        if recipe_image:
            recipe.recipe_image = recipe_image
        recipe.save()
        return redirect("recipe")

# @login_required
def recipe_delete(request, id):
    Recipe.objects.get(id=id).delete()
    return redirect("recipe")

# @login_required
def recipe_delete_all(request):
    Recipe.objects.all().delete()
    return render(request, "recipe/recipe.html")


def login_view(request):
    if request.method == "GET":
        return render(request, "recipe/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect("recipe")
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password")
            return render(request, "recipe/login.html")

    

def register(request):
    if request.method == "GET":
        return render(request, "recipe/register.html")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"username already exist")
            return redirect("register")


        User.objects.create_user(username=username, password=password, first_name= first_name,last_name = last_name)
       
        messages.info(request,"user created successfully ")

        return redirect("login")
    

def logout_view(request):
    logout(request)  # Log out the user
    return redirect("login")



def recipe_random_set(request):
    # vege = Recipe.objects.all()
    # vege = Recipe.objects.all().order_by('recipe_view_count')
    # vege = Recipe.objects.all().order_by('recipe_view_count')[0:2]
    vege = Recipe.objects.filter(recipe_view_count__lte = 55) 
    for veg in vege:
        veg.recipe_view_count = random.randint(20,100)
        veg.save()
    return render(request, "recipe/practice.html", {"vege":vege})
    



def get_students(request):
    queryset = Student.objects.all()

    ranks = Student.objects.annotate(mark=Sum('marks__marks')).order_by('-marks', '-student_age')
    for rank in ranks:
        print(rank.marks)

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(
            Q(student_name__icontains =  search) |
            Q(department__name__icontains =  search) |
            Q(student_email__icontains =  search) |
            Q(student_age__icontains =  search) |
            Q(student_id__student_id__icontains =  search) 
            
            )
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "student/student.html", {"page_obj": page_obj})



def marks(request, id):
    # generate_report_card()
    submark_obj = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total_marks = submark_obj.aggregate(total_marks = Sum("marks"))
    # current_rank = -1
    # ranks = Student.objects.annotate(mark=Sum('marks__marks')).order_by('-marks', '-student_age')

    # i = 1
    # for rank in ranks:
    #     if id == rank.student_id.student_id:
    #         current_rank = i
    #         break
    #     i = i + 1
        # return render(request, 'see_marks.html/', {'queryset': queryset, 'total_marks': total_marks, 'current_rank': current_rank})
    return render(request, "student/student_marks.html", {"submark_obj":submark_obj, "total_marks":total_marks})



def generate_ranks(request):
    # Calculate total marks for each student
    total_marks = (
        Student.objects.annotate(total=Sum('marks__marks'))  # Get total marks from SubjectMarks
    .order_by('-total')  # Order by total marks in descending order
    )
    for marks in total_marks:
        print(marks.marks)

    # Assign ranks
    ranked_students = []
    current_rank = 1
    previous_total = None

    for student in total_marks:
        # If the total is the same as the previous student, keep the same rank
        if previous_total is not None and student.total == previous_total:
            rank = current_rank
        else:
            rank = current_rank

        ranked_students.append({
            'student': student,
            'total_marks': student.total,
            'rank': rank
        })

        previous_total = student.total
        current_rank += 1  # Increment rank for the next student

    return render(request, "student/student_rank.html", {"ranked_students": ranked_students})

