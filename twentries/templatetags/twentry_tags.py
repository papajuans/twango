from django import template
from twentries.forms import TwentryForm

def twentry(twentry):
    to_return = {
        'twentry': twentry
    }
    return to_return

def twentry_list(context, twentries):
    to_return = {
        'twentries':twentries,
        'request': context['request'],
    }
    return to_return

def twentry_form(context):
    to_return = {
        'form':  TwentryForm(),
        'user':context['user'],
    }
    return to_return

register = template.Library()
register.inclusion_tag('twentries/twentry.html')(twentry)
register.inclusion_tag('twentries/twentry_list.html', takes_context=True)(twentry_list)
register.inclusion_tag('twentries/form.html', takes_context=True)(twentry_form)