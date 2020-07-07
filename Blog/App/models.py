from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["created"]

    def __str__(self):
        return self.title
