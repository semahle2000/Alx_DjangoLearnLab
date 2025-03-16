from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

"""
Unit tests for the Book model endpoints.
- Test CRUD operations.
- Test filtering, searching, and ordering functionalities.
- Test permissions and authentication mechanisms.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(title="Book Title", publication_year=2023, author=self.author)

    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Author Name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2023)