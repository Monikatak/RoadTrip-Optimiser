from django.shortcuts import render

# Create your views here.

def tsp(request):
    return render(request,'blog/tsp.html',{})
