from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin
@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
    list_display_links = ("first_name", "last_name", "birth_date")
    search_fields = ("first_name", )
    ordering = ("first_name", )

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "count", "author")
    list_display_links = ("title", "description", "count", "author")
    search_fields = ("id", "title" )
    ordering = ("title", )
    autocomplete_fields = ("author", )

@admin.register(BookingBook)
class BookingBookAdmin(admin.ModelAdmin):
    list_display = ("create_data","returen_date")
    list_display_links = ("create_data","returen_date")
    search_fields = ("student", "book")
    ordering = ("student", "book")

@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("text", )
