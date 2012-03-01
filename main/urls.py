from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'twitter', name='twitter'),
    url(r'^zombies/?$', 'list_zombies', name='zombies'),
    url(r'^zombies/add/?$', 'create_zombie', name='add_zombie'),
    url(r'^zombies/(?P<pk>\d+)/edit/?$', 'update_zombie', name='update_zombie'),
    url(r'^zombies/(?P<pk>\d+)/delete/?$', 'delete_zombie', name='delete_zombie'),
    url(r'^zombie/(?P<pk>\d+)/tweets/?$', 'zombie_tweets', name='zombie_tweets'),
)
