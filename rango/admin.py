from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

#Adding further classes which may be created in the future is as simple
# as adding another call to the admin.site.register() method
