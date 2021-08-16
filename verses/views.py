from django.views.generic import ListView, DetailView
from .models import Verse

# Create your views here.
class VerseListView(ListView):
    model = Verse 
    template_name = 'verse_list.html'

class VerseDetailView(DetailView):
    model = Verse 
    template_name = 'verse_detail.html'