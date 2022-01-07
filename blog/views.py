from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendMessage, CommentForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import Message, News, User, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):

    data = {
        'title': "Главная страница"
    }

    return render(request, 'blog/home.html', data)


def contact(request):
    if request.method == "POST":
        sendMessage = SendMessage(request.POST)

        if sendMessage.is_valid():
            sendMessage.save()

            subject = Message.article
            plain_message = Message.text
            from_email = f"From {Message.email}"
            to = "alex@mail.ru"

            # сама функции отправки письма
            send_mail(subject, plain_message, from_email, [to])

            messages.success(request, f'Сообщение было отправленно')
            return redirect('contact-page')
    else:
        sendMessage = SendMessage()

    data = {'sendMessage': sendMessage}
    return render(request, 'blog/contact.html', data)


def uslugi(request):
    return render(request, 'blog/uslugi.html', {'title': "Услуги"})


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Новости'
        return ctx


class UserALLNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserALLNewsView, self).get_context_data(**kwargs)

        ctx['title'] = f"Cтатьи пользователя {self.kwargs.get('username')}"
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        ctx['form'] = CommentForm()
        ctx['comments'] = Comment.objects.filter(title=self.kwargs['pk']).order_by('-date')
        return ctx

    def post(self, request, *args, **kwargs):

        if request.method == "POST":

            commentForm = CommentForm(request.POST)

            if commentForm.is_valid():
                comment = Comment()
                comment.user = request.user
                comment.title = News.objects.get(pk=self.kwargs['pk'])
                comment.text = commentForm.cleaned_data['text']
                comment.save()
                url = '/news/' + str(self.kwargs['pk'])
                return redirect(url)


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/news_create.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NewsCreateView, self).get_context_data(**kwargs)

        ctx['title'] = 'Добавить статью'
        ctx['btn_text'] = 'Добавить'
        return ctx


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/news_create.html'

    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NewsUpdateView, self).get_context_data(**kwargs)

        ctx['title'] = 'Редактировать статью'
        ctx['btn_text'] = 'Обновить'
        return ctx


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'blog/news_delete.html'
    success_url = '/news'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False
