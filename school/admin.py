from django.contrib import admin
from school.models import Class , Subject, SubjectsList
from accounts.models import School
# Register your models here.
class StudentClassAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': [
                                'class_name',
                                'connect_school',]}),)

    list_display = ('class_name','connect_school',)
admin.site.register(Class, StudentClassAdmin)

class ClassInline(admin.TabularInline):
    model = Class

class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        ClassInline,
    ]

# class StudentSubjectAdmin(admin.ModelAdmin):
#     fieldsets = ((None, {'fields': [
#                                 'subjects',
#                                 'connect_class',]}),)

#     list_display = ('class_name','connect_class',)
# admin.site.register(Subject, StudentSubjectAdmin)

admin.site.register(Subject)

admin.site.register(SubjectsList)