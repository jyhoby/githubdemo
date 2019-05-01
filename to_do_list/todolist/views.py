from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def home(request):
	if request.method=='POST':
		if request.POST['待办事项']=='':
			content={'清单':Todo.objects.all(),'警告':'请输入内容！'}
			return render(request,'todolist/home.html',content)
		else:
			a_row = Todo(thing=request.POST['待办事项'],done=False)
			a_row.save()
			content={'清单':Todo.objects.all()}
			return render(request,'todolist/home.html',content)
	else:
		content={'清单':Todo.objects.all()}
		return render(request,'todolist/home.html',content)


def about(request):
	return render(request,'todolist/about.html')

def edit(request):
	# content={'已修改事项':Todo.objects.all()[int(forloop_counter)-1]['待办事项']}
	# return render(request,'todolist/edit.html',content)
	return render(request,'todolist/edit.html')

def delete(request,每件事_id):
	a=Todo.objects.get(id=每件事_id)
	a.delete()
	return redirect("todolist:主页")

def cross(request,每件事_id):
	if request.POST["完成状态"]=='已完成':
		a=Todo.objects.get(id=每件事_id)
		a.done=True
		a.save()
		return redirect("todolist:主页")
	else:
		a=Todo.objects.get(id=每件事_id)
		a.done=False
		a.save()
		return redirect("todolist:主页")