from django.shortcuts import render, redirect
from .models import AssignedBlock, StudentDetails, TakeAttendance, Exam
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
from django.http import JsonResponse

# Create your views here.
def home_page(request):
    if request.method == "POST":
        usn = request.POST.get("usn")
        return redirect("fetchdetails",usn=usn)
    return render(request, 'index.html')

def student_fetch(request, usn):
    context = {}
    context['studentvalid'] = False
    context['examexists'] = False
    try:
        stu = StudentDetails.objects.get(usn=usn)
        context['studentvalid'] = True
    except StudentDetails.DoesNotExist:
        context['studentvalid'] = False

    if context['studentvalid']:
        try:
            blockObj = AssignedBlock.objects.get(student = stu)
            context['examexists'] = True
            context['exam'] = str(blockObj.exam)
            context['room_no'] = str(blockObj.block)

            if not TakeAttendance.objects.filter(student=stu).exists():
                obj = TakeAttendance.objects.create(student = stu, exam = blockObj.exam)
                obj.save()
            return JsonResponse(context)
        

        except AssignedBlock.DoesNotExist:
            return JsonResponse(context)
    return JsonResponse(context)
    #return render(request, 'details.html',{"usn":usn,"msg":msg})