from django.contrib import admin

# Register your models here.
from .models import Photo

class PhotoModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "user"]
	#list_display_links = ["title"]
	list_filter = ["updated", "timestamp"]
	#list_editable = ["draft"]
	search_fields = ["title", "content"]

	class Meta:
		model = Photo

admin.site.register(Photo, PhotoModelAdmin)