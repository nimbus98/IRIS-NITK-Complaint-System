from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.template import loader

from .models import form,users,form2
from .forms import ApplicationForm,UserForm,form21,GuestForm



def index(request):
    template = loader.get_template('Portalapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def complaint(request):
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')
    else:
        f = ApplicationForm()
    
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'form':f,}
    return HttpResponse(template.render(context, request))

def confirmation(request):
    template = loader.get_template('Portalapp/sub/information.html')
    context = {}
    return HttpResponse(template.render(context, request))
def Admin(request):
    error=""
    if request.POST:
        f=UserForm(request.POST)
        if f.is_valid():
            q= get_object_or_404(users, usergroup=f.cleaned_data['usergroup'])
            if f.cleaned_data['user_name']==q.user_name :
                if f.cleaned_data['password']==q.password :
                    if f.cleaned_data['usergroup']=="Admin":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite'))
                    elif f.cleaned_data['usergroup']=="User":
                        return HttpResponseRedirect(reverse('Portalapp:usersite'))
                else:
                    error="Password is incorrect"
                    template = loader.get_template('Portalapp/sub/admin.html')
                    context = {'error':error,'form':f,}
                    return HttpResponse(template.render(context, request))
            else:
                error="Username is incorrect"
                template = loader.get_template('Portalapp/sub/admin.html')
                context = {'error':error,'form':f,}
                return HttpResponse(template.render(context, request))
    else:
        f=UserForm()
    template = loader.get_template('Portalapp/sub/admin.html')
    context = {'error':error,'form':f,}
    return HttpResponse(template.render(context, request))

def adminsite(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    names=form.objects.values_list('name', flat=True).filter(approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(approval=False)
    date=form.objects.values_list('date', flat=True).filter(approval=False)
    info=form.objects.values_list('info', flat=True).filter(approval=False)
    email=form.objects.values_list('email', flat=True).filter(approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approvalfunc')

    context = {'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
	
    
def approvalfunc(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite')


def usersite(request):
    template = loader.get_template('Portalapp/sub/approved.html')
    names_n=form.objects.values_list('name', flat=True).filter(approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(approval=True)
    approval=form.objects.values_list('approval', flat=True).filter(approval=False)

    context = {'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))