from django.contrib import admin
from .models import Emp,Testimonial
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','emp_id')
    search_fields=('name','emp_id')
    list_filter=('working',)
# Register your models here.
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)