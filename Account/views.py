from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from .models import Course,Staff


 

# Create your views here.

def contacts(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phone'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
        return render(request,'contacts.html',dicts)
    return render(request,'contacts.html')

def course(request):
  courses={
  'course':Course.objects.all()
  }
  return render(request,'course.html',courses)

def gallery(request): 
    return render(request,'gallery.html')
def mainhome(request):
    return render(request,'mainhome.html')



def trainer(request):
    return render(request,'trainer.html')    

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email']=check_user.email
            request.session['name']=check_user.name
            request.session['phno']=check_user.phno
            return redirect('home')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username and password')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phno = request.POST['phno']
        password2 = request.POST['password2']
        if password == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'This email is taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password is not match')
            return redirect('signup')
    else: 
        return render(request,'signup.html')
    return render(request,'signup.html')

def forgot(request):
   
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('login')
        else:
            messages.error(request,'Invalid email id')
            return redirect('forgot')
    return render(request,'forgot.html')
    

