from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
     path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('view_doctor',views.view_doctor,name='view_doctor'),
    path('view_patient',views.view_patient,name='view_patient'),
    path('view_appoinment',views.view_appoinment,name='view_appoinment'),
    path('delete_doctor(?p<int:pid>)/',views.delete_doctor,name='delete_doctor'),
    path('delete_patient(?p<int:pid>)/',views.delete_patient,name='delete_patient'),
    path('delete_appoinment(?p<int:pid>)/',views.delete_appoinment,name='delete_appoinment'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('add_appoinment/',views.add_appoinment,name='add_appoinment'),

]













