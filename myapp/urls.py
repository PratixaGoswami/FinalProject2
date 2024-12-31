from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index),
   
    path("hiree/",views.hireee,name='hiree'),
    path("contact/",views.contact),
   

    
    path("hiree/",views.hireee,name='hiree'),
    path("add_worker/",views.add_worker,name="add_worker"),
    path("update_worker/",views.update_worker,name='update_worker'),
    path("deleteworker/",views.deleteworker,name='deleteworker'),
    path('verify_worker/',views.verify_worker,name="verify_worker"),

    path("job/",views.job,name='job'),
    path("add_job/",views.add_job,name="add_job"),
    path("updatejob/",views.updatejob,name='updatejob'),
    path("deletejob/",views.deletejob,name='deletejob'),
    path('verify_job/',views.verify_job,name="verify_job"),
    
    path("signup/",views.signup,name='signup'),
    path("login/",views.login,name='login'),
    path("otpverify/",views.otpverify,name="otpverify"),
    path('userlogout/',views.userlogout),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('search/', views.search_data, name='search_users'),

    path("password_reset_request/",views.forgetpassword ,name='password_reset_request'),
    path("newpasswordpage/<int:user>/",views.newpasswordpage, name='newpasswordpage'),

   
    # Password reset views
   
   
    
    
  
]