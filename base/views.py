from django.shortcuts import render
from base import models as base_models

def index(request):
    services=base_models.Service.objects.all()
    
    context={
        "services": services
    }
    return render(request, 'base/index.html',context)

def service_detail(request,service_id):
      services=base_models.Service.objects.get()
    return render(request, 'base/service_detail.html')