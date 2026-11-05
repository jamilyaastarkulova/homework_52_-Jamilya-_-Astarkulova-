from django.contrib import admin
from webapp.models import Todo

# admin.site.register(Article)

# class ArticleAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Article, ArticleAdmin)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task')
    fields = ('id', 'task', 'status', 'created_at')
    # exclude = []
    readonly_fields = ('id', 'created_at')
