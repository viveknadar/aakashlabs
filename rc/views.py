from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from rc.models import RemoteCenter, Coordinator

def index(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)


def all_rc(request):
    context = RequestContext(request)
    remotecenters = RemoteCenter.objects.all()
    coordinators = Coordinator.objects.all()
    
    context_dict = {'remotecenters': remotecenters,
                    'coordinators': coordinators}

    return render_to_response('rc/all_rc.html', context_dict, context)

def rc(request, id):
    context = RequestContext(request)
    remotecenter = RemoteCenter.objects.get(pk=id)
    print remotecenter.rc_id
    coordinator_id = remotecenter.coordinator.id
    print coordinator_id
    coordinator = Coordinator.objects.filter(user_id=coordinator_id)
    
    for c in coordinator:
        print c.user.username
    context_dict = {'remotecenter': remotecenter,
                    'coordinator': coordinator}
    return render_to_response('rc/rc.html', context_dict, context)
