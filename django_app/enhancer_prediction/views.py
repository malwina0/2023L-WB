from django.shortcuts import render
from plot_example import get_plot
from django.http import HttpResponse
from django.conf import  settings
import pandas as pd
import csv
import os

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


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dane.csv"'

    base_dir = settings.BASE_DIR
    df = pd.read_csv(os.path.join(base_dir, 'Percentage.csv'))
    for i in range(len(df)):
        df['list of percentages'].iloc[i] = eval(df['list of percentages'].iloc[i])
    max_len = max([len(list_p) for list_p in df['list of percentages'].to_list()])

    header = ['chromosome']
    for i in range(max_len):
        text = str(1700 * i + 1) + '-' + str(1700 * (i + 1))
        header.append(text)

    data = []
    for row in range(len(df)):
        data.append([df['chromosome'].iloc[row]])
        data[row].extend(df['list of percentages'].iloc[row])

    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(data)

    return response

