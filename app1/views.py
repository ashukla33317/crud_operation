
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        content={
            'student_info':models.Student_info.objects.all(),
            'student_form':forms.Student_form()
        }
        return render(request,"index.html",content)

    def post(self,request):
        student_name=request.POST['student_name']
        email=request.POST['email']
        roll_number=request.POST['roll_number']
        student=models.Student_info(student_name=student_name,email=email,roll_number=roll_number)
        student.save()
        return redirect('/')

class Delete_data(View):
    def post(self,request):
        student_id=request.POST['student_id']
        details=models.Student_info.objects.filter(id=student_id)
        details.delete()
        return redirect('/')
