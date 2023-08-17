from django.db import models

# reference --> django model fields
# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  desc = models.TextField()
  date = models.DateField()

  # customise object name in database
  def __str__(self):
    return self.name

class Department(models.Model):
  name = models.CharField(max_length=150, null=False)
  location = models.CharField(max_length=150) 

  def __str__(self):
        return self.name

class Role(models.Model):
  name = models.CharField(max_length=50, null=False)

  def __str__(self):
    return self.name

class Employee(models.Model):
  first_name = models.CharField(null=False, max_length=50)
  last_name = models.CharField(max_length=50)
  profile_img = models.FileField(upload_to="profile/", default='profile/anonymous.jpg', max_length=250)
  salary = models.IntegerField(default=0)
  bonus = models.IntegerField(default=0)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  role = models.ForeignKey(Role, on_delete=models.CASCADE)
  phone = models.IntegerField(default=0)
  hired_at = models.DateField()

  def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)


# Complete process to make new model-    
  #1. after creating every model we have to register in admin.py i.e called model register
  #2. and then app register - from apps.py file copy class name and put it INSTALLED_APPS[] in setting.py  
  #3. then command on terminal --> python manage.py makemigrations 
  # {for making changes in model and make file for that}
  #4. Then after make up file we have to run cmd --> python manage.py migrate
  #  {for apply the pending changes created by makemigrations and store in table in our database (i.e in admin page)}
  

  # cmd -- python manage.py shell 
  # ref - making queries django
  # {for checking info about model like show objects and filter, get info and can make many complex queries} 
  # base query - model_name.objects. 