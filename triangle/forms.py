from django import forms


class TriangleForm(forms.Form):
    leg1 = forms.DecimalField()
    leg2 = forms.DecimalField()

    def clean_leg1(self):
        leg1 = self.cleaned_data.get('leg1')
        if leg1 <= 0:
            raise forms.ValidationError("Больше нуля пж")
        else:
            return leg1

    def clean_leg2(self):
        leg2 = self.cleaned_data.get('leg2')
        if leg2 <= 0:
            raise forms.ValidationError("Больше нуля пж")
        else:
            return leg2
