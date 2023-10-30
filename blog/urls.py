from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main, name='main'),
    path('blog/', views.post_list, name= 'post_list'),
    path('write/', views.post_write, name='post_write'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('blog/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('blog/search/<str:tag>/', views.post_search_tag, name = 'post_search_tag'),
    path('blog/search/title/<str:title>/', views.post_search_title, name = 'post_search_title'),
    path('blog/<int:pk>/comment/new/', views.comment_new, name='comment_new'),

]