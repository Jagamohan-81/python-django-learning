from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("<h1>Welcome to lipuns first web app in django</h1> ")

def contactUs(request):
    return HttpResponse("Welcome to contactus page")
def blogDetails(request,blogName):
    return HttpResponse(blogName)
def home(request):
    return HttpResponse("Home page")