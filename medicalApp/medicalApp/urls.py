from django.contrib import admin
from django.urls import include, path

from medRelations.views import (
    registrationView,
    loginPageView,
    accountView,
    authView,
    newPatient,
    newDoctor,
    newIntervention,
    getPatients,
    getDoctors,
    getInterventions,
)
urlpatterns = [
    path('', registrationView, name='registration'),
    path('admin/', admin.site.urls),
    path('loginPage', loginPageView, name='loginPageView'),
    path('home', accountView, name='myAccount'),
    path('login', authView, name='userLogin'),
    path('newPatient', newPatient, name='newPatient'),
    path('newDoctor', newDoctor, name='newDoctor'),
    path('newIntervention', newIntervention, name='newIntervention'),
    path('ajax/getPatients', getPatients, name='getPatients'),
    path('ajax/getDoctors', getDoctors, name='getDoctors'),
    path('ajax/getInterventions', getInterventions, name='getInterventions'),
]
