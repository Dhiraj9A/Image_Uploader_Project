from django.shortcuts import render,redirect
from . models import img_uploder
from . form import *
# Create your views here.
                                #......................home..........................#
def index(request):
    if request.method=='POST':
        form=img_form(request.POST,request.FILES)
        form.save()
    form=img_form() 
    img=img_uploder.objects.all()
    data={
        'form':form,
         'img':img
    }   
    return render(request,'index.html',data)

                                #......................delete............................#
def delete(request,id):
    dlt=img_uploder.objects.get(id=id)
    dlt.delete()
    return redirect('home')


