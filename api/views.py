from urllib import request
from .models import Article
from .models import Category
from .models import Comment
from .serializers import ArticleSerializer
from .serializers import CategorySerializer
from .serializers import CommentSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


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


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by('-created_date')
    serializer_class = CategorySerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializers

    def get_queryset(self):

        article = self.request.query_params.get('article')
        return Comment.objects.all().filter(article=article).order_by('-created_date')
