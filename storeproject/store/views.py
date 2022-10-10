from django.contrib import auth, messages
from django.contrib.auth.models  import User
from django.shortcuts import render,redirect

# Create your views here.
def demo(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        userauth=auth.authenticate(user=username,password=password)

        if userauth is not None:
           auth.login(request,userauth)
           return redirect('login')
        else:
           messages.info(request,"invalid")
           return redirect('new')

    return render(request,'login.html')
def register(request):
     if request.method== 'POST':
         username = request.POST['username']
         password = request.POST['password']
         cpassword=request.POST['password1']
         user=User.objects.create_user(username=username,password=password)
         user.save();
         return redirect('/login')

     return render(request, 'register.html')
def new(request):
         # return redirect('base')
         return render(request,'new.html')
def base(request):
    if request.method== 'POST':
        return redirect('one')
    return render(request,"base.html")
def one(request):
       # return redirect('register')
       return render(request,'one.html')