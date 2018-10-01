from django import template
from django.template.defaultfilters import stringfilter
from django.shortcuts import HttpResponse
from django.contrib import messages
register = template.Library()

@register.filter(name='splitname')
@stringfilter
def splitname(string):
    name,value=string.split("==") 
    return name
   
@register.filter(name='splitvalue')
@stringfilter
def splitvalue(string):
    name,value=string.split("==") 
    return value

@register.filter(name='splittitle')
@stringfilter
def splittitle(string):
    title,content=string.split(":") 
    return title

@register.filter(name='splitcontent')
@stringfilter
def splitcontent(string):
    title,content=string.split(":") 
    return content

@register.filter('break')
def break_(loop):
    raise StopLoopException(loop, False)