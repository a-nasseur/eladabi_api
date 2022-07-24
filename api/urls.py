from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(),
         name='articles_details'),
    path('articles/featured/', views.FeaturedArticle.as_view(),
         name='featured_article'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('comments/', views.CommentList.as_view(), name='comments'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
