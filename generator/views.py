from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    thePassword=""
    length=10
    for x in range(length):
        thePassword +=random.choice(characters)
    return render(request,'generator/password.html',{'password':thePassword})