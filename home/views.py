from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, redirect,get_object_or_404
from .models import Home, Contact_me, Article,About
from .forms import ContactForm,CommentForm

def home(request):
    home = Home.objects.filter(is_published=True).first()
    articles_last4 = (
        Article.objects.filter(is_published=True)
        .annotate(published_comments_count=Count('comments', filter=Q(comments__is_published=True)))
        .order_by('-created')[:4]
    )
    context = {
        'home': home,
        'articles_last4': articles_last4,
        'page_title': 'Home',
    }
    return render(request, 'index.html', context)


def about(request):
    home = Home.objects.filter(is_published=True).first()
    about = About.objects.filter(is_published=True)
    context = {
        'home': home,
        'about': about,
        'page_title': 'About',
    }
    return render(request, 'about.html', context)


def contact(request):
    home = Home.objects.filter(is_published=True).first()
    contact_me = Contact_me.objects.filter(is_published=True)
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')

    return render(request, 'contact.html', {
        'home': home,
        'contact_me': contact_me,
        'form': form,
        'page_title': 'Contact',
    })


def blog(request):
    home = Home.objects.filter(is_published=True).first()
    articles_qs = Article.objects.filter(is_published=True).annotate(
        approved_comments_count=Count('comments', filter=Q(comments__is_published=True))
    ).order_by('-created')

    p = Paginator(articles_qs, 1)
    page = request.GET.get('page')
    articles = p.get_page(page)

    return render(request, 'blog.html', {
        'home': home,
        'articles': articles,
        'page_title': 'Blog',
    })


def blog_single(request, pk):
    home = Home.objects.filter(is_published=True).first()
    article = get_object_or_404(Article, pk=pk, is_published=True)
    comments = article.comments.filter(is_published=True)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('.')

    ctx = {
        'home': home,
        'article': article,
        'comments': comments,
        'form': form,
        'page_title': article.title,
    }
    return render(request, 'blog-single.html', ctx)
