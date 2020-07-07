from django.db import models, connection
from ..models import Blog


class Blog_models():
    def blog_list(filtrar):
        blog = Blog.objects.filter(title__icontains=filtrar)
        return blog
