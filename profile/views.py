from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from socialgraph.util import get_people_user_follows, get_people_following_user
from socialgraph.util import get_mutual_followers

def detail(request, username=None):
    """
    Renders information about a single user's profile.  This includes
    information about who follows them, who they follow, mutual followers, the
    latest events created, and whether the currently logged in user is a friend
    of the user to render.
    """
    user = get_object_or_404(User, username=username)
    people_following_user = get_people_following_user(user)
    context = {
        'profile_user': user,
        'people_following_user': people_following_user,
        'people_user_follows': get_people_user_follows(user),
        'mutual_followers': get_mutual_followers(user),
        'friend': request.user in people_following_user,
    }
    return render_to_response(
        'profile/detail.html',
        context,
        context_instance = RequestContext(request)
    )
    