from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView
from django.urls import path

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]