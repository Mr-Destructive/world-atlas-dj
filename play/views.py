from django.shortcuts import render

# Create your views here.
def play(request):
    return render(request,'play/index.html')
def home(request):
    return render(request,'home/index.html')
def bot(request):
    return render(request,'play/bot.html')

def room(request):
    return render(request,'room/room.html')
