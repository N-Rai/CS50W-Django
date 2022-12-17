from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", max_value=10, min_value=1)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":            #check if the request method is POST
        form = NewTaskForm(request.POST)    #Set all the input data to a variable
        if form.is_valid():                 #chcek if all the form data is valid
            task = form.cleaned_data["task"]    # If so retrieve the task 
            request.session["tasks"] += [task]                # Add the task to the list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks.html", {"form": form})
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

