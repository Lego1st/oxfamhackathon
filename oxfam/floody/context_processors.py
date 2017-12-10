from models import *

def add_variable_to_context(request):
    return {
        'posts': [ p.location for p in Post.objects.all()]
    }
