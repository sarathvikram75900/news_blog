from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('add_categories/',views.add_categories,name='add_categories'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('delete_category/<int:pk>',views.delete_category,name='delete_category'),

    path('posts/',views.posts,name='posts'),
    path('add_posts/',views.add_posts,name='add_posts'),
    path('edit_posts/<int:pk>',views.edit_posts,name='edit_posts'),
    path('delete_posts/<int:pk>',views.delete_posts,name='delete_posts'),



    path('users/',views.users,name='users'),
    path('add_users',views.add_users,name='add_users'),
    path('edit_user/<int:pk>/',views.edit_user,name='edit_user'),
    path('delete_user/<int:pk>/',views.delete_user,name='delete_user'),

]