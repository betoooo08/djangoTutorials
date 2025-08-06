from django.urls import path
from .views import homePageView, aboutPageView, contactPageView, productIndexView, productShowView, ProductCreateView, ProductSuccessView

urlpatterns =[
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', productIndexView.as_view(), name='index'),
    path('products/<str:id>', productShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='form'),
    path('products/success/', ProductSuccessView.as_view(), name='success'),
]