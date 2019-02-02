from django.views import generic

from .models import Demo

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'demo_list'

    def get_queryset(self):
        return Demo.objects.all().order_by('id')
