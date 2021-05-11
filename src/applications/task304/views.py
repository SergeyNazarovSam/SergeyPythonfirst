from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task304.logic import solution


class Task304Form(Form):
    sentence = CharField(required=False)


class IndexView(FormView):
    form_class = Task304Form
    success_url = "/tasks/304/"
    template_name = "task304/index.html"

    def form_valid(self, form):
        sentence = form.cleaned_data.get("sentence")
        result = solution(sentence) if sentence else ""

        self.request.session["task304result"] = result
        self.request.session["task304sentence"] = sentence

        return super().form_valid(form)
