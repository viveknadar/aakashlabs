from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)
