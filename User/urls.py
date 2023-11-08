from django.urls import path
from .views import *

urlpatterns = [
    path('login/', ObtainToken.as_view(), name='login'),
]