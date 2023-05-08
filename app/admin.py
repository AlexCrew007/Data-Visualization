from django.contrib import admin
from app.models import dataBase
# Register your models here.

class dataBaseAdmin(admin.ModelAdmin):
    list_display=('id',)
    list_filter=('end_year','topic','sector','region','pestle','country')


admin.site.register(dataBase,dataBaseAdmin)