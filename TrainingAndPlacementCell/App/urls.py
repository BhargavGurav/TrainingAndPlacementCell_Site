from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('iiicell/', views.iiicell, name='iiicell'),
    path('PlacementProcedure/', views.placementprocedure, name='placementprocedure'),
    path('contact/', views.contact, name='contact'),
    path('TandPactivity/', views.tandpactivity, name='tandpactivity'),
    path('loginuser/', views.loginuser, name="loginuser"),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('PlacementReport/', views.placementreport, name='placementreport'),
    path('mou/', views.mou, name='mou'),
    path('broucher/', views.broucher, name='broucher'),
    path('register/', views.register, name='register'),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('profile/', views.profile, name='profile'),
    path('students/', views.students, name='students'),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('team/', views.team, name='team'),
]
