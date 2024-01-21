from django import template

register = template.Library()

@register.filter()
def mymedia(val):
    if val:
        return f"/media/{val}"
    return f'static/no-image-500x500.jpg'

