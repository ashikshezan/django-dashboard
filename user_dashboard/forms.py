import os
from django import forms


class UploadForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    csv = forms.FileField()

    # def validate(self, value):
    #     # First run the parent class' validation routine
    #     super().validate(value)
    #     # Run our own file extension check
    #     file_extension = os.path.splitext(value.name)[1]
    #     if file_extension != '.csv':
    #         raise forms.ValidationError(
    #             ('Invalid file extension'),
    #             code='invalid'
    #         )
