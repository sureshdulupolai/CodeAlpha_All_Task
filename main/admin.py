from django.contrib import admin
from .models import URL

# Register your models here.
# Custom admin for URL model
class URLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'created_at')  # Columns to display in admin list
    search_fields = ('short_code', 'original_url')              # Add search functionality
    list_filter = ('created_at',)                               # Filter by creation date
    ordering = ('-created_at',)                                 # Latest URLs appear first

# Register the URL model with the custom admin
admin.site.register(URL, URLAdmin)
