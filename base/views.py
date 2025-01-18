from django.shortcuts import render

def index(request):
    return render(request, 'base/index.html')

def service_detail(request,service_id):
    return render(request, 'base/service_detail.html')