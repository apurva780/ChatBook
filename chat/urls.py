from django.urls import path,include
from . import views

app_name = 'chatting'

urlpatterns = [
    path('',views.add,name="add"),
    path('download',views.download,name="download")
    
]
