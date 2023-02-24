from django.shortcuts import render

def project(request):
   return render(request,"project.html")

def article(request):
   return render(request,"articles.html") 

def paintings(request):
   return render(request,"paintings.html") 

