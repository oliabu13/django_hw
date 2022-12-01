from django.contrib import admin
from django.urls import path

from books.views import books_view, book, first_page

urlpatterns = [
    path('', first_page, name='first_page'),
    path('books/', books_view, name='books'),
    path('books/<pub_date>/', book, name='book'),
    path('admin/', admin.site.urls),
]
