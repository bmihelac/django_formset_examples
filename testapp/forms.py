from django import forms

from models import ShirtColorPrice, Color


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
        Return 1 for fieldname DELETION_FIELD_NAME if object does not have price.
        """
        if fieldname == DELETION_FIELD_NAME:
            return "1" if not self._raw_value('price') else ""
        return super(ShirtColorPriceModelForm, self)._raw_value(fieldname)
    
    
    class Meta:
        model = ShirtColorPrice
        # NOTE: there is bug in Django 1.2 that would not allow setting widgets
        # http://code.djangoproject.com/ticket/13095
        widgets = {
            # 'shirt': forms.widgets.HiddenInput(),
            # 'color': forms.widgets.HiddenInput(),
        }

class ShirtColorPriceModelFormset(forms.models.BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        self.total_related_objects_num = Color.objects.count()
        if kwargs.get('instance'):
            self._initial_form_count = kwargs['instance'].shirtcolorprice_set.count()
            self.extra = self.total_related_objects_num - self._initial_form_count
        else:
            self.initial_form_count = 0
            self.extra = self.total_related_objects_num
        super(ShirtColorPriceModelFormset, self).__init__(*args, **kwargs)
        self.max_num =  self.total_related_objects_num
        
    def get_related_queryset(self):
        return Color.objects.all()
    
    def initial_form_count(self):
        return self._initial_form_count

    def _get_initial_forms(self):
        return [f for form in self.forms if f.instance]

    def _get_extra_forms(self):
        return [f for form in self.forms if not f.instance]
        
    def _construct_form(self, i, **kwargs):
        related_object = self.get_related_queryset()[i]
        try:
            instance = self.get_queryset().get(color=related_object)
        except ShirtColorPrice.DoesNotExist, e:
            instance = None
        kwargs['initial'] = {'color': related_object.id}
        kwargs['instance'] = instance
        form = forms.formsets.BaseFormSet._construct_form(self, i, **kwargs)
        setattr(form.instance, self.fk.get_attname(), self.instance.pk)
        return form
        
    