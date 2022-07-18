import email
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return  render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username,
                password=password1, email=email
            )
            user.save()
            return redirect('home')
        return render(request,'register.html')
    return  render(request, 'register.html') 