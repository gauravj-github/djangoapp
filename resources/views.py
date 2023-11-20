from django.shortcuts import render
from django.http import HttpResponse
import datetime



# Create your views here.

def home(request):
    if request.method=='post':
         n= request.POST.get("nam")
         print(n,"jeygfj")

    date=datetime.datetime.now()
    
    is_Active=True

    name="Gaurav"

    list_of_program=[
          'write a code for even and odd',
         'write a code for prime numbewr',
        'write a code for armstrong number',
        'write a code for leapyear',
         'write a code for even and odd',
         'write a code for prime numbewr'
    ]
 
    student={
               'student_name':"ravi",
               'student_id':"nagv",
                'student_college':"XYX"
    }

    data={
        'date':date,
         'is_Active':is_Active,
          'name':name,
         'list_of_program':list_of_program,
         'student_data':student
        
         
                
    }

    print("test function")
    #return HttpResponse("<h1>hellow this is index page</h1>"+str(date))
    return render(request,"hoime.html",data)

def about(request):
    #return HttpResponse("<h1>this is about page<h1/>")
     return render(request,"about.html",{})
def services(request):
    #return HttpResponse("<h1>this is services page<h1/>")
     return render(request,"services.html",{})
    