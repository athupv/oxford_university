from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        
        labels = {
                'student_id' : 'Student Id',
                'student_name' : 'Student Name',
                'student_phone' :'PhoneNumber',
                'student_email' : 'Email',
                'student_address' : 'Address',
                'student_place':'Place'
                
            }
            
  
         