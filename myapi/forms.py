from django import forms

class ApprovalForm(forms.Form):
    firstname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    lastname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter Lastname'}))
    Dependants=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Number of Dependants'}))
    ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Monthly Gross Income'}))
    CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Co-Applicant Monthly Gross Income'}))
    LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Requested Loan Ammount'}))
    Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Loan Term in Months'}))
    Credit_History=forms.ChoiceField(choices=[(1,1),(1,1),(2,2),(3,3)])
    Gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    Married=forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Education=forms.ChoiceField(choices=[('Graduate','Graduate'),('Not_Graduate','Not_Graduate')])
    Self_Employed=forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Property_Area=forms.ChoiceField(choices=[('Rural','Rural'),('Semi-urban','semi-urban'),('urban','urban')])
    
