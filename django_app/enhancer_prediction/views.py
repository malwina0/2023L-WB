from django.shortcuts import render
from plot_example import get_plot

def about(request):
    context = {
        "title": "enhancer prediction"
    }
    return render(request, 'about.html', context)


def methods(request):
    context = {
        "title": "methods"
    }
    return render(request, 'methods.html', context)


def enhancer_classification(request):
    if request.method == 'POST':
        chromosome = request.POST.get('chromosome')
        start_range = request.POST.get('start_range')
        end_range = request.POST.get('end_range')

        plot_div = get_plot(chromosome, start_range, end_range)
        return render(request, 'classifier.html', {'plot_div': plot_div})

    return render(request, 'classifier.html')
