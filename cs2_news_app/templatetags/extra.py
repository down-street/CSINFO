from django import template

register = template.Library()

@register.filter
def index_3(List, i):
    try:
        return List[int(i+3)]
    except:
        return None
    
@register.filter
def index(List, i):
    try:
        return List[int(i)]
    except:
        return None

@register.filter
def getkey(dictionary, i):
    print(dictionary)
    return getattr( dictionary,i)