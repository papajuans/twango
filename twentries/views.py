from models import Twentry
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from twentries.forms import TwentryForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def public(request):
    """
    Render the latest from all public twentries.
    """
    return render_to_response(
        'twentries/public.html',
        {
            'twentries': Twentry.objects.order_by('-date_posted'),
        },
        context_instance = RequestContext(request),
    )
    
def user(request, username=None):
    """
    Render the twentries of a specific entry.
    """
    user = get_object_or_404(User, username=username)
    return render_to_response(
        'twentries/user.html',
        {
            'twentries': Twentry.objects.filter(user=user).order_by('-date_posted'),
            'the_user':user,
        },
        context_instance = RequestContext(request),
    )

@login_required
def create(request):
    """
    Create a twentry (handles form post)
    """
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
    
    return HttpResponseRedirect(reverse('public_timeline'))
        