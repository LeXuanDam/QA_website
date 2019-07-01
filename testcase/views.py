from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_step': " Your test steps here:"}

    return render(request, 'testcase/index.html', context=my_dict)