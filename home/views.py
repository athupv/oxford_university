from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from Account.models import  Staff,Contact
from home.models import  Students

from.forms import StudentForm


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
    
class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquiry.html',{'form':customer})
class Staffdetails(View):
    def get(self,request):
        staff=Staff.objects.all()
        return render(request,'staff.html',{'form':staff})
    
class Addstudent(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'students.html',{'form':std1})
    def post(self,request):
        if request.method == "POST":
            std1=StudentForm(request.POST)
            if std1.is_valid():
                std1.save()
                student=Students.objects.all()
                return render(request,'showstudent.html',{'form':student})
            else: 
                print("Form is not valid")
            return redirect('showstudents')
        
class Showstudents(View):
     def get(self,request):
         std=Students.objects.all()
         return render(request,'showstudent.html',{'form':std})
        
       
class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Students.objects.filter(student_id=edit1)
        return render(request,'edit.html',{'form':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Students.objects.filter(student_id=edit1).exists():
                if request.POST['student_address']:
                    Students.objects.filter(student_id=edit1).update(student_address=request.POST['student_address'])
                if request.POST['student_place']:
                    Students.objects.filter(student_id=edit1).update(student_place=request.POST['student_place'])
                if request.POST['student_name']:
                    Students.objects.filter(student_id=edit1).update(student_name=request.POST['student_name'])
                if request.POST['student_email']:
                    Students.objects.filter(student_id=edit1).update(student_email=request.POST['student_email'])
                if request.POST['student_phone']:
                    Students.objects.filter(student_id=edit1).update(student_phone=request.POST['student_phone'])
                student=Students.objects.all()
                return render(request,'showstudent.html',{'form':student})
            
class Delete(View):
        def get(self,request):
            delete=request.GET['delete']
            Students.objects.filter(student_id=delete).delete()
            student=Students.objects.all()
            return render(request,'showstudent.html',{'form':student})

class Profile(View):
       def get(self,request):
           if request.session['email'] is not None:
               user=Staff.objects.filter(email=request.session['email'])
               return render(request,'myprofile.html',{'form':user})
           
class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'editprofile.html',{'form':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method=="POST":
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"email id already exists")
                        return render(request,'editprofile.html',{'form':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'myprofile.html',{'form':customer})


                
    












