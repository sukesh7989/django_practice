from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index" ),
    path("login/",views.Login,name="login" ),
    path("product/",views.Product,name="product" ),
    path("service/",views.Service,name="service" ),
    path("transport/",views.Transport,name="transport" ),
    
]
