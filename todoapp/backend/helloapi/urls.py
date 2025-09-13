from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.GreetingListCreate.as_view(), name='greeting_list'),
    path('items/<int:pk>/', views.GreetingRetrieveUpdateDestroy.as_view(), name='greeting_rud'),
]