
from django.urls import path
from . import views
from .views import FileListView,FileDetailView,FileCreateView


urlpatterns =[
    path('',FileListView.as_view(),name='blog-home'),
    path('files/<int:pk>/',FileDetailView.as_view(),name='file-detail'),
    path('files/new/',FileCreateView.as_view(),name='file-create'),


    path('about/',views.about,name='blog-about'),


]