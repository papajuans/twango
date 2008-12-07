from models import Entry
from django.shortcuts import render_to_response
from django.template import RequestContext

def public(request):
    return render_to_response('entries/public.html',
        {'entries': Entry.objects.order_by('-date_posted')},
        context_instance = RequestContext(request))
