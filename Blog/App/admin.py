from django.contrib import admin
from .models import Blog


class Projectadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Blog, Projectadmin)
