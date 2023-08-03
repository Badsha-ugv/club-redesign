from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('event/',views.event_view,name='event_view'),
    path('project/',views.project_view,name='project_view'),
    path('event/',views.blog_view,name='blog_view'),
    path('contest/',views.contest_view,name='contest_view'),
    path('rank/',views.rank_view,name='rank_view'),

    path('create/',views.create_project,name='create_project'),
    
    
]