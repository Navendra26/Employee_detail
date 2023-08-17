from django.contrib import admin
from my_app.models import Contact
from my_app.models import Employee, Role,  Department

# Register your models here.
admin.site.register(Contact)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)



