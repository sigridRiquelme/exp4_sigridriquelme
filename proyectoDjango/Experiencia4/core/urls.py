from django.urls import path
from .views import index
from .views import crud


urlpatterns =[
    path ('', index, name="index"),
    path ('crud', crud, name='crud'),
]

