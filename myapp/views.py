from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from.models import Doctor,Patient,Appoinment


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def login(request):
   if request.method == "POST":
      username=request.POST['username']
      password=request.POST['pwd']
      user= auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         messages.info(request,'logged out sucsessfully')
         return redirect('dashboard')
        
      else:
         messages.info(request,'invalid credentials')
         return redirect('login')

   return render(request,'login.html') 

def logout(request):
   auth.logout(request)

   return redirect('login')
def index(request):
   if not request.user.is_staff:
        return redirect('login')
   doctors=Doctor.objects.all()
   patients=Patient.objects.all()
   appoinments=Appoinment.objects.all()

   d=0
   p=0
   a=0
   for i in doctors:
       d+=1
   for i in patients:
       p+=1
   for i in appoinments:
       a+=1
   d1={'d':d,'p':p,'a':a}

   return render(request,'index.html',d1) 

def view_doctor(request):
   doc=Doctor.objects.all()
   d={'doc':doc}
   return render(request,'view_doctor.html',d)

def delete_doctor(request,pid):
    
      doctor = get_object_or_404(Doctor, id=pid)
      doctor.delete() 
      return redirect('view_doctor')
def add_doctor(request):
   if not request.user.is_staff:
      return redirect('view_doctor')

   if request.method == "POST":
      n=request.POST['Name']
      m = request.POST.get('mobile')  
      sp=request.POST['special']
      Doctor.objects.create(Name=n,mobile=m,special=sp)
      messages.success(request, 'Profile details updated.')
   
      return redirect('view_doctor')
   return render(request,'add_doctor.html')

def view_patient(request):
   doc=Patient.objects.all()
   d={'doc':doc}
   return render(request,'view_patient.html',d)

def delete_patient(request,pid):
    
      patient = get_object_or_404(Patient, id=pid)
      patient.delete() 
      return redirect('view_patient')

def add_patient(request):
   if not request.user.is_staff:
      return redirect('view_patient')

   if request.method == "POST":
      n = request.POST['Name']  # Use lowercase
      m = request.POST.get('mobile')  
      g = request.POST['gender']
      ad = request.POST['adress']
      Patient.objects.create(Name=n, mobile=m, gender=g, adress=ad)  # Use lowercase in the model
      messages.success(request, 'Profile details updated.')
   
      return redirect('view_patient')
   return render(request, 'add_patient.html')


def add_appoinment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()  # Correct this line to fetch from Patient model
    if request.method == "POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        dt = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name=d).first()
        patient = Patient.objects.filter(Name=p).first()

        try:
            Appoinment.objects.create(Doctor=doctor, Patient=patient, Date=dt, Time=t)
            error = "no"
        except:
            error = "yes" 

    context = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appoinment.html', context)

def view_appoinment(request):
   doc=Appoinment.objects.all()
   d={'doc':doc}
   return render(request,'view_appoinment.html',d)

def delete_appoinment(request,pid):
    
      app = get_object_or_404(Appoinment, id=pid)
      app.delete() 
      return redirect('view_appoinment')




      






























      
      










































































