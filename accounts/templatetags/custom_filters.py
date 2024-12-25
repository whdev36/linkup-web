from django import template

register = template.Library()

@register.filter
def getattr(obj, attr):
    try:
        return getattr(obj, attr, None)
    except AttributeError:
        return None
