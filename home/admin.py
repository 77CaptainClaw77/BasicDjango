from django.contrib import admin
from home.models import Student,Teacher,Library,Magazine,Article
# Register your models here.

#registering the student model
#admin.site.register(Student)
#admin.site.register(Teacher)
# admin.site.register(Library)
# admin.site.register(Magazine)
# admin.site.register(Article) 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter=('teacher_name','teacher_id')
    search_fields=('teacher_name','teacher_id')
    fields=('teacher_name','subject','teacher_salary')
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
