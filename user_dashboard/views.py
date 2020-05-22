
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Dashboard

from .custome_ploty_charts import get_chart, plot_pei_chart, get_top_amounts, plot_bar_chart
# Create your views here.


@login_required
def dashboar_view(request, *args, **kwargs):
    context = dict()
    # temporarily getting the data from the data.csv file
    df = pd.read_csv('data.csv')
    df = clean_data(df)

    # Plotting the barchart
    bar_data = get_top_amounts(df, 'month')
    context['bar_plot'] = plot_bar_chart(bar_data)

    # Plotting Pie chart
    pie_data = get_top_amounts(df, 'directorate')
    context['pie_plot'] = plot_pei_chart(pie_data)

    # Plotting Pie chart
    pie_data2 = get_top_amounts(df, 'department')
    context['pie_plot2'] = plot_pei_chart(pie_data2)

    return render(request, template_name='pages/dashboard.html', context=context)


def clean_data(df):
    df.columns = [
        'directorate',
        'department',
        'expenditure_type',
        'ref_doc_1',
        'vendor_name',
        'expenditure_amount',
        'payment_date']

    df['payment_date'] = pd.to_datetime(df['payment_date'])
    df['year'] = pd.DatetimeIndex(df['payment_date']).year
    df['month'] = pd.DatetimeIndex(df['payment_date']).month
    df['month'] = df['payment_date'].map(lambda x: x.strftime('%B'))
    return df
