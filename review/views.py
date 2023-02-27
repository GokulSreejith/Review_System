from django.shortcuts import render
from django.http import HttpResponse
from.forms import reviewR

# Create your views here
def Welcome(request):
    return render(request, 'welcome.html')

def ViewReviews(request):
    return render(request, "view-reviews.html")

def ReviewSuccess(request):
    return render(request, "review-success.html")

def CreateReview(request):
        if(request.method == "POST"):
            fm = reviewR(request.POST)
            print(fm)
            if fm.is_valid():
                fm.save()
                return render(request, "review-success.html")
        else:
            fm = reviewR()
            return render(request, "create-review.html",{'forms':fm})

def AdminLogin(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        print(username + password)
        return render(request, "admin-login.html")
    else:
        return render(request, "admin-login.html")