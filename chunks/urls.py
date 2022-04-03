from django.urls import re_path


urlpatterns = [
    re_path('^edit/(?P<key>\w+)/$', 'edit_view', name='edit'),
]
