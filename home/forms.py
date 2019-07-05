from django import forms
from home.models import Teacher
class TeacherEditModelForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        widgets={
            'teacher_name:':forms.TextInput(attrs={'class':'form-control','placeholder':'Teacher Name'}),
            'subject':forms.Select(attrs={'class':'custom-select'})
        }

class TeacherSearchForm(forms.Form):
    search_query=forms.CharField(label="Search",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True','name':'teacher_name'}))

class TeacherCreateForm(forms.Form):
    t_n=forms.CharField(label='Teacher Name ',widget=forms.TextInput(attrs={'class':'form-control','required':'True','maxlength':'30'}))
    subject_list=(('CSE','Computer Science'),('ME','Mechanical Engineering'),('CE','Civil Engineering'))
    sub=forms.CharField(label="Subject Taught ",widget=forms.Select(choices=subject_list,attrs={'class':'form-control'}))
    sal=forms.CharField(label='Teacher Salary',widget=forms.NumberInput(attrs={'class':'form-control','required':'True','maxlength':'7'}))
