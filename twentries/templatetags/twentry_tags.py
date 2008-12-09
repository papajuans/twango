from django import template

def twentry(context, t):
    to_return = {
        'twentry': t
    }
    return to_return

register = template.Library()

register.inclusion_tag('twentries/twentry.html', takes_context=True)(twentry)
