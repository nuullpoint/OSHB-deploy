from django.contrib import admin

# Register your models here.

from .models import BlogAuthor, Blog, BlogComment, BlogView, BlogLike


# Minimal registration of Models.
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
admin.site.register(BlogView)
admin.site.register(BlogLike)


class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = BlogComment
    max_num = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('title', 'author', 'publish_date')
    inlines = [BlogCommentsInline]
