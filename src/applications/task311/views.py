from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task311.logic import solution


class Task311Form(Form):
    email = CharField(required=False)


class IndexView(FormView):
    form_class = Task311Form
    success_url = "/tasks/311/"
    template_name = "task311/index.html"

    def form_valid(self, form):
        email = form.cleaned_data.get("email", "")

        try:
            solution(email)
            result = email
        except ValueError as err:
            result = str(err)

        self.request.session["task311result"] = result
        self.request.session["task311email"] = email

        return super().form_valid(form)
