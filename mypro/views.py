from calendar import c
import re
from urllib import request
from django.shortcuts import render

def home(request):
    return render(request,"home.html", {})
    
