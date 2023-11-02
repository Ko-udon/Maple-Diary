from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.main, name='main'),
    path('', views.post_list, name= 'post_list'),
    path('write/', views.post_write, name='post_write'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('search/<str:tag>/', views.post_search_tag, name = 'post_search_tag'),
    path('<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('<int:pk>/comment/<int:parent_comment>/reply/', views.comment_reply, name='comment_reply'),
    path('post_detail_fail/', views.post_detail_fail, name = 'post_detail_fail'),
    # path('cube_history/', views.cube_history, name = 'cube_history')
]