
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import pandas as pd
from .models import Dashboard

from django_pandas.io import read_frame
from . import dashboard_plot_items
from .forms import UploadForm


# Dashboard Home View
# @login_required
def dashboar_view(request, *args, **kwargs):
    if request.method == "POST":
        uploaded_file = request.FILES.get('csv')
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                df = format_and_clean_data(df)
                try:
                    row_iter = df.iterrows()
                    objs = [
                        Dashboard(
                            user=request.user,
                            directorate=row['directorate'],
                            department=row['department'],
                            expenditure_type=row['expenditure_type'],
                            ref_doc_1=row['ref_doc_1'],
                            vendor_name=row['vendor_name'],
                            expenditure_amount=float(
                                row['expenditure_amount']),
                            payment_date=row['payment_date']
                        )
                        for index, row in row_iter
                    ]
                    Dashboard.objects.bulk_create(objs)
                    messages.success(
                        request, f'Successfully updatd the databese!')
                except:
                    messages.warning(
                        request, f'Error occured! Could not update the databas')
            except:
                messages.warning(
                    request, f'Failed! Please upload a valid CSV file')
        return redirect('dashboard')
    else:
        context = dict(in_dashboard='True')
        form = UploadForm()
        context['form'] = form
        # Loading Data from Django Model
        dashboard_items = Dashboard.objects.all()
        df = read_frame(dashboard_items)
        df = format_datetime(df)

        # Creatings Charts
        context['time_series'] = dashboard_plot_items.time_series(
            dataframe=df,
            x_title="Time Series",
            y_title="Sum of Expenditure"
        )  # expenditure timeseries

        context['bar_chart_yearly'] = dashboard_plot_items.yearly_expenditure_barchart(
            dataframe=df,
            x_title='Months',
            y_title="Sum of expenditure"
        )  # yearly expenditure bar chart

        context['bar_chart_group'] = dashboard_plot_items.plot_group_bar_chart(
            dataframe=df
        )

        context['pie_plot_dropdown'] = dashboard_plot_items.dropdown_pie(
            dataframe=df)  # dropdown pie chart

        context['pie_plot'] = dashboard_plot_items.plot_pei_chart(
            df)  # pie chart

        return render(request, template_name='pages/dashboard.html', context=context)


def format_datetime(data):
    # Converting payment date to pandas -> Datetime object & Creating 3 new Columns
    data['payment_date'] = pd.to_datetime(data['payment_date'])
    data['year'] = pd.DatetimeIndex(data['payment_date']).year
    data['month'] = pd.DatetimeIndex(data['payment_date']).month
    # Creating a new column with full month name
    data['month'] = data['payment_date'].map(lambda x: x.strftime('%B'))

    return data


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
    data['payment_date'] = pd.to_datetime(data['payment_date'])
    return data


# from user_dashboard.models import Dashboard
# Dashboard.objects.all().delete()
