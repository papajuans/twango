from models import Twentry
from django.shortcuts import render_to_response
from django.template import RequestContext

def public(request):
    return render_to_response(
        'twentries/public.html',
        {'twentries': Twentry.objects.order_by('-date_posted')},
        context_instance = RequestContext(request),
    )
