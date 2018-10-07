from django.contrib import admin

# Register your models here.
from bio.models import Gene, Keyword, Source


class KeywordInline(admin.StackedInline):
    model = Keyword

class SourceInline(admin.TabularInline):
    model = Source

@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    inlines = [KeywordInline, SourceInline]
    list_display = ['code', 'name', 'sequence', 'source']
    search_fields = ['keywords__name']
