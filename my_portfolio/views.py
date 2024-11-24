from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

