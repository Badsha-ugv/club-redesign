from django.urls import path 
from . import views 


urlpatterns = [
    path('test/',views.test) ,
    path('register/',views.register_view,name='register_view') ,
    path('login/',views.login_view,name='login_view') ,
    # path('',views.home_view,name='home_view') ,
    path('profile/<slug:slug>', views.user_profile_view,name='user_profile_view'),


    
]