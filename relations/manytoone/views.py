from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article

# Create your views here.
def create(request):
    reporter = Reporter(
        first_name="Juan",
        last_name="Perez",
        email="[EMAIL_ADDRESS]"
    )
    article = Article(
        headline="Juan Perez Articulo 1",
        pub_date="2022-01-01",
        reporter=reporter
    )
    article2 = Article(
        headline="Juan Perez Articulo 2",
        pub_date="2022-01-02",
        reporter=reporter
    )
    article3 = Article(
        headline="Juan Perez Articulo 3",
        pub_date="2022-01-03",
        reporter=reporter
    )
    reporter.save()
    article.save()
    article2.save()
    article3.save()
    result = reporter.article_set.all()
    return HttpResponse(result)
    
