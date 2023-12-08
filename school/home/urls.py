from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="topStudents"),
    path('blog/', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]