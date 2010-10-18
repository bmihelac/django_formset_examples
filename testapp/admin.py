from django.contrib import admin

from models import *
from forms import ShirtColorPriceModelFormset, ShirtColorPriceModelForm


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