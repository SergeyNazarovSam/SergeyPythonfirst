from applications.task306.logic import solution
from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView


class Task306Form(Form):
    age = CharField(required=False)


class IndexView(FormView):
    form_class = Task306Form
    success_url = "/tasks/306/"
    template_name = "task306/index.html"

    def form_valid(self, form):
        age_raw = form.cleaned_data.get("age")

        age = (
            None
            if (
                    not age_raw
                    or (isinstance(age_raw, str) and not age_raw.isnumeric())
            )
            else int(age_raw)
        )

        if age is not None:
            result = solution(age)
        else:
            result = None

        self.request.session["task306result"] = result
        self.request.session["task306age"] = age_raw

        return super().form_valid(form)
