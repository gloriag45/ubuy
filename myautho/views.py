from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse

# Create your views here.
def show_register(request):

    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')


    form = UserCreationForm()
    context_dict ={
        'form':form
    }
    return render(request,'myautho/register.html',context_dict)
    # return HttpResponse("This is my register page")

def log_in(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Seems you haven't created an account yet"
            context_dict = {
                'error':error
            }
            return render(request, 'myautho/login.html', context_dict)





    return render(request, 'myautho/login.html')
    # return HttpResponse("Log In Page")

def log_out(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            logout(request)
            return redirect('login')
    
        return render(request,'myautho/logout.html')
    else:
        return redirect('login')
        # return HttpResponse('Oswadde nnyo')