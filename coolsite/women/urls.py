from django.urls import path, re_path
from women.views import *

app_name = 'women'

urlpatterns = [
    path('',index,name='home'),
    path('addpage/',addpage,name='add_page'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/',show_category, name='category')
]
