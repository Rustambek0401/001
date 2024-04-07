from django.shortcuts import render
from django.views import View

from library.models import Book


class BookListView(View):
    def get(self,request):
        books = Book.objects.all()
        context = {'books':books}
        return render(request,'library.html', context)

class BookDetailView(View):
    def get(self,request, id):
        book = Book.objects.get(id=id)
        return render(request,'book-detil.html',{'book':book})