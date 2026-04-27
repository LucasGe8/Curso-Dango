from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.
def create(request):
    pub1 = Publication(title="El País")
    pub2 = Publication(title="The Sun")
    pub3 = Publication(title="The Times")
    pub1.save()
    pub2.save()
    pub3.save()
    article = Article(headline="Noticia")
    article.save()
    article.publications.add(pub1, pub2, pub3)
    pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()
    result = pub1.title
    
    #para eliminar 
    #article.publications.remove(pub1)
    #para eliminar todas
    #article.publications.clear()
    #para eliminar las publicaciones que coincidan con la consulta
    #article.publications.filter(id=1).delete()
    #para obtener las publicaciones en comun entre dos articulos
    article1 = Article.objects.get(id=1)
    article2 = Article.objects.get(id=2)
    result = article1.publications.intersection(article2.publications)
    #Para obtener la diferencia entre dos conjuntos
    result = article1.publications.difference(article2.publications)
    #Para obtener la diferencia simetrica entre dos conjuntos
    result = article1.publications.symmetric_difference(article2.publications)
    #Para obtener la union entre dos conjuntos
    result = article1.publications.union(article2.publications)
    return HttpResponse(result)

    