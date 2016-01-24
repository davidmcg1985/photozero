from django import forms


from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "title",
            "content",
            "image_rotated",
            # "draft",
            # "publish",
        ]