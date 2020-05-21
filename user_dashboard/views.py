
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
import numpy as np

# from .models import TestModel

# Create your views here.


@login_required
def dashboar_view(request, *args, **kwargs):
    # data = TestModel.objects.values_list('num', flat=True)
    # print(data)

    # plot_div = get_chart(list(data))
    plot_div = 'asd'
    return render(request, template_name='pages/dashboard.html', context={'plot_div': plot_div})


def get_chart(data):
    axis_x = np.linspace(1, 101, 100)
    axis_y = np.random.randn(100)

    # number of graphs
    trace0 = go.Scatter(x=data, y=data, mode='markers', name='scatter')
    trace1 = go.Scatter(x=axis_x, y=axis_y + 5, mode='lines', name='line')
    trace2 = go.Scatter(x=axis_x, y=axis_y - 5,
                        mode='lines+markers', name='scatter_line')

    # gathering data
    data = [trace0, trace1, trace2]

    # graph layour/styling
    layout = go.Layout(
        title='A Random Scatter Graph',
    )

    # making a figure consists => data, layout
    fig = go.Figure(data=data, layout=layout)

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
