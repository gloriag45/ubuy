from django.shortcuts import render,redirect
from interns.models import *
from interns.form import TaskForm, InternForm

# from django.http import HttpResponse

# Create your views here.
def application_tracking(request):
    return render(request, 'interns/application_tracking.html')
    # return HttpResponse("Application Tracking")

def dashboard(request):
        intern_days = InternshipDay.objects.all()
        page='days'
        return render(request, 'interns/intern_dashboard.html',{
           'intern_days' :intern_days,
           'page':page
    })
    
        
def tasks(request):
    intern_days = InternshipDay.objects.all()
    page='days'
    return render(request, 'interns/tasks.html',{
        'intern_days' :intern_days,
        'page':page
    }
        
    )
def task_details(request,intern_day):
  
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
             task =form.save()
            #  day_id =task.day
            #  intern_day2 = InternshipDay.objects.get(id = day_id)
             return redirect('task_details', task.day)
        else:
             pass
   
    
    page='tasks'
    internship_day = InternshipDay.objects.get(Internship_day=intern_day)
    intern_days = InternshipDay.objects.all()
    AllTasks = internship_day.tasks.all()
    print(AllTasks)

    form = TaskForm()


    return render(request, 'interns/intern_dashboard.html',{
        'tasks':AllTasks,
        'page':page,
        'intern_day':intern_day,
        'intern_days':intern_days,
        'form':form
    } )




def intern_details(request):
        
        if request.method == 'POST':
           form = InternForm(request.POST)
           if form.is_valid():
              intern =form.save()
            
              return redirect('application_tracking')
        else:
             pass
        form = InternForm()

        return render(request, 'interns/intern_details.html',{
             'form':form
        })

def show_application(request):
     return render(request, 'interns/application.html')

def other_details(request,intern_day, task):
   page=None
   intern_day=intern_day
   task =task
   print(task)
   internship_day = InternshipDay.objects.get(Internship_day=intern_day)
   intern_days = InternshipDay.objects.all()

   AllTasks = internship_day.tasks.all()
   
   my_task = Task.objects.get(task = task)
   task_tools =my_task.tools.all()
   task_skills =my_task.skills.all()
   task_experiences = my_task.experiences.all()
   task_suggestions = my_task.suggestions.all()
   task_images = my_task.task_images.all()
   print(my_task)

   page:'other_details'
   context_dict={
      'tasks':AllTasks,
      'page':page,
      'task':task,
      'intern_days':intern_days,
      'intern_day':internship_day,
      'task_tools':task_tools,
      'task_skills':task_skills,
      'task_experiences':task_experiences,
      ' task_suggestions': task_suggestions,
      'task_images':task_images


   }
     
   return render(request, 'interns/other_details.html', context_dict)
    