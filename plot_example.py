import numpy as np
import plotly.graph_objects as go
import nbformat
import math
import pandas as pd
import plotly.offline as opy
import csv

def get_plot(chromosome, start_range, end_range):
    df = pd.read_csv('Percentage.csv')

    def read_list(row):
        str = df.at[row, 'list of percentages'][1:-1]
        l = [float(x) for x in str.split(", ")]
        return l

    lens = [146619,143059, 116484, 112444, 106421, 100656, 93611, 86097, 83067, 79727, 79416, 78737, 67747, 63147, 60313, 53150, 47762, 45928, 34782, 37074, 28312, 30180]

    def get_ids_for_list(len):
        return [i for i in range(len)]

    chr = int(chromosome[3:])
    start = int(start_range)
    end = int(end_range)
    st = math.floor(start / 1700)
    en = math.ceil(end / 1700)

    tickvals = get_ids_for_list(lens[chr - 1])[st:en + 1]
    ticktext = [val * 1700 for val in tickvals]
    tickvals_modified = []
    ticktext_modified = []
    if len(tickvals) // 10 != 0:
        for i, val in enumerate(tickvals):
            if i == 0 or i == len(tickvals) - 1 or i % (len(tickvals) // 10) == 0:
                tickvals_modified.append(val)
                ticktext_modified.append(ticktext[i])
    else:
        tickvals_modified = tickvals
        ticktext_modified = ticktext

    fig = go.Figure(data=go.Bar(x=get_ids_for_list(lens[chr-1])[st:en + 1], y=read_list(chr - 1)[st:en + 1],
                                marker=dict(color=read_list(chr - 1)[st:en + 1], colorscale='BuPu', reversescale=True),
                                hovertemplate = '%{y}%<br>'
                                ))

    fig.update_layout(
        title={
            'text': f'Percentage of probability that a given segment of nucleotides is an enhancer',
            'x': 0.5,
            'font': {'color': 'white'}
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(color='white'),
            title=dict(text='Nukleotides', font=dict(color='white')),
            showgrid=False,
            tickmode='array',
            tickvals=tickvals_modified,
            ticktext=ticktext_modified),
        yaxis=dict(
            tickfont=dict(color='white'),
            title=dict(text='Percentage', font=dict(color='white')),
            showgrid=False)
    )
    fig.update_traces(marker=dict(line=dict(color='rgba(0,0,0,0)')))
    fig.update_yaxes(range=[0, 100])

    plot_div = opy.plot(fig, auto_open=False, output_type='div')
    return plot_div