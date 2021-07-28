from django.urls import path
from . import views
app_name='post'


urlpatterns = [
    path('',views.post,name='post'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addPost/',views.addPost,name='addpost'),
    path('post/<slug:slug>/',views.detail,name='detail'),
    path('update/<slug:slug>/',views.update,name='update'),
    path('delete/<slug:slug>/',views.delete,name='delete'),
    path('comment/<slug:slug>',views.addCommit,name='comment'),
]
