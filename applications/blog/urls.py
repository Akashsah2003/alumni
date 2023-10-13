from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    path('viewblog/<str:blogid>', views.view_blog, name='view__blog'),
    path('createblog', views.create_blog, name='createblog'),
]
