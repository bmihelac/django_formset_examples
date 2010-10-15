from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from models import ShirtColorPrice, Shirt, Color
from forms import ShirtColorPriceForm, ShirtColorPriceForm2, ShirtColorPriceModelForm, \
                  ShirtColorPriceModelFormset


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
    
def example4(request, **kwargs):
    ctx = RequestContext(request)
    ShirtColorPriceFormset = modelformset_factory(ShirtColorPrice, extra=3)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        formset = ShirtColorPriceFormset()
    ctx['formset'] = formset
    return render_to_response('example4.html', ctx)
    
def example5(request, **kwargs):
    ctx = RequestContext(request)
    # NOTE: in example3 we set extra=0 and it created extra forms from initial array size
    extra_forms_num = Shirt.objects.count() * Color.objects.count()
    ShirtColorPriceFormset = modelformset_factory(ShirtColorPrice, extra=extra_forms_num)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        initial_data = []
        for shirt in Shirt.objects.all():
            for color in Color.objects.all():
                initial_data.append({
                    'shirt': shirt.id,
                    'color': color.id,
                })
        formset = ShirtColorPriceFormset(initial=initial_data)
    ctx['formset'] = formset
    return render_to_response('example5.html', ctx)    

def example6(request, **kwargs):
    ctx = RequestContext(request)
    existing_forms_num = ShirtColorPrice.objects.count()
    extra_forms_num = Shirt.objects.count() * Color.objects.count() - existing_forms_num
    ShirtColorPriceFormset = modelformset_factory(ShirtColorPrice, 
            form=ShirtColorPriceModelForm, 
            formset=ShirtColorPriceModelFormset,
            extra=extra_forms_num,
            can_delete=True)
    if request.method == 'POST':
        formset = ShirtColorPriceFormset(request.POST)
        if formset.is_valid():
            formset.save()
            ctx['cleaned_data'] = formset.cleaned_data
            return render_to_response('display_cleaned_data.html', ctx)
    else:
        initial_data = []
        for i in range(existing_forms_num):
            initial_data.append({})
        for shirt in Shirt.objects.all():
            for color in Color.objects.all():
                if not ShirtColorPrice.objects.filter(shirt=shirt, color=color):
                    initial_data.append({
                        'shirt': shirt.id,
                        'color': color.id,
                    })
        formset = ShirtColorPriceFormset(initial=initial_data)
    ctx['formset'] = formset
    return render_to_response('example6.html', ctx)    
    