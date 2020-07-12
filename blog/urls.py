from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import index, create, update, detail, delete, palindrome_check, BlogList, BlogDetail
app_name = 'blog'
urlpatterns = [
    path('', index, name='home'),
    path('api/', BlogList.as_view(),name='api_home'),
    path('api/<int:pk>/', BlogDetail.as_view()),
    path('blog/create/', create, name='create'),
    path('blog/<int:id>/update', update, name='update'),
    path('blog/<int:id>/', detail, name='detail'),
    path('blog/<int:id>/delete', delete, name='delete'),
    path('blog/palindrome/<int:id>/', palindrome_check, name='palindrome'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
