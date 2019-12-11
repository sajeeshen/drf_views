from django.urls import path
from .views import BookList, BookUpdateView

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookUpdateView.as_view())
]