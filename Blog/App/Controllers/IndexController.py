from django.shortcuts import render, HttpResponse
from django.core.paginator import *
from App.Models.Blog_models import Blog_models
from ..models import Blog


class IndexController():
    def index(self):

        blog = Blog.objects.all()
        count = blog.count()
        paginator = Paginator(blog, 3)
        page = self.GET.get("page")
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {"blog": items, "count": count}
        return render(self, "Views/Index/index.html", context)

    def buscar(self):
        queryset_list = Blog.objects.all()
        filtrar = self.GET.get("filtrar")
        if filtrar:
            queryset_list = queryset_list.filter(title__icontains=filtrar)
        count = queryset_list.count()
        paginator = Paginator(queryset_list, 3)
        page = self.GET.get("page")
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {"blogsearch": items, "count2": count}
        return render(self, "Views/Index/buscar.html", context)

    def about(self):
        return render(self, "Views/Index/about.html")
