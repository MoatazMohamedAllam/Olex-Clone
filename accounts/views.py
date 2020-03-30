from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        

        #check if passwords matched
        if password == password2:

            #if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request,'this username already exists')
                return redirect('accounts:register')
            else:
                #check email
                if User.objects.filter(email=email).exists():
                    messages.error(request,'this email already exists')
                    return redirect('accounts:register')
                else:
                    #every thing is valid
                    user =User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    )
                    user.save()
                    

                    messages.success(request,'you are now registered and can login')
                    return redirect('accounts:login')
        else:
            messages.error(request,'passwords does not matched!')
            return redirect('accounts:register')

    else:
        return render(request,'accounts/register.html')

#this method to allow user login by email and i will call it in login view
def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except:
        return None

def login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        username = get_user(email)

        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            if 'remember_me' in request.POST:
                request.session.set_expiry(1209600) # 2 weeks

            messages.success(request,'you are now logged in')
            return redirect('products:index')
        else:
            messages.error(request,'invalid email or password')
            return redirect('accounts:login')

    return render(request,'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are logged out ')
        return redirect('products:index')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'your profile updated successfully')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request,'accounts/profile.html',context)




    
