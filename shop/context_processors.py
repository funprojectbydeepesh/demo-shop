
''' Context processor is simple interface . It's a python function which takes one argument and HttpRequest object , 
return dictionary that get added to templatecontent. ContextProcessor must return dictionary'''

from .models import Category

def get_category_link(request):
    links = Category.objects.all()
    return dict(links=links)
