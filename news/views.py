from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_new.html'

    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/delete_new.html'


def news(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


def create_new(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Неверная форма'

    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create_new.html', data)
