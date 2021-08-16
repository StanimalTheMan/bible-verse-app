from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        """Save the request with the form"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)