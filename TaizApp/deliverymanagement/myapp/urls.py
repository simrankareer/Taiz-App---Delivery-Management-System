from django.contrib import admin
from django.urls import path
from myapp import  views

urlpatterns = [
    path("", views.index,name="home"),
    path("about", views.about,name="about"),
    path("order", views.place_order,name="Place Order"),
    path("myorders/", views.myorders,name="My Order"), #used to view user' orders
    path("contact", views.contact,name="Contact US"),
    path("delivery", views.delivery,name="Delivery Management"),
    path("viewassigned", views.viewassigned,name="Your Assigned Deliveries"), #used to view assigned orders by Delivery agents
    path("updatestatus/<int:id>/", views.updatestatus,name="Update order Status"),
    path("vieworder", views.vieworder,name="All Orders"), #used by shops to view order placed by customer
    #path("assigndriver/<int:id>/", views.assigndriver,name="Shop Action Portal"),
    path('create_order/', views.create_order, name='create_order'), #used by shops to add drivers and status
    path('register', views.register, name='register'),
    #path('place_order/', views.place_order, name='place_order'),
    
]