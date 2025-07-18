from django.shortcuts import render
from interns.models import Interns

# Create your views here.
def show_interns(request):
    interns = Interns.objects.all()
    return render(request, 'myadmin/interns.html',{
        'interns':interns
    })
    # return HttpResponse("This is my intern page")
def intern_details(request, first_name):
    intern = Interns.objects.get(first_name = first_name)
    return render(request, 'myadmin/intern_details.html',{
        'intern' :intern
    }
        
    )
