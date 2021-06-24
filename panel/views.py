from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from shortner.models import	Url


class PanelTemplateView(LoginRequiredMixin, TemplateView):
	template_name = 'list.html'

def logout_view(request):
    logout(request)
    return redirect('/admin/login/?next=/panel/')
	