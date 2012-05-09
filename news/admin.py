from django.contrib import admin
admin.autodiscover()

from models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'author','created','is_draft')
	filter_horizontal = ('category',)
	class Media:
		js = ('js/tiny_mce/tiny_mce.js','js/application.js',)

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)