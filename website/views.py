from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home (request):
    isActive=False
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None:isActive=False
        else:isActive=True
    name="Shravya"
    list_of_programs=['WAP to check even or odd',
                      'WAP to check palindrome or not',
                      'WAP to print all prime numbers',
                      'WAP to print pascals triangle']
    student={
        'student_name':"Shravya",
        'student_college':"GNITS",
        'student_city':"Hyd"
    }
    data={
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)
def about(request):
    return render(request,"about.html",{})
def services(request):
    return render(request,"services.html",{})
