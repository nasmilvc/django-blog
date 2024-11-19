from django.contrib import admin

from blogging.models import Post, Category


# create an InlineModelAdmin to represent Categories on the Post admin view.
class CategoryInline(admin.TabularInline):
    model = Category.posts.through  # through attribute is a reference to model that manages the many-to-many relation
    extra = 1  # standard is 3

# create a customized ModelAdmin class for Post and Category models.
class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, )
    fields = ('title', 'text', 'author', 'published_date')

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
