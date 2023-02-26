from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Welcome, name='welcome'),
    path('login', views.AdminLogin, name='admin-login'),
    path('create-review', views.CreateReview, name='create-reviews'),
    path('view-reviews', views.ViewReviews, name='view-reviews'
    # ,{
    #     reviews: [
    #         {
    #         "name": "Anna Kendrick",
    #         "profileURL": "https://i.ibb.co/QcqyrVG/Mask-Group.png",
    #         "time":"14 July 2021"
    #         "title":"Beautiful addition to the theme",
    #         "description":"When you want to decorate your home, the idea of choosing a decorative theme can seem daunting. Some themes seem to have an endless amount of pieces, while others can feel hard to accomplish",
    #         "images": ["https://i.ibb.co/QXzVpHp/vincent-wachowiak-8g-Cm-EBVl6a-I-unsplash-1.png","https://i.ibb.co/znYKsbc/vincent-wachowiak-z-P316-KSOX0-E-unsplash-1.png"]
    #     },
    #         {
    #         "name": "James Schofield",
    #         "profileURL": "https://i.ibb.co/RCTGZTc/Mask-Group-1.png",
    #         "time":"23 June 2021",
    #         "title":"Comfortable and minimal, just how I like it!",
    #         "description":"This style relies more on neutral colors with little to no embellishment on furniture. Lighter fabrics, such as silk and cotton, are popular, as are lighter colors in wood and metal.",
    #         "images":["https://i.ibb.co/xfg5T5T/sam-moqadam-kvmds-Tr-GOBM-unsplash-removebg-preview-1.png","https://i.ibb.co/54F7vvV/Group-1855.png"]
    #     },
    #     ]
    # }
    ),
]
