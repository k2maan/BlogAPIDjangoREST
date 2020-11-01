from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
