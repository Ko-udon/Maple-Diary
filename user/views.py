from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

def main(request):
  return render(request, 'main.html')


register = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'user/form.html',
    success_url = '/login/'
)

login = LoginView.as_view(
    template_name = 'user/form.html',
)

# logout = LogoutView.as_view(
#     next_page = '/accounts/login/'
# )

@login_required
def profile(request):
    return render(request, 'user/profile.html')
