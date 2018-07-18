from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
	template_name="index.html"
		
class AboutPageView(TemplateView):
	template_name="about.html"
	
def year_archive(request, year):
	a_list= Article.objects.filter(pub_date__year=year)
	context= {'year' : year , 'article_list': a_list}
	return render(request, 'news/year_archive.html',context)
	