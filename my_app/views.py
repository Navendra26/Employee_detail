from django.shortcuts import render, HttpResponse, redirect
from my_app.models import Contact, Employee
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.db.models import Q

# Create your views here.
def index(request):
  #dictionary
  context = {
     "var1": "this is val1",
     "var2": "this is val2"
  }
  print(request.user)
  if request.user.is_anonymous:
    return redirect("/login")
  return render(request,'index.html',context)
 # return HttpResponse("This is homePage") #if we want to response a string we use this otherwise we will use Templates

def about(request):
  return render(request, 'about.html')
  # return HttpResponse("this is About us page")

def services(request):
   return render(request, 'services.html')
  # return HttpResponse("this is service page")

def contact(request):
  # logic for adding contact 
   if request.method == "POST":
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     desc = request.POST.get('desc')
     # object of Contact class 
     contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
     contact.save()
     messages.success(request, "Your messages has been submitted.")
   return render(request, 'contact.html')
  # return HttpResponse("this is contact us page")

def loginUser(request):
  if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      #check if user has entered correct credentials, ref --> django auth
      user = authenticate(username=username, password=password)  # authenticate means to check whether user exists or not
      print(username, password)

      if user is not None:
        #A backend authenticated the credentials
        login(request, user)
        return redirect("/")
      else:
        # No backend authenticated the credentials
        return render(request, 'login.html')
  return render(request, 'login.html')

def logoutUser(request):
  logout(request)
  return redirect("/login")

def addEmp(request):
  if request.method == "POST":
    # we can also post a model like this 
    """ 
    first_name = request.POST.get('first_name')
    salary = int(request.POST.get('salary')) 
    """
    # this syntax is also good way to send (use which ever is convinient to you)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    salary = int(request.POST['salary'])
    bonus = int(request.POST['bonus'])
    department = int(request.POST['department'])
    phone = int(request.POST['phone'])
    role =int(request.POST['role'])
    
    new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, phone=phone, bonus=bonus, department_id=department, role_id=role, hired_at=datetime.now())
    new_emp.save()
    return HttpResponse("An employee has been added to the department!")
  
  elif request.method == "GET":
    return render(request, 'add_emp.html')

  else:
    return HttpResponse("an exception occured!")

def allEmp(request):
  emps = Employee.objects.all()
  context = {
    "emps": emps
  }
  print(emps)
  return render(request, 'all_emp.html', context)

def removeEmp(request, emp_id = 0):
  if emp_id:
    try:
      instance = Employee.objects.get(id=emp_id)
      instance.delete()
      return HttpResponse("Employee Removed successfullly!")
    except:
      return HttpResponse("Please Enter a valid ID!")
  emps = Employee.objects.all()
  context = {
    "emps": emps
  }
  return render(request, 'remove_emp.html', context)

def filterEmp(request):
  if request.method == "POST":
    name = request.POST['name']
    department = request.POST['department']
    role = request.POST['role']
    emps = Employee.objects.all()
    if name:
      # Q object used for conditional statement like (or, and, not).
      # icontains used when we dont want case sensitive and contains any character will be filtered
      # __icontains and __name is part of syntax
      emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name)) 
    if department:
      emps = emps.filter(department__name__icontains = department)
    if role:
      emps = emps.filter(role__name__icontains = role)

    context = {
      'emps': emps
    }
    return render(request, 'all_emp.html', context)

  elif request.method == "GET":
    return render(request, 'filter_emp.html')
  else:
    return HttpResponse("An Exception Occured!")