from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np


# Will return the Summation of expenditure_amount of a given single Column
def get_sum_of_one_given_column(dataframe, col_name):
    col = dataframe[col_name].value_counts()
    data = pd.DataFrame()

    # *******************************************************
    # Here the logic goes to calculate the summation. Pandas data analysis will be required here
    # I have just given a simple logic for testing purpose
    for index, i in col.iteritems():
        temp_df = dataframe.loc[dataframe[col_name]
                                == index, ['expenditure_amount']].sum()
        cost = temp_df.expenditure_amount
        temp_series = pd.Series(
            {'col_name': index, 'sum_of_expenditure': cost})
        data = data.append(temp_series, ignore_index=True)

    # Has to return a pandas DataFrame object with 2 col -> col_name & sum_of_expenditure
    return data


def time_series(dataframe):
    data = get_sum_of_one_given_column(
        dataframe=dataframe, col_name='payment_date')

    fig = px.line(data, x='col_name', y='sum_of_expenditure',
                  title='Time Series of Expenditure Amount')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


# Plot bar chart you yearly expenditure
def yearly_expenditure_barchart(dataframe):
    # As there is only one year of data I am representing months as year for demo
    data = get_sum_of_one_given_column(dataframe=dataframe, col_name='month')
    fig = px.bar(data, y='sum_of_expenditure',
                 x='col_name', text='sum_of_expenditure')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


# Pie chart plot of the top 5 sum of expenditure of a given column
def plot_pei_chart(dataframe):
    dataframe = get_sum_of_one_given_column(dataframe, 'directorate')
    fig = px.pie(dataframe[:5], values='sum_of_expenditure',
                 names='col_name', title='')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


# Drop down Pie chart plot of the top 5 sum of expenditure of a given column
def dropdown_pie(dataframe):
    dropdown_option_1_data = get_sum_of_one_given_column(
        dataframe, 'directorate')
    dropdown_option_2_data = get_sum_of_one_given_column(
        dataframe, 'department')

    trace1 = go.Pie(labels=dropdown_option_1_data['col_name'],
                    values=dropdown_option_1_data['sum_of_expenditure'])
    trace2 = go.Pie(labels=dropdown_option_2_data['col_name'],
                    values=dropdown_option_2_data['sum_of_expenditure'])

    data = [trace1, trace2]
    fig = go.Figure(data)

    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="Select One",
                         method="restyle",
                         args=[{"visible": [False, False, False]},
                               {"title": "All Expenditure Percentage",
                                "annotations": []}]),

                    dict(label="Directorate",
                         method="update",
                         args=[{"visible": [True, False, False]},
                               {"title": "Directorate wise Expenditure Percentage",
                                "annotations": []}]),

                    dict(label="Department",
                         method="update",
                         args=[{"visible": [False, True, False]},
                               {"title": "Department wise Expenditure Percentage",
                                "annotations": []}]),
                ]),
            )
        ])
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


if __name__ == "__main__":
    pass
