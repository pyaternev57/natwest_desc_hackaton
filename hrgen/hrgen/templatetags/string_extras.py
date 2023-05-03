from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter()
@stringfilter
def split_long(value):
    return "/r".join([value[i : i + 30] for i in range(0, len(value), 30)])
