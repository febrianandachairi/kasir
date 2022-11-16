from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'title' : 'Ini halaman Index'
    }
    return render(request, template_name, context)
def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'Ini halaman About'
    }
    return render(request, template_name, context)