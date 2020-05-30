
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Dashboard

from django_pandas.io import read_frame
from . import dashboard_plot_items


# Dashboard Home View
@login_required
def dashboar_view(request, *args, **kwargs):
    context = dict()
    # # temporarily getting the data from the data.csv file
    # df = pd.read_csv('data.csv')
    # df = format_and_clean_data(data=df)

    # Loading Data from Django Model
    dashboard_items = Dashboard.objects.all()
    df = read_frame(dashboard_items)
    print(df.head(3))
    # # Creatings Charts
    # context['pie_plot'] = dashboard_plot_items.plot_pei_chart(df)  # pie chart
    # context['pie_plot_dropdown'] = dashboard_plot_items.dropdown_pie(
    #     dataframe=df)  # dropdown pie chart
    # context['bar_chart_yearly'] = dashboard_plot_items.yearly_expenditure_barchart(
    #     dataframe=df)  # yearly expenditure bar chart
    # context['time_series'] = dashboard_plot_items.time_series(
    #     dataframe=df)  # expenditure timeseries

    return render(request, template_name='pages/dashboard.html', context=context)


def format_and_clean_data(data):
    # Renaming Columns
    data.columns = [
        'directorate',
        'department',
        'expenditure_type',
        'ref_doc_1',
        'vendor_name',
        'expenditure_amount',
        'payment_date']

    # Converting payment date to pandas -> Datetime object & Creating 3 new Columns
    data['payment_date'] = pd.to_datetime(data['payment_date'])
    data['year'] = pd.DatetimeIndex(data['payment_date']).year
    data['month'] = pd.DatetimeIndex(data['payment_date']).month
    # Creating a new column with full month name
    data['month'] = data['payment_date'].map(lambda x: x.strftime('%B'))

    return data
