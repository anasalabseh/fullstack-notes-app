from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.note_create_view, name='note-create'),
    path('', views.note_list_create_view, name='note-list'),
    path('<int:pk>/', views.note_retrieve_view, name='note-retrieve'),
    path('<int:pk>/update/', views.note_update_view, name='note-update'),
    path('<int:pk>/delete/', views.note_delete_view, name='note-delete'),
]
