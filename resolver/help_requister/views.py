from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class GreetingsPage(LoginRequiredMixin, TemplateView):
    template_name = 'greetings.html.j2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
