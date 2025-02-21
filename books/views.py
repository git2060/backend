from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .models import BksBook
from rest_framework.pagination import PageNumberPagination
from .serializers import BookSerializersView


class PageLimit(PageNumberPagination):
    page_size=25

class BksBookListView(generics.ListAPIView):
    serializer_class = BookSerializersView
    pagination_class=PageLimit

    def get_queryset(self):
        queryset = BksBook.objects.all()
        

        gutenberg_id = self.request.query_params.get("gutenberg_id", None)
        title = self.request.query_params.get("title", None)
        author = self.request.query_params.get("author", None)
        languages = self.request.query_params.get("language", None)
        topics = self.request.query_params.get("topic", None)
        mime_type = self.request.query_params.get("mime_type", None)

        if gutenberg_id:
            queryset = queryset.filter(gutenberg_id=gutenberg_id)

        if title:
            queryset = queryset.filter(title__icontains=title)

        if author:
            queryset = queryset.filter(book_authors__author__name__icontains=author)

        if languages:
            language_list = languages.split(",")  # Convert "en,fr" to ['en', 'fr']
            queryset = queryset.filter(language_book__language__code__in=language_list)

        if topics:
            topic_list = topics.split(",")  # Convert "child,infant" to ['child', 'infant']
            topic_filter = Q()
            for topic in topic_list:
                topic_filter |= Q(subjects__subject___name__icontains=topic) | Q(shelve__bookshalf__name__icontains=topic)
            queryset = queryset.filter(topic_filter)

        if mime_type:
            queryset = queryset.filter(format_books__mime_type__iexact=mime_type)

        return queryset.order_by("-download_count")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_books = queryset.count()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "total_books": total_books,
            "books": serializer.data
        })

