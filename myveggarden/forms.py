from django import forms
from .models import Garden, GardenSet
from django.views.generic import DetailView

class GardenSetForm(forms.ModelForm):
    class Meta:
        OTHER = 'Other'
        model = GardenSet
        fields = [
            "concentration_set",
            "next_cycle_set",
            "cycle_time_set",
            "plant_pump_set",
            "recirculation_pump_set",
            "solution_pump_set",
        ]
        widgets = {
            "concentration_set": forms.NumberInput(attrs={'class': 'form-control ppap-form-field', 'min': 0}),
            "next_cycle_set": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "cycle_time_set": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "plant_pump_set": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "recirculation_pump_set": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "solution_pump_set": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }


class GardenForm(forms.ModelForm):
    class Meta:
        OTHER = 'Other'
        model = Garden
        fields = [
            "concentration",
            "luminosity",
            "temperature",
         #   "next_cycle",
         #   "cycle_time",
            "plant_pump",
            "recirculation_pump",
            "solution_pump",
        ]
        widgets = {
            "concentration": forms.NumberInput(attrs={'class': 'form-control ppap-form-field', 'min': 0}),
            "luminosity": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "temperature": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
         #   "next_cycle": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
         #   "cycle_time": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "plant_pump": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "recirculation_pump": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "solution_pump": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }


class YourDetailView(DetailView):
    context_object_name = "certific"
    model = Garden

    def get_context_data(self, **kwargs):
        """This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(YourDetailView, self).get_context_data(**kwargs)
        context["car"] = Car.objects.get(registration="DK52 WLG")
        return context

#Alterar "car" para Certification ou RequiredDocuments e mudar em URLS para YourDetailView, como descrito no link abaixo.
#link onde retirei informações acima: http://stackoverflow.com/questions/14936160/django-detailview-how-to-display-two-models-at-same-time

class TestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

