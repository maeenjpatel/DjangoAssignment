from django.shortcuts import render
from .models import QueryForm
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def formquery(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        sem = request.POST['sem']
        email = request.POST['email']
        tel = request.POST['tel']
        desc = request.POST['desc']

          
        queryf = QueryForm(name=name,dept=dept,sem=sem,email=email,tel=tel,desc=desc)
        queryf.save()
    return render(request,"myapp/form.html")