from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('/register')
        else:
            messages.info(request, 'password not matching..')
            return redirect('/register')

    else:   
        return render(request, 'register.html')

def login(request):
    

    return render(request, 'login.html')