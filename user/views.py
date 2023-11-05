from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, CreateView, DetailView, View
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserCharacter
from .forms import UserCharacterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
import requests
from datetime import datetime

def main(request):
    return render(request, 'main.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/form.html'
    success_url = '/profile/write' # 회원가입후 프로필 작성페이지로 이동

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        auth_login(self.request, user) # 자동 로그인
        # UserCharacter.objects.create(user_id = User)
        return response
    

register = RegisterView.as_view()

def success_register(request):
    return render(request, 'success_register.html')

login = LoginView.as_view(
    template_name = 'user/form.html',
)

logout = LogoutView.as_view(
    next_page = '/'
)


# 프로필 상세조회
class ProfileDetailView(DetailView):
    model = UserCharacter
    template_name = 'user/profile_detail.html'
profile_detail = ProfileDetailView.as_view()


# 프로필 작성하기
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserCharacter
    form_class = UserCharacterForm
    template_name = 'user/form.html'
    def form_valid(self, form):
        info = form.save(commit=False) 
        info.user_id = self.request.user
        return super().form_valid(form) 
    
    def get_success_url(self): # 작성에 성공하면 프로필 상세페이지로 이동
        return reverse('user:profile_detail', kwargs={'pk' : self.object.user_id.pk})

profile_write = ProfileCreateView.as_view()



# 프로필 수정하기
class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = UserCharacter
    form_class = UserCharacterForm
    template_name = 'user/form.html'
    def test_func(self):
        return self.get_object().user_id == self.request.user
    
    def get_success_url(self): # 작성에 성공하면 프로필 상세페이지로 이동
        return reverse('user:profile_detail', kwargs={'pk' : self.object.user_id.pk})

profile_edit = ProfileEditView.as_view()

# cube
def cube_history(request):
    return render(request, 'cube/cube_history.html')

class CubeHistory(View):
    model = UserCharacter
    template_name = 'user/cube_history.html'
    
    def get(self, request):
        url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results?count=10&date='
        search_date = request.GET.get('date')
        if search_date is None:
            today = datetime.today()
            print('noneType입니다')
            search_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
        url += search_date

        user = request.user
        userCharacter = UserCharacter.objects.get(user_id = user.pk)
        api_key = userCharacter.maple_api_key

        headers = {
            'Authorization': api_key
        }

        result = '에러'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            result = result['cube_histories']
            # print(result[0])
            return render(request, 'user/cube_history.html', {'result':result[0]})
        else:
            return render(request, 'user/cube_history.html', {'result':result})

cube_history = CubeHistory.as_view()