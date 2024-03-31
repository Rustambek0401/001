from django.urls import path
from .views import student_new
urlpatterns = [
    path('student/', student_new),
]