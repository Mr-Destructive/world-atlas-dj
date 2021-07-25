from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/index.html')
def play(request):
    return render(request,'play/index.html')
