from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'text':"Hellow world", 'number': 400}
    return render(request,'basic_app/index.html', my_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/basic_relative_templaste.html')
