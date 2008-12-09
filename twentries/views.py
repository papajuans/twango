from models import Twentry
from django.shortcuts import render_to_response
from django.template import RequestContext
from twentries.forms import TwentryForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def public(request):
    form = TwentryForm()
    return render_to_response(
        'twentries/public.html',
        {
            'twentries': Twentry.objects.order_by('-date_posted'),
            'form': form,
            'user': request.user,
        },
        context_instance = RequestContext(request),
    )

@login_required
def create(request):
    form = TwentryForm(request.POST or None)
    if form.is_valid():
        twentry = form.save(commit=False)
        twentry.user = request.user
        twentry.save()
        request.user.message_set.create(message='Your twentry was posted')
        if 'next' in request.POST:
            next = request.POST['next']
        else:
            next = reverse('public_timeline')
        return HttpResponseRedirect(next)
    
    return HttpResponseRedirect('public_timeline')
        