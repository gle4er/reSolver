from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

from help_requister.models import Problem


class GreetingsPage(TemplateView):
    template_name = 'greetings.html.j2'


class ProblemForm(LoginRequiredMixin, CreateView):
    model = Problem
    fields = ['title', 'category', 'description']
    template_name = 'problem_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
