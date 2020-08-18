from datetime import datetime

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    News,
    Comment
)

class NewsAdmin(admin.ModelAdmin):
    search_fields = ('name', 'create_date')
    list_display = ('name', 'new_date')

    def new_date(self, obj):
        if datetime.today().date() > obj.create_date:
            return mark_safe(u'<span style="color:red">%s</span>' % obj.create_date)
        else:
            return mark_safe(u'<span style="color:green">%s</span>' % obj.create_date)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment)

# Register your models here.
