from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student, Address

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name", "age")
    list_display_links = ("first_name", "last_name", "age")
    search_fields = ("first_name", )
    ordering = ("last_name", )

admin.site.register(Address)
