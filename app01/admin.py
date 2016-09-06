from django.contrib import admin

# Register your models here.


from app01 import models

admin.site.register(models.PushTarget)
admin.site.register(models.ProductionLine)
admin.site.register(models.Production)
admin.site.register(models.HostInfo)
