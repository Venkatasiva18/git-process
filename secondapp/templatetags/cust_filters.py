from django import template
register = template.Library()


@register.filter(name='f8upper')
def first_eight_upper(value):
    "This is my own filter "
    result = value[0:20].upper()
    return result


# @register.filter(name='c_and_c')
# def cut_and_concate(value,arg):
#     result = value[:4]+str(arg)
#     return result


register.filter("f8upper", first_eight_upper)

