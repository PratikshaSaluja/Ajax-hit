from django.shortcuts import render
from .forms import studentregsitration
from .models import testuser1
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    form = studentregsitration()
    data = testuser1.objects.all()
    return render(request, 'home.html', {'form':form, 'data':data})
# @csrf_exempt
def save(request):
    if request.method=="POST":
        form = studentregsitration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            usr = testuser1(name=name , email=email , password=password)
            usr.save()
            data = testuser1.objects.values()
            data_list = list(data)
            return  JsonResponse({'status':'Save', 'data_list1' :data_list})
        else:
            return JsonResponse({"status":'Failed'})