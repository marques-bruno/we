from django import template

register = template.Library()

# @register.filter
# def replace(value, arg):
#     """
#     Replacing filter
#     Use `{{ "aaa"|replace:"a|b" }}`
#     """
#     if len(arg.split('|')) != 2:
#         return value

#     what, to = arg.split('|')
#     return value.replace(what, to)

# @todo: this isn't the right way, let's find a better one
@register.filter
def replace_pk(value, arg):
    """
    Replacing filter
    Use `{{ value|replace:"arg" }}`
    """
    return value.replace("<int:pk>", str(arg))