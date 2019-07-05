from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from home.forms import TeacherSearchForm
from home.forms import TeacherEditModelForm
from home.forms import TeacherCreateForm
from home.models import Teacher
# Create your views here.
def addition_page(request,n1,n2):
    res=n1+n2
    return render(request,'addition.html',{'result':res})

		
def home_page(request):
	my_form=TeacherSearchForm()
	
	if request.method=="POST":
		search=TeacherSearchForm(request.POST)
		if search.is_valid():
			value=search.cleaned_data.get('search_query')
			res=Teacher.objects.filter(teacher_name__contains = value)
			return render(request,'home_page.html',{'result':res,'form':my_form})
	else:
		return render(request,'home_page.html',{'result':None,'form':my_form})
	

def index_page(request):
    return HttpResponse("YOU ARE ON INDEX PAGE")


def delete_query(request,id):

	query=Teacher.objects.get(teacher_id=id)
	#print(query.teacher_name)
	query.delete()
	messages.success(request,query.teacher_name+" was deleted successfully")
	return redirect('/home')

def edit_query(request,id):
	print(request.session['id'])
	query=Teacher.objects.get(teacher_id=id)
	if request.method=="POST":
		modelform=TeacherEditModelForm(request.POST,instance=query)
		if modelform.is_valid():
			modelform.save()
			return redirect('/home')
	else:
		modelform=TeacherEditModelForm(instance=query)
		return render(request,'edit.html',{'form':modelform})
	
def create_query(request):
	if request.method=="POST":
		del request.session['id']
		request.session['id']="SECRET"
		data_recieved=TeacherCreateForm(request.POST)
		if data_recieved.is_valid():
			new_teacher=Teacher.objects.create(teacher_name=data_recieved.cleaned_data.get('t_n'),teacher_salary=data_recieved.cleaned_data.get('sal'),subject=data_recieved.cleaned_data.get('sub'))	    
			new_teacher.save()
			messages.success(request,"CREATED SUCCESSFULLY")
			return redirect('/home')
	else:
		my_form=TeacherCreateForm()
		return render(request,"create_teacher.html",{'form':my_form})































        