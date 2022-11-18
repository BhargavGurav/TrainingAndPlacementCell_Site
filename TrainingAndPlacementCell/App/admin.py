from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Training and Placement Cell GCOEJ | Adminstration'
admin.site.register(Mou)
admin.site.register(PlacementReport)
admin.site.register(Broucher)
admin.site.register(Student)
admin.site.register(Query)

