from django.contrib import admin

from . models import Menu, Item


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'menu')
    list_filter = ('menu', )
    fieldsets = (
        (None, {
            'fields': (('menu', 'parent'), 'title')
        }),
    )

    # def url(self, instance):
    #     return '<a href="%s">View on site</a>' % (instance.get_absolute_url())
    # url.allow_tags = True