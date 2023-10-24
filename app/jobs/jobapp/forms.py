from django import forms

#Form to edit that data for jobs
class JobDataForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)  # Hidden input for the 'id' field
    jobTitle = forms.CharField(label='Job Title', max_length=100)
    companyLocation = forms.CharField(label='Company Location', max_length=100)
    salary=forms.IntegerField(label='salary',max_value=10000000)

#Form for the input query box
class SearchForm(forms.Form):
    query = forms.CharField(label='Search',required=False, max_length=200)
