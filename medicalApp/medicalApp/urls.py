from django.contrib import admin
from django.urls import include, path

from medRelations.views import (
    registrationView,
    loginPageView,
    accountView,
    authView,
    newPatient,
    newIntervention,
    getPatients,
    getInterventions,
)
urlpatterns = [
    path('', registrationView, name='registration'),
    path('admin/', admin.site.urls),
    path('loginPage', loginPageView, name='loginPageView'),
    path('home', accountView, name='myAccount'),
    path('login', authView, name='userLogin'),
    path('newPatient', newPatient, name='newPatient'),
    path('newIntervention', newIntervention, name='newIntervention'),
    path('ajax/getPatients', getPatients, name='getPatients'),
    path('ajax/getInterventions', getInterventions, name='getInterventions'),
]
