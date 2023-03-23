from django.contrib import admin
from .models import Exam, ExamBlocks, StudentDetails, Department, AssignedBlock, TakeAttendance

# Register your models here.

admin.site.register(Exam)
admin.site.register(ExamBlocks)
admin.site.register(StudentDetails)
admin.site.register(Department)
admin.site.register(AssignedBlock)
admin.site.register(TakeAttendance)
