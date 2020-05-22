from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np


# A random Chart
def get_chart():
    axis_x = np.linspace(1, 101, 100)
    axis_y = np.random.randn(100)
    # number of graphs
    trace1 = go.Scatter(x=axis_x, y=axis_y + 5, mode='lines', name='line')
    trace2 = go.Scatter(x=axis_x, y=axis_y - 5,
                        mode='lines+markers', name='scatter_line')

    # gathering data
    data = [trace1, trace2]

    # graph layour/styling
    layout = go.Layout(
        title='A Random Scatter Graph',
    )
    # making a figure consists => data, layout
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def get_top_amounts(df, col_name):
    col = df[col_name].value_counts()
    data = pd.DataFrame()
    for index, i in col.iteritems():
        temp_df = df.loc[df[col_name] == index, ['expenditure_amount']].sum()
        cost = temp_df.expenditure_amount
        temp_series = pd.Series({'name': index, 'cost': cost})
        data = data.append(temp_series, ignore_index=True)
    return data


def plot_pei_chart(data):
    fig = px.pie(data[:5], values='cost', names='name', title='')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plot_bar_chart(data, xlabel='', ylabel=''):
    trace0 = go.Bar(x=data['name'], y=data['cost'])
    data = [trace0]

    # Style layout
    layout = go.Layout(
        title='',
        xaxis=dict(
            title=xlabel,
            # showticklabels=True,
            type='category',
        ),
        yaxis=dict(
            title=ylabel,
            #             type='category'
        ),
        margin=dict(t=0, b=0, l=0, r=0)
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(barmode='group', xaxis_tickangle=-50)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
