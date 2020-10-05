from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import registerForm
from django.contrib.auth.decorators import login_required

def registrationView(request):
    context = {}
    if request.POST:
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('myAccount')
        else:
            context['registration_form'] = form
    else:
        form = registerForm()
        context['registration_form'] = form
    return render(request,'medRelations/Test.html', context)

def loginPageView(request):
    return render(request, 'medRelations/login.html')

def authView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('myAccount')
        else:
            return render(request, 'loginPageView', {'error_message': 'Invalid login!'})
    else:
        return render(request, 'loginPageView')

@login_required
def accountView(request):
    return render(request, 'medRelations/account.html')
