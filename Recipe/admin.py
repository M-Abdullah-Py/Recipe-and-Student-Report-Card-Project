from django.contrib import admin
from django.db.models import Sum

# Register your models here.

from .models import *
admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]

admin.site.register(SubjectMarks, SubjectMarksAdmin)


class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    ordering = ["student_rank"]
    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(mark=Sum('marks'))
        # print(subject_marks.aggregate(mark=Sum('marks')))
        # return 0 
        return marks['mark']
    list_display += ['total_marks']
admin.site.register(ReportCard, ReportCardAdmin)
