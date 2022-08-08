import email
from django.shortcuts import redirect, render , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from cartApp.models import cartItem

# Create your views here.
def index(request):
    if 'user' in request.session.keys() and request.session['user']:
          return  render(request, 'index.html', context={'CartCount': request.session['CartCount']})
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
        return render(request, 'register.html')
    return render(request, 'register.html')
def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username, password = password)
        if user is not None:
         login(request = request,user = user)
         request.session['user'] = user.id
         request.session['CartCount'] = cartItem.objects.filter(uid = user.id, in_cart = True ).count()
         return redirect('home')   
        return render(request, 'login.html')
    return render(request, 'login.html')
def Logout(request):
    request.session['user'] = False
    request.session['CartCount'] = 0
    logout(request=request)
    return redirect ('home')
    