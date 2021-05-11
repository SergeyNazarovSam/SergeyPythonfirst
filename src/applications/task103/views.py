from django.forms import IntegerField
from django.forms import Form
from django.views.generic import FormView


class Task103Form(Form):
    age1 = IntegerField(required=False)
    age2 = IntegerField(required=False)
    age3 = IntegerField(required=False)


class IndexView(FormView):
    form_class = Task103Form
    success_url = "/tasks/103/"
    template_name = "task103/index.html"

    def form_valid(self, form):
        age1 = int(form.cleaned_data.get("age1", "0") or 0)
        age2 = int(form.cleaned_data.get("age2", "0") or 0)
        age3 = int(form.cleaned_data.get("age3", "0") or 0)
        ages = (age1, age2, age3)
        age_sum = sum(ages)
        age_avg = age_sum / len(ages)

        self.request.session["task103age1"] = age1
        self.request.session["task103age2"] = age2
        self.request.session["task103age3"] = age3
        self.request.session["task103age_sum"] = age_sum
        self.request.session["task103age_avg"] = age_avg
        self.request.session["task103ages"] = ages

        return super().form_valid(form)
