from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from feedback.forms import FeedbackForm
from time import sleep

# Create your views here.
def index(request):

    if request.method == "GET":
        form = FeedbackForm()
        
    else:

        form = FeedbackForm(request.POST)

        if form.is_valid():
            sleep(30)
            return HttpResponseRedirect("success")

    return render(request, "feedback/index.html", 
                  {
                      "form": form
                  }) 


         
def success(request):

    if request.method == "GET":
        return render(request, "feedback/success.html")
