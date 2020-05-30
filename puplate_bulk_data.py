import pandas as pd
from user_dashboard.models import Dashboard


def format_and_clean_data(data):
    # Renaming Columns
    data.columns = [
        'idd'
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


df = pd.read_csv('data.csv')
df = format_and_clean_data(df)
print(df.head(3))
row_iter = df.iterrows()

objs = [
    Dashboard(
        directorate=row['directorate'],
        department=row['department'],
        expenditure_type=row['expenditure_type'],
        ref_doc_1=row['ref_doc_1'],
        vendor_name=row['vendor_name'],
        expenditure_amount=float(row['expenditure_amount']),
        payment_date=row['payment_date']
    )
    for index, row in row_iter
]

Dashboard.objects.bulk_create(objs)
