from django.urls import path, include
from .views import AuthorListView, AuthorActionView

urlpatterns = [ 
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>', AuthorActionView.as_view())
]