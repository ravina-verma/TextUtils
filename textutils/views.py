# created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
 return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def analyze(request):
 #get text
 djtext=request.POST.get('text', 'No text entered')
 removepunc=request.POST.get('removepunc','off')
 capitalize=request.POST.get('capitalize','off')
 removespace=request.POST.get('removespace','off')
 newlineremover=request.POST.get('newlineremover','off')
 charcount=request.POST.get('charcount','off')
 #analyze text
 analyzed = ""
 purpose=""
 if removepunc=="on":
     punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     for char in djtext:
      if char not in punctuations:
       analyzed=analyzed+char
     djtext=analyzed
     purpose+="| Removed Punctuations "
     params = {'purpose': purpose, 'analyzed_text': analyzed}
 if capitalize=="on":
     analyzed=""
     for char in djtext:
         analyzed=analyzed+ char.upper()
     djtext=analyzed
     purpose+="| Capitalize "
     params = {'purpose': purpose, 'analyzed_text': analyzed}
 if removespace=="on":
    analyzed=""
    s=""
    for char in djtext:
        if char==' ':
            if len(s)!=0:
                analyzed=analyzed+s+' '
                s=""
        else:
            s=s+char
    if len(s) != 0:
        analyzed = analyzed + s
    djtext=analyzed
    purpose+="| Removed Extra space "
    params = {'purpose':purpose, 'analyzed_text': analyzed}
 if newlineremover=="on":
     analyzed=""
     for char in djtext:
         if char !='\n' and char!='\r':
             analyzed+=char
     djtext=analyzed
     purpose+='| Removed newline '
     params={'purpose': purpose ,'analyzed_text':analyzed}

 if charcount=="on":
     s=""
     cnt=0
     for i,char in enumerate(djtext):
         if djtext[i]!=' ':
             cnt+=1
     purpose+="| Char count "
     params={'purpose':purpose,'analyzed_text':analyzed, 'cnt':cnt}
 if newlineremover=="on" or charcount=="on" or removepunc=="on" or removespace=='on' or capitalize=='on':
     return render(request, 'analyze.html', params)
 return HttpResponse("<h1>You have not selected anything  betaa ji</h1>")




