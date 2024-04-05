from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "pric", "count", "author")
    list_display_links = ("title", "description", "pric", "count", "author")
    search_fields = ("id", "title")
    ordering = ("title", )
@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("frist_name", "last_name", "birth_date")
    list_display_links = ("frist_name", "last_name", "birth_date")
    search_fields = ("id")
    ordering = ("firt_name", )

@admin.register(BookingBook)
class BookingBookAdmin(admin.ModelAdmin):
    list_display = ("student", "book","create_data","returen_date")
    list_display_links = ("student", "book","create_data","returen_date")
    search_fields = ("student", "book")
    ordering = ("student", "book")

@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("text", "book")
