from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('routes/', views.get_routes, name='get_routes')
]
