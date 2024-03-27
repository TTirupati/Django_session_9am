from django.http import HttpResponse

def index_page_order(request):
    return HttpResponse("<h1>hello you are at Order App- Index Page</h1>")