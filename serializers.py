from rest_framework import serializers
from blog.models import Article, Category


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', 'content', 'created_at', 'updated_at', 'views')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('title',)
