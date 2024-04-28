from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    data = Student.objects.all()
    print(data)
    context = { "data" : data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def insertData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("Email")
        age = request.POST.get("Age")
        gender = request.POST.get("gender")

        print(name,email,age,gender)
        query = Student(name=name, email=email,age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")

def updateData(request,id):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["Email"]
        age = request.POST["Age"]
        gender = request.POST["gender"]
        # edit functionalities

        edit = Student.objects.get(id = id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()



        return redirect("/")

    d = Student.objects.get(id = id)
    context = { "d" : d}

    
    return render(request,"update.html",context)

def deleteData(request,id):
    d = Student.objects.get(id=id)
    d.delete()
    
    return redirect("/")


    