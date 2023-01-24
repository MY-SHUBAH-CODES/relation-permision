from django.shortcuts import render
from django.http.response import HttpResponse
from .models import * 

# Create your views here.
def home(request,token=3):
    #get all data
    if token==1:
        data=User.objects.all()
        for i in data:
            print(i.username,i.password)        
            return HttpResponse("pakad lia")
    #get all data using parent table in one to one relation.use "table name_field name " in filter.note table name should be paa in small like User_detail-->>user_detail
    if token==2:
        data=User.objects.filter(user_detail__father_name='papa')
        for i in data:
            print(i.username,i.password)
        return HttpResponse("pakad lia")
    #note: i may have get more than two records for one matched row in child table because of many to many relation(hint: may be two user involves in one records of book) 
    if token==3:
        data=User.objects.filter(book__book_name='mylife')
        for i in data:
            print(i.username,i.date_joined,i.is_active,i.is_superuser)
        return HttpResponse("pakad lia")

    # if token==4:
    #     data=User.objects.filter(book__writt='mylife')
    #     for i in data:
    #         print(i.username,i.date_joined,i.is_active,i.is_superuser)
    #     return HttpResponse("pakad lia")


    


