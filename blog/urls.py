from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('get_post_by_category/<int:category_id>/',views.get_post_by_category,name='get_post_by_category'),
    path('single_post/<int:pk>/',views.single_post,name='single_post'),
    path('search/',views.search,name='search'),
]