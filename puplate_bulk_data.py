import pandas as pd
from user_dashboard.models import Dashboard
from user_dashboard.views import format_and_clean_data


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
