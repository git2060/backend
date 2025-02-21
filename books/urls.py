from django.urls import path
from .views import BksBookListView

urlpatterns = [
    path("books/", BksBookListView.as_view(), name="book-list"),
]
