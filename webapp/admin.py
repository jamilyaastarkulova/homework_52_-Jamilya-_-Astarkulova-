from django.contrib import admin
from webapp.models import Todo

# admin.site.register(Article)

# class ArticleAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Article, ArticleAdmin)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    search_fields = ('title', 'task')
    fields = ('id', 'title', 'task', 'status', 'created_at', 'updated_at')
    # exclude = []
    readonly_fields = ('id', 'created_at', 'updated_at')
