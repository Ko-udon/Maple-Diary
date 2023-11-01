from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, CreateView, DetailView
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserCharacter
from .forms import UserCharacterForm
from django.urls import reverse_lazy


def main(request):
    return render(request, 'main.html')


register = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'user/form.html',
    success_url = '/login/'
)



def success_register(request):
    return render(request, 'success_register.html')

login = LoginView.as_view(
    template_name = 'user/form.html',
)

logout = LogoutView.as_view(
    next_page = '/'
)

@login_required
def profile(request):
    return render(request, 'user/profile.html')

class ProfileDetailView(DetailView):
    model = UserCharacter
    template_name = 'user/profile_detail.html'
profile_detail = ProfileDetailView.as_view()


# 프로필 작성하기
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserCharacter
    form_class = UserCharacterForm
    success_url = reverse_lazy('user:profile')
    template_name = 'user/form.html'

    def form_valid(self, form):
        info = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        info.user_id = self.request.user
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.

profile_write = ProfileCreateView.as_view()

#프로필 수정하기
class ProfileEditView(UpdateView):
    model = UserCharacter
    form_class = UserCharacterForm
    success_url = reverse_lazy('user:profile')
    template_name = 'user/form.html'
    
profile_edit = ProfileEditView.as_view()



class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = UserCharacter
    form_class = UserCharacterForm
    success_url = reverse_lazy('user:profile')
    template_name = 'user/form.html'
    
    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().user_id == self.request.user

profile_edit = ProfileEditView.as_view()
