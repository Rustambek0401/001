from django.shortcuts import render
from django.views import View
from .models import Student


class StudentView(View):
    def get(self, request):
        Students = Student.objects.all()
        context = {"talabalar": Students}
        return render(request, 'student.html', context)

class LendingView(View):
    def get(self, request):
        return render(request, 'index.html')
