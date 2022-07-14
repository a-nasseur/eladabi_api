from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='articles_details'),
    path('articles/featured/', views.FeaturedArticle.as_view(), name='featured_article' )
]

urlpatterns = format_suffix_patterns(urlpatterns)