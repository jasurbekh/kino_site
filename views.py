from rest_framework.generics import ListAPIView
from blog.models import Article, Category
from .serializers import ArticleSerializers, CategorySerializers


class ArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category
