from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import registerForm, authenticationForm

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

def loginView(request):
    return render(request, 'medRelations/login.html')

def authView(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('myAccount')
    if request.POST:
        form = authenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            account = authenticate(email=email, password=password)
            if account:
                login(request,account)
                return redirect('myAccount')
    else:
        form = authenticationForm()
    context['loginForm'] = form;
    return render(request, "medRelations.login.html", context)

def accountView(request):
    return render(request, 'medRelations/account.html')
