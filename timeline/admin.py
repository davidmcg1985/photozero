from django.contrib import admin

# Register your models here.
from .models import Media

class MediaModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "draft", "publish", "user"]
	list_display_links = ["title"]
	list_filter = ["updated", "timestamp", "publish"]
	list_editable = ["draft"]
	search_fields = ["title", "content"]

	class Meta:
		model = Media

admin.site.register(Media, MediaModelAdmin)