from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, user_login, user_logout
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import admin_view, librarian_view, member_view
from django.urls import path
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Add other URL patterns here
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # Add other URL patterns here
]

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    # Add other URL patterns here
]

urlpatterns = [
    path('book/add/', views.add_book, name='add_book/'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book/'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]