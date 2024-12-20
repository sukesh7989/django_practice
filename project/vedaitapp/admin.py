from django.contrib import admin

# Register your models here.
from .models import Admission

class AdmissionAdmin(admin.ModelAdmin):
    list_display=('id','stu_name','stu_father','joindate','stu_class','fees')
    
admin.site.register(Admission,AdmissionAdmin)
       