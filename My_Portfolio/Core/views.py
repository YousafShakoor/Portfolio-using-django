from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm
# Create your views here.
def index(request):
    head=Header.objects.all()
    educations=education.objects.all()
    experiences=experience.objects.all()
    skill=skills.objects.all()
    portfolios=portfolio.objects.all()
    details=detail.objects.all()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ContactForm()
    return render(request,'index.html',{
        'head':head,
        'form':form,
        'skills':skill,
        'educations':educations,
        'experiences':experiences,
        'portfolios':portfolios,
        'details':details,
    })