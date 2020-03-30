from django import template

register = template.Library()


@register.filter
def hash_Phone(phone):
    for index,val in enumerate(phone):
        phone = phone.replace(val,'X')
    return phone
