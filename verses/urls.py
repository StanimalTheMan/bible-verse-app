from django.urls import path
from .views import VerseListView, VerseDetailView

urlpatterns = [
    path('<int:pk>/', VerseDetailView.as_view(), name='verse_detail'),
    path('', VerseListView.as_view(), name='verse_list'),
]