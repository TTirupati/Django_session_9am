from django.shortcuts import render
from django.http import HttpResponse

#we will call this as a view
def homepage(request):
    return render(request, 'registration_app/home.html')

def user_registration(request):
    return render(request, 'registration_app/user_registration.html')

def user_login(request):
    return render(request, 'registration_app/user_login.html')


def user_details(request):
    #this data will come from database: assume
    db_data={'id':1010,'first_name':'John','last_name':'parker','email':'John@gmail.com'}
    return render(request, 'registration_app/user_details.html',context={'data':db_data})
