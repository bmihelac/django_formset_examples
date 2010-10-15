from django import forms

from models import ShirtColorPrice


DELETION_FIELD_NAME = forms.formsets.DELETION_FIELD_NAME


class ShirtColorPriceForm(forms.Form):
    shirt_id = forms.CharField()
    color = forms.CharField()
    price = forms.DecimalField()
    

class ShirtColorPriceForm2(forms.Form):
    shirt_id = forms.CharField()
    color = forms.CharField()
    price = forms.DecimalField(required=False)


class ShirtColorPriceModelForm(forms.ModelForm):
    price = forms.DecimalField(required=False)
    
    def _raw_value(self, fieldname):
        """
        Return 1 for fieldname DELETION_FIELD_NAME if object do not have price.
        """
        if fieldname == DELETION_FIELD_NAME:
            return "1" if not self._raw_value('price') else ""
        return super(ShirtColorPriceModelForm, self)._raw_value(fieldname)
    
    
    class Meta:
        model = ShirtColorPrice
        # NOTE: there is bug in Django 1.2 that would not allow setting widgets
        # http://code.djangoproject.com/ticket/13095
        widgets = {
            'shirt': forms.widgets.HiddenInput(),
            'color': forms.widgets.HiddenInput(),
        }

class ShirtColorPriceModelFormset(forms.models.BaseModelFormSet):
    """
    extra_forms = 0
    """
    pass
    