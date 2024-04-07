from django.urls import path
from .views import StudentView, LendingView
urlpatterns = [
    path('student/', StudentView.as_view(), name="student"),
    path('', LendingView.as_view(), name='LendingView'),
]