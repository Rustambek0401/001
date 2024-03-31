from django.shortcuts import render

def student_new(request):
    return render(request, 'student_new.html')