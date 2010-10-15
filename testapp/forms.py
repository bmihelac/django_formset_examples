from django import forms


class ShirtColorPriceForm(forms.Form):
    shirt_id = forms.CharField()
    color = forms.CharField()
    price = forms.DecimalField()
    
class ShirtColorPriceForm2(forms.Form):
    shirt_id = forms.CharField()
    color = forms.CharField()
    price = forms.DecimalField(required=False)
