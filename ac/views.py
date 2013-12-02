from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from ac.models import AakashCenter, Coordinator

def index(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)


def about(request):
    """Index page.

    Arguments:
    - `Request`:
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('about.html', context_dict, context)    


def all_ac(request):
    context = RequestContext(request)
    aakashcenters = AakashCenter.objects.all()
    coordinators = Coordinator.objects.all()
    
    context_dict = {'aakashcenters': aakashcenters,
                    'coordinators': coordinators}

    return render_to_response('ac/all_ac.html', context_dict, context)

def get_ac_name_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(name__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()

    # if max_results > 0:
    #     if len(code_list) > max_results:
    #         code_list = code_list[:max_results]

    return lst

def get_ac_id_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(ac_id__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst


def get_ac_city_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(city__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst


def get_ac_state_list(max_results=0, starts_with=''):
    if starts_with:
        lst = AakashCenter.objects.filter(state__contains=starts_with)
    else:
        lst = AakashCenter.objects.all()
    return lst    

def suggest_ac_id(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_id']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_id']

    ac_id_list = get_ac_id_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_id_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)


def suggest_ac_name(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_name']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_name']

    ac_name_list = get_ac_name_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_name_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)
    
def suggest_ac_city(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_city']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_city']

    ac_city_list = get_ac_city_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_city_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)

def suggest_ac_state(request):
    context = RequestContext(request)
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggest_ac_state']
        print "GET: suggestion"
        print starts_with
    else:
        print "POST: suggestion"
        starts_with = request.POST['suggest_ac_state']

    ac_state_list = get_ac_state_list(10, starts_with)
    
    context_dict = {'aakashcenters': ac_state_list}

    return render_to_response('ac/ac_list.html',
                              context_dict, context)

def ac(request, id):
    context = RequestContext(request)
    aakashcenter = AakashCenter.objects.get(pk=id)
    print aakashcenter.ac_id
    coordinator_id = aakashcenter.coordinator.id
    print coordinator_id
    coordinator = Coordinator.objects.filter(user_id=coordinator_id)
    
    for c in coordinator:
        print c.user.username
    context_dict = {'aakashcenter': aakashcenter,
                    'coordinator': coordinator}
    return render_to_response('ac/ac.html', context_dict, context)
