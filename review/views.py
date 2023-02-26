from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def Welcome(request):
    return render(request, 'welcome.html')

def ViewReviews(request):
    return render(request, "view-reviews.html")

def CreateReview(request):
    return render(request, "create-review.html")

def AdminLogin(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        print(username + password)
        return render(request, "admin-login.html")
    else:
        return render(request, "admin-login.html")