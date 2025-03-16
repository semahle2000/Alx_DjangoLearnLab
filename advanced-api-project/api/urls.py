from django.urls import path
from .views import TestView
from .views import BookListView, BookDetailView

urlpatterns = [
    path('test/', TestView.as_view(), name='test-view'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]