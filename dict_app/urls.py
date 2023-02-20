from django.urls import path
from dict_app import views




urlpatterns = [
    path("",views.home,name="home"),
    path("base",views.base,name="base"),
    path("log",views.login_view,name="log"),
    #add teacher data
    path("add",views.teacher_add,name="add"),
    #view data
    path("view",views.view,name="view")

    

   
]