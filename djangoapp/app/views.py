#sfrom django.shortcuts import render

from django.http import HttpResponse
def home(request):
    html = "<html><body>Hello World!</br><p>Testing 1,2,3...</p></body></html>"
    return HttpResponse(html)