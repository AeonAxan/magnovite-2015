from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def selected(context, url):
    request = context['request']
    if request.path == url:
        return 'selected'
    else:
        return ''

@register.simple_tag(takes_context=True)
def selected_url(context, url, fragment=None):
    request = context['request']

    if request.path == url:
        return fragment or '#'
    else:
        return url
