import os.path

from django import template

register = template.Library()


@register.filter()
def mediapath(image):
    if image:
        return f'../../media/{image}'


@register.simple_tag()
def mediapath(image):
    if image:
        return f'../../media/{image}'
