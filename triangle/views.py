import math

from django.shortcuts import render

from triangle.forms import TriangleForm


def triangle(request):
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            gip = math.sqrt(form.cleaned_data['leg1'] ** 2 + form.cleaned_data['leg2'] ** 2)
            gip = gip if gip % 1 != 0 else int(gip)
            return render(request, 'index.html', {'gip':  gip})
    else:
        form = TriangleForm()
    return render(request, 'index.html', {'form': form})
