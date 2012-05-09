from django.shortcuts import render_to_response

def articles(request,id=0):
    context = {}
    render_to_response('articles.html', context)
