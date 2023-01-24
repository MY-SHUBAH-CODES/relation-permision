from django.contrib import admin
from .models import *

class User_detailadmin(admin.ModelAdmin):
    list_display=['id','user','father_name','mother_name','education','age','hobby']
admin.site.register(User_detail,User_detailadmin)

class Postadmin(admin.ModelAdmin):
    list_display=['id','user','post_text']
admin.site.register(Post,Postadmin)

class Bookadmin(admin.ModelAdmin):
    list_display=['id','book_name','writtenby','writers']
admin.site.register(Book,Bookadmin)


