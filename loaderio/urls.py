from django.conf.urls import url
from loaderio.views import show_token


urlpatterns = [
    url(r'^(?P<token>loaderio-[0-9a-z]+)(?:\.txt|\.html|/)?$',
        show_token)
]
