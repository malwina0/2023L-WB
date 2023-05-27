from django.shortcuts import render


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
    context = {
        "title": "enhancer-classification"
    }
    return render(request, 'classifier.html', context)
