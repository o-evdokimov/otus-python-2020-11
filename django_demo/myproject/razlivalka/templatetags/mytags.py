from django import template

register = template.Library()

@register.filter(name='bold')
def bold(text):
    return f'<strong>{str(text)}</strong>'

