from django.urls import path
from Lctl import views


urlpatterns = [
    path('', views.main , name="home"),
    # path('', views.cardhome , name="home"),
    path('home', views.cardhome , name="cardhome"),
    path('login', views.userlogin , name="login"),
    # path('register', views.createuser , name="register"),
    path('register', views.see , name="see"),
    path('registerfreelancer', views.createuser , name="createuser"),
    path('search/<slug:searchfor>', views.searchfor , name="searchfor"),
    path('search/', views.search , name="search"),
    path('search/freelancerprofile/<slug:id>', views.freelancer_profile , name="freelancerprofile"),
    path('freelancer-dashboard', views.freelancer_dashboard , name="freelancerdashboard"),
    path('freelancer-dashboard/work', views.freelancer_work , name="freelancerwork"),
    path('freelancer-dashboard/edit-freelancer-dashboard', views.edit_freelancer_dashboard , name="editfreelancerdashboard"),
    path('search/checkout/<slug:id>', views.checkout , name="checkout"),
    path('logout', views.userlogout , name="logout"),
    
]