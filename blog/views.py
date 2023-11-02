from django.shortcuts import render
from django.conf import settings
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import requests

def main(request):
    return render(request, 'main.html')

# 블로그 첫 화면, 게시글 조회
class PostListView(ListView):
    model = Post
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()

# 제목검색
class PostSearchByTitleView(ListView):
    model = Post
    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['title']

        if qs:
            qs = qs.filter(title__icontains = tag)
        return qs
    
post_search_title = PostSearchByTitleView.as_view()


# 태그검색
class PostSearchByTagView(ListView):
    model = Post
    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['tag']

        if qs:
            qs = qs.filter(category__name__contains = tag)
        return qs
    


post_search_tag = PostSearchByTagView.as_view()


# 글 새로 작성하기
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'

    def form_valid(self, form):
        video = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.

post_write = PostCreateView.as_view()

# 글 상세 조회
class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    # def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
    #     return self.get_object().is_private == False
    

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    # 조회수
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()

# 글 수정
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()

# 글 삭제
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()


# 댓글작성
@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })


def post_detail_fail(request):
    return render(request, 'blog/post_detail_fail.html')