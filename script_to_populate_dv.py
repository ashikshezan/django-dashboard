import pandas as pd
from user_dashboard.models import Dashboard


def add_data(row):
    flag, created = Dashboard.objects.get_or_create(
        # user=row['user'],
        directorate=row['directorate'],
        department=row['department'],
        expenditure_type=row['expenditure_type'],
        ref_doc_1=row['ref_doc_1'],
        vendor_name=row['vendor_name'],
        expenditure_Amount=row['expenditure_Amount']
    )
    print("- Data: {0}, Created: {1}".format(str(flag), str(created)))
    return flag


def populate(data):
    # data is a list of lists
    for index, row in data.iterrows():
        add_data(row)


df = pd.read_csv('data.csv')
df.columns = ['user',
              'directorate',
              'department',
              'expenditure_type',
              'ref_doc_1',
              'vendor_name',
              'expenditure_Amount']
populate(df)
