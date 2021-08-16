from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse 

from .models import Verse
from .forms import CommentForm

# Create your views here.
class VerseListView(ListView):
    model = Verse 
    template_name = 'verse_list.html'

class VerseDisplay(DetailView):
    model = Verse
    template_name = 'verse_detail.html'
    context_object_name = 'verse'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class VerseComment(LoginRequiredMixin,SingleObjectMixin, FormView):
    model = Verse
    form_class = CommentForm
    template_name = 'verse_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(VerseComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs 

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.verse = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        verse = self.get_object()
        return reverse('verse_detail', kwargs={'pk': verse.pk}) + '#comments'


class VerseDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        view = VerseDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = VerseComment.as_view()
        return view(request, *args, **kwargs)