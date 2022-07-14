from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-created_date')
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class FeaturedArticle(generics.ListAPIView):
    queryset = Article.objects.all().filter(featured=True)
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

