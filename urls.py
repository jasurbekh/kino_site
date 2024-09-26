from django.urls import path
from .views import ArticleView, CategoryView


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('categories/', CategoryView.as_view()),
]