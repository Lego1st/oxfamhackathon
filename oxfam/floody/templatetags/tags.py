from django import template
from ..models import *
register = template.Library()


@register.simple_tag
def get_points(request):
    return Post.objects.all()

register.tag('get_points', get_points)