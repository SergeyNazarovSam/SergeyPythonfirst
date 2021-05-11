from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task303.logic import solution


class Task303Form(Form):
    sentence = CharField(required=False)


class IndexView(FormView):
    form_class = Task303Form
    success_url = "/tasks/303/"
    template_name = "task303/index.html"

    def form_valid(self, form):
        sentence = form.cleaned_data.get("sentence")
        result = solution(sentence) if sentence else ""

        self.request.session["task303result"] = result
        self.request.session["task303sentence"] = sentence

        return super().form_valid(form)
