from django.forms import IntegerField
from django.forms import Form
from django.views.generic import FormView


class Task302Form(Form):
    a = IntegerField(required=False)
    b = IntegerField(required=False)


class IndexView(FormView):
    form_class = Task302Form
    success_url = "/tasks/302/"
    template_name = "task302/index.html"

    def form_valid(self, form):
        a_raw = form.cleaned_data.get("a", "")
        b_raw = form.cleaned_data.get("b", "")

        a = int(a_raw) if a_raw else 0
        b = int(b_raw) if b_raw else 0

        result = f"{a} плюс {b} равно {a + b}"

        self.request.session["task302result"] = result
        self.request.session["task302a"] = a_raw
        self.request.session["task302b"] = b_raw

        return super().form_valid(form)
