from django import forms

class JobDataForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)  # Hidden input for the 'id' field
    jobTitle = forms.CharField(label='Job Title', max_length=100)
    companyLocation = forms.CharField(label='Company Location', max_length=100)
    jobRequirement = forms.CharField(
        label='Job Requirement',
        widget=forms.Textarea(attrs={'rows': 5}),  # Use a Textarea for multiple lines
    )
    metadata = forms.CharField(
        label='Metadata',
        widget=forms.Textarea(attrs={'rows': 5}),  # Use a Textarea for multiple lines
    )
