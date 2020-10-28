from django.contrib import admin
from gestao.models import Categoria


class CategoriaInline(admin.StackedInline):
    model = Categoria


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [
        CategoriaInline,
    ]


admin.site.register(Categoria, CategoriaAdmin)