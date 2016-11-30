from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import random
import math


# Create your views here.

def tsp(request):
    return render(request,'blog/tsp.html',{})

@csrf_exempt
def trip(request):
    print("yes")
    out = json.loads(request.body.decode('utf-8'))
    print(out)
    print(out[0])
    print(len(out))
    print(len(out[0]["city0"]))
    durations = []
    for i in range(0,len(out)):
        durations.append(out[i]["city"+str(i)])
        #print(durations[i])
    durm = np.asarray(durations)
    #print(durm)
    d,totaltime=simulated(durm)
    flat = ordering(d)
    print("original",d)
    print("flatten",flat)
    jslist = json.dumps([{"path":flat},{"totaltime":totaltime.item()}])
    return HttpResponse(jslist)

#objective function
def objective(routes,durm):
   distance=0
   for a,b in routes:
       distance+=durm[a][b]
   
   return distance
   
       
#generate initial solution
def initialsolution(row):
   initial=[]
   for i in range(row):
       if i < row-1:
           initial.append([i,i+1])
       if i == row-1:
           initial.append([i,initial[0][0]])
   return initial
   
#swap cities
def swap(route,row):
   city1=random.randrange(row)
   city2=random.randrange(row)
          
   for l in route:
       if l[0] == city1:
           l[0]='tmp'
       elif l[1] == city1:
           l[1]='tmp'
   
   for l in route:
       if l[0] == city2:
           l[0]=city1
       elif l[1] == city2:
           l[1]=city1
   
   
   for l in route:
       if l[0]=='tmp':
           l[0]=city2
       elif l[1]=='tmp':
           l[1]=city2
           
   return route

def simulated(durm):
   row,col=durm.shape
   path=initialsolution(row)
   cost=objective(path,durm)
   T=0.1
   Tmin=0.000001
   alpha=0.9
   while T>Tmin:
       n=1
       while n<10:
           n+=1
           newpath=swap(path,row)
           newcost=objective(newpath,durm)
           deltaE=cost-newcost
           if deltaE<0:
               cost=newcost
               path=newpath
           elif random.random() < math.exp(-deltaE/T):
               cost=newcost
               path=newpath
       T=T*alpha
       
   return path,cost

#return ordered path
def ordering(path):
   reorder=[path[0][0]]
   for a in path:
       for b in path:
           if a[1]==b[0] and b!=reorder[0]:
               reorder.extend([b[0]])

   return reorder


