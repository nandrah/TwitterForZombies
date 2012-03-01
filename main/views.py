from django.shortcuts import render_to_response
from django.template import RequestContext
from main.utils import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main.models import Zombie, Tweet
from main.forms import ZombieForm


def twitter(request):
    tweets = Tweet.objects.all()
    return render_to_response('twitter.html',
    {'tweets': tweets},
    RequestContext(request))


class ZombieMixin(object):
    model = Zombie
    success_url = reverse_lazy('zombies')
    form_class = ZombieForm


class ZombieListView(ZombieMixin, ListView):
    pass


class ZombieCreateView(ZombieMixin, CreateView):
    pass


class ZombieUpdateView(ZombieMixin, UpdateView):
    pass


class ZombieDeleteView(ZombieMixin, DeleteView):
    pass


list_zombies = ZombieListView.as_view()
create_zombie = ZombieCreateView.as_view()
update_zombie = ZombieUpdateView.as_view()
delete_zombie = ZombieDeleteView.as_view()
