from django.contrib import admin
from models import Share, Category

class ShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'category', 'status',)
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('created', 'status')
    
admin.site.register(Share, ShareAdmin)
admin.site.register(Category)
