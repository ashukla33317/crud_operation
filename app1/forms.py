from django import forms

class Student_form(forms.Form):
    student_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    roll_number=forms.IntegerField()