#I have created this file--Fahad

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
    # return HttpResponse("Home")


def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
            punctuations='''!()-[]{};:'"\,<>./?#$@%&^*~`'''
            analyzed = ""
            for char in djtext:
                 if char not in punctuations:
                     analyzed = analyzed + char

            params = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}         
            return render(request,'analyze.html',params)

            # return HttpResponse("Remove punc")
    else:
         return HttpResponse("Error")
    