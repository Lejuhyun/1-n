from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def create(request): # 1. 빈 종이를 주는 과정 # 2. 데이터베이스에 저장하는 과정
    if request.method == 'POST': 
        form = ArticleForm(request.POST) # 사용자의 정보를 담은 articleForm
        if form.is_valid(): #유효성검사
            form.save() # 유효하다면 폼을 저장
            return redirect('articles:index')
    else: # 빈 종이를 주는 과정(else문이 먼저 발생)
        form = ArticleForm() # Html코드를 변수로 저장해준다

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html',context)

def detail(request, id):
    article = Article.objects.get(id = id)

    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)