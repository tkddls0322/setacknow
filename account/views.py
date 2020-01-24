from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import NowUser

# Create your views here.
def signup(request):
    context={}
    if request.method =="POST":
        if request.POST.get("pw1")==request.POST.get("pw2"):
            try:
                user = User.objects.create_user(username=request.POST.get('sid'), password=request.POST.get('pw1'))

            except IntegrityError:
                context.update({"error": "이미 가입된 학번입니다."})
                return render(request, "signup.html", context)

            now_user = NowUser(user=user)

            now_user.phonenum = request.POST.get("pn")

            now_user.save()

            return render(request,"setackapp/index.html", context)

        else:
            return render(request, 'signup.html')

    return render(request, 'account/signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST["sid"]
        password=request.POST["pw"]
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("laundry.html")
        else:
            return render(request,"loginpage.html",{'error':'username or password is incorrect'})
    else:
        return render(request, 'account/loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
