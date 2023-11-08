from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author-api')
router.register('book', BookViewSet, basename='book-api')

urlpatterns = [
    path('', DemoView.as_view(), name='demo'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:author_id>/', AuthorView.as_view(), name='author'),
] + router.urls