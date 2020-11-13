from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import registerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, Intervention

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

def newPatient(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    address = request.POST['address']
    email = request.POST['email']
    phone = request.POST['phone']
    cnp = request.POST['cnp']
    allergies = request.POST['allergies']
    diseases = request.POST['diseases']
    currentTreatment = request.POST['currentTreatment']
    patient = Patient(firstName=firstName, lastName=lastName, address=address, email=email, phone=phone, cnp=cnp, allergies=allergies, diseases=diseases, currentTreatment=currentTreatment)
    patient.save()
    return redirect('myAccount')

def newIntervention(request):
    interventionName = request.POST['interventionName']
    intervention = Intervention(interventionName=interventionName)
    intervention.save()
    return redirect('myAccount')

def viewPatients(request):
    patients = Patient.objects.all()
    print("Aici!!")
    return render(request, 'medRelations/account.html', {'patientsForm': patients})

def viewInterventions(request):
    interventions = Intervention.objects.all()
    print("Aici!!")
    return render(request, 'medRelations/account.html', {'interventionsForm' : interventions})
