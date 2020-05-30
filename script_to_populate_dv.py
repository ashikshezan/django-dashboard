import pandas as pd
from user_dashboard.models import Dashboard
from user_dashboard.views import format_and_clean_data


@transaction.commit_manually
def populate(data):
    # data is a list of lists
    for index, row in data.iterrows():
        entry = Dashboard(
            # user=row['user'],
            directorate=row['directorate'],
            department=row['department'],
            expenditure_type=row['expenditure_type'],
            ref_doc_1=int(row['ref_doc_1']),
            vendor_name=row['vendor_name'],
            expenditure_amount=float(row['expenditure_amount']),
            payment_date=row['payment_date']
        )
        entry.save()

    transaction.commit()


df = pd.read_csv('data.csv')
df = format_and_clean_data(df)
print(df.head(3))
populate(df)


# def add_data(row):
#     flag, created = Dashboard.objects.get_or_create(
#         # user=row['user'],
#         directorate=row['directorate'],
#         department=row['department'],
#         expenditure_type=row['expenditure_type'],
#         ref_doc_1=int(row['ref_doc_1']),
#         vendor_name=row['vendor_name'],
#         expenditure_amount=float(row['expenditure_amount']),
#         payment_date=row['payment_date']
#     )
#     print("- Data: {0}, Created: {1}".format(str(flag), str(created)))
#     return flag
