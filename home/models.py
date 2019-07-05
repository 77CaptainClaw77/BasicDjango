from django.db import models
from django.utils import timezone #the default value can be set from this as well
# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(verbose_name="ID",primary_key=True)
    teacher_name=models.CharField(verbose_name="Teacher Name",max_length=30)
    teacher_salary=models.FloatField(verbose_name="Salary",max_length=5)
    subject_list=(('CSE','Computer Science'),('ME','Mechanical Engineering'),('CE','Civil Engineering'))
    subject=models.CharField(verbose_name="Subject Taught",max_length=50,choices=subject_list,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="TeacherInfo"
    
    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_name=models.CharField(verbose_name='Name',null=False,unique=True,max_length=100)
    deps=(('CSE','Computer Science'),('ME','Mechanical Engineering'),('CE','Civil Engineering'))
    departments=models.CharField(verbose_name='Department',choices=deps,blank=True,null=True,max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)
    class_teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    student_image=models.ImageField(upload_to='student',default=None,null=True)

    class Meta:
        db_table="StudentInfo"

    def __str__(self):
        return self.student_name

class Library(models.Model):
    book_id=models.AutoField(verbose_name="ID",primary_key=True)
    book_name=models.CharField(verbose_name="Book Name",max_length=40)
    borrowed_by=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,unique=False,verbose_name="Borrowed By")
    due_date=models.DateField(verbose_name="Due Date",null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="BookInfo"

    def __str__(self):
        return self.book_name

class Magazine(models.Model):
    mag_name=models.CharField(verbose_name="Magazine Name",max_length=50)

class Article(models.Model):
    article_name=models.CharField(verbose_name="Article Name",max_length=50)
    article_magazines=models.ManyToManyField(Magazine)
