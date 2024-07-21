from django.shortcuts import render

from django.http import HttpResponse
#here to make the combination of python server as well as using html there is dictnary system which is {} let's try
def html(request):
    return render(request,'hello_html.html',{'name':'this is from python using dictionary'})#we also need to change this in the html file as 
#this server or the working is redirected to the html file hence we will use html and dictionary