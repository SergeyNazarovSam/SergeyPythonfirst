from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task310.logic import solution1, solution2, parse_decimal


class Task310Form(Form):
    money = CharField(required=False)


class IndexView(FormView):
    form_class = Task310Form
    success_url = "/tasks/310/"
    template_name = "task310/index.html"

    def form_valid(self, form):
        money_raw = form.cleaned_data.get("money", "")
        money = parse_decimal(money_raw)

        result1 = solution1(money)
        result2 = solution2(money)

        self.request.session["task310result1"] = result1
        self.request.session["task310result2"] = result2
        self.request.session["task310money"] = money_raw

        return super().form_valid(form)
