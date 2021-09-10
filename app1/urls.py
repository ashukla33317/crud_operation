from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='Home'),
    path('rem',views.Delete_data.as_view(),name="rem")
]
