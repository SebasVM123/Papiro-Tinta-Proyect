from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def login_view(request):
    return render(request, 'main/login.html')

def register_view(request):
    return render(request, 'main/register.html')