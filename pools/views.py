from django.shortcuts import render

# Create your views here.

from django.views import generic

from pools.models import Questions


class IndexView(generic.ListView):
    template_name = 'pools/index.html'
    context_object_name = 'lastest_posts_text'

    def get_queryset(self):
        return Questions.objects.order_by('pub_date')
