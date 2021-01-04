
from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.eeelist, name='eeelist'),
    path('electriciansreg',views.electricianreg, name='electriciansreg'),
    path('<int:e_id>',views.detailjobe, name='detailjobe'),
    path('<int:e_id>/eupvote',views.eupvote, name='eupvote'),
    
    

]
