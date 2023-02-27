from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Welcome, name='welcome'),
    path('login', views.AdminLogin, name='admin-login'),
    path('create-review', views.CreateReview, name='create-reviews'),
    path('view-reviews', views.ViewReviews, name='view-reviews'    ),
]