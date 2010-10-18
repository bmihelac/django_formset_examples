from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminFormSet, InlineAdminForm

from models import *
from forms import ShirtColorPriceModelFormset, ShirtColorPriceModelForm


def _patched_inline_admin_formset_iter(self):
    for form in self.formset.forms:
        instance = form.instance
        yield InlineAdminForm(self.formset, form, self.fieldsets,
            self.opts.prepopulated_fields, instance, self.readonly_fields,
            model_admin=self.model_admin)
    yield InlineAdminForm(self.formset, self.formset.empty_form,
        self.fieldsets, self.opts.prepopulated_fields, None,
        self.readonly_fields, model_admin=self.model_admin)
InlineAdminFormSet.__iter__ = _patched_inline_admin_formset_iter

class ColorAdmin(admin.ModelAdmin):
    pass


class ShirtColorPriceInline(admin.TabularInline):
    model = ShirtColorPrice
    formset = ShirtColorPriceModelFormset
    form = ShirtColorPriceModelForm
    template = "admin/edit_inline/tabular_all.html"


class ShirtAdmin(admin.ModelAdmin):
    inlines = [ShirtColorPriceInline]


admin.site.register(Color, ColorAdmin)
admin.site.register(Shirt, ShirtAdmin)