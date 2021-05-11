from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView


class Task301Form(Form):
    name = CharField(required=False)


class IndexView(FormView):
    form_class = Task301Form
    success_url = "/tasks/301/"
    template_name = "task301/index.html"

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        result = name if name else "anonymous"

        self.request.session["task301greeting_name"] = result
        self.request.session["task303input_name"] = name

        return super().form_valid(form)
