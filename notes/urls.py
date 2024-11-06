from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list),
    path('add-note/', views.add_note)
]
