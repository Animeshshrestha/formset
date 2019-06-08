from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, Http404 
from django.utils import timezone

from .models import Post
from .forms import TestForm, PostModelForm


def formset_view(request):
        PostModelFormset = modelformset_factory(Post, form=PostModelForm)
        formset = PostModelFormset(request.POST or None, 
                queryset=None)
        if formset.is_valid():
            
            for form in formset:
                print(form.cleaned_data)

                obj = form.save(commit=False)
                if form.cleaned_data:
                    if not form.cleaned_data.get("publish"):
                        obj.publish = timezone.now()
                    obj.save()
        context = {
            "formset": formset
        }
        print(formset.errors)
        errors_dict = {'%s-%s-%s' % (formset.prefix, index, k): v for (index, errors) in enumerate(formset.errors) for k,v in errors.items()}
        print(errors_dict)
        return render(request, "formset_view.html", context)
 
