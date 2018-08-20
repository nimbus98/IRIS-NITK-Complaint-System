from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from .models import form,users,form2

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    branch = forms.CharField(max_length=100)
    roll_number = forms.CharField(max_length=100)  
    date = forms.CharField(max_length=100)
    info = forms.CharField(required=False,max_length=1000)
    email= forms.EmailField()
    phone= forms.CharField(max_length=100)
    address= forms.CharField(max_length=1000)
	
    def save(self):
        new_entry = form.objects.create(
            name = self.cleaned_data['name'],
		    branch = self.cleaned_data['branch'],
		    roll_number = self.cleaned_data['roll_number'],
	        date = self.cleaned_data['date'],
		    info = self.cleaned_data['info'],
		    email = self.cleaned_data['email'],
		    phone = self.cleaned_data['phone'],
		    address = self.cleaned_data['address'],
			)
        return new_entry
	
    def clean_name(self):
        name = self.cleaned_data['name']
        count=0
        for i in name:
            if i.isalpha()==False:
                count=count+1
        if count>0:
            raise ValidationError("Name can only contain alphabets")
        return name
	
    def clean_branch(self):
        branch = self.cleaned_data['branch']
        count=0
        for i in branch:
            if i.isalpha()==False:
                count=count+1
        if count>0:
            raise ValidationError("Branch can only contain alphabets")
        return branch
		
    def clean_roll_number(self):
        roll_number = self.cleaned_data['roll_number']
        count=0
        for i in roll_number:
            if i.isalnum()==False :
                count=count+1
        if count>0 or len(roll_number)==0:
            raise ValidationError("Roll number can only contain alphabets and numbers and it cannot be left empty")
        return roll_number
	
    def clean_date(self):
        date = self.cleaned_data['date']
        count=0
        for i in date:
            if i.isalpha()==True:
                count=count+1
        if count>0:
            raise ValidationError("Date cannot contain alphabets")
        return date
		
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        count=0
        for i in phone:
            if i.isnumeric()==False:
                count=count+1
        if count>0:
            raise ValidationError("Phone number can only contain numbers")
        return phone
	
	
class UserForm(forms.Form):
    usergroup = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100) 

class GuestForm(forms.Form):
    usergroup = forms.CharField(max_length=100)  
	
class form21(forms.Form):
    approval = forms.IntegerField()
	
    def save(self):
        new_entry = form2.objects.create(
            approval = self.cleaned_data['approval'],
        )
        return new_entry