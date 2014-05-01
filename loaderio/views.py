from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from loaderio.models import Validation


def show_token(request, *args, **kwargs):
    validation = get_object_or_404(Validation,
                                   token=kwargs.get("token"),
                                   enabled=True)
    return HttpResponse(validation.token, content_type="text/plain")
