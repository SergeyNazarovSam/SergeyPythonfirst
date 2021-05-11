from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task309.logic import solution
from applications.task309.logic import CoefficientsT


class Task309Form(Form):
    a = CharField(required=False)
    b = CharField(required=False)
    c = CharField(required=False)
    can_into_complex = CharField(required=False)


class IndexView(FormView):
    form_class = Task309Form
    success_url = "/tasks/309/"
    template_name = "task309/index.html"

    def form_valid(self, form):
        a_raw = form.cleaned_data.get("a", "") or ""
        b_raw = form.cleaned_data.get("b", "") or ""
        c_raw = form.cleaned_data.get("c", "") or ""
        can_into_complex = bool(form.cleaned_data.get("can_into_complex"))

        coefficients = CoefficientsT(a=a_raw, b=b_raw, c=c_raw)

        try:
            result = solution(coefficients, can_into_complex)
        except ValueError as err:
            result = f"нет решений ({err})"

        self.request.session["task309result"] = result
        self.request.session["task309a"] = a_raw
        self.request.session["task309b"] = b_raw
        self.request.session["task309c"] = c_raw
        self.request.session["task309can_into_complex"] = can_into_complex

        return super().form_valid(form)
