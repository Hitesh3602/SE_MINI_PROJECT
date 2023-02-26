from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render

def form(request):
    cursor=connection.cursor()
    cursor.execute("Select * from category")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context={
        'keyposts': posts
    }
    print(posts)
    return render(request,'grievancesystem/complaint.html',context)

def insert(request):
    cursor=connection.cursor()
    category=request.POST['category']
    date=request.POST['date']
    description=request.POST['description']
    print("aaya")
    print(category)
    print(date)
    print(description)
    
    cursor.execute("INSERT INTO grievance (description,date,status,CID) values (%s,%s, %s, %s)",(description,date,"pending",category))
    return render(request,'grievancesystem/dashboard.html')

def fetch(request):
    cursor=connection.cursor()
    cursor.execute("Select *,category.categoryName from grievance inner join category on grievance.CID=category.CID")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context={
        'keyposts': posts
    }
    print(posts)
    return render(request,'grievancesystem/viewcomplaint.html',context)

def dashboard(request):
    return render(request,'grievancesystem/dashboard.html')

def logout(request):
     return render(request,'grievancesystem/login.html')