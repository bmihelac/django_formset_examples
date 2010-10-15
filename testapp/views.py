from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.formsets import formset_factory

from forms import ShirtColorPriceForm, ShirtColorPriceForm2


def example1(request, **kwargs):
    ctx = RequestContext(request)
    ShirtColorPriceFormset = formset_factory(ShirtColorPriceForm, extra=3)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        formset = ShirtColorPriceFormset()
    ctx['formset'] = formset
    return render_to_response('example1.html', ctx)

def example2(request, **kwargs):
    ctx = RequestContext(request)
    ShirtColorPriceFormset = formset_factory(ShirtColorPriceForm, extra=0)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        formset = ShirtColorPriceFormset(initial=[
            {'shirt_id': 1, 'color': 'red'},
            {'shirt_id': 2, 'color': 'blue'},
        ])
    ctx['formset'] = formset
    return render_to_response('example2.html', ctx)
    
def example3(request, **kwargs):
    ctx = RequestContext(request)
    ShirtColorPriceFormset = formset_factory(ShirtColorPriceForm2, extra=0)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        formset = ShirtColorPriceFormset(initial=[
            {'shirt_id': 1, 'color': 'red'},
            {'shirt_id': 2, 'color': 'blue'},
        ])
    ctx['formset'] = formset
    return render_to_response('example3.html', ctx)    