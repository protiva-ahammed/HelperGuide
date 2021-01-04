
from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.createjoblist, name='createjoblist'),
    path('create',views.create, name='create'),
    path('<int:createjob_id>',views.detailjob, name='detailjob'),
    path('<int:createjob_id>/upvote',views.upvote, name='upvote'),
    
    

]
