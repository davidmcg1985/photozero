from django import forms
from django.template.defaultfilters import filesizeformat
from .models import Photo, Comment


class PhotoForm(forms.ModelForm):

    def clean(self):
        #first, run the built-in clean. cleaned_data is a dictionary of all of the stuff in the form
        cleaned_data = super(PhotoForm, self).clean()

        #check and see if we have image in our data dictionary (ie, if there is a dictionary key called 'image')
        if 'image' in cleaned_data:
            #reject the upload if the file is too large (size is in bytes, this magic number = 2.5MB)
            if cleaned_data['image']._size > 2621440:
                raise forms.ValidationError('Please keep files under %s. Your file is %s.' % (filesizeformat(2621440), filesizeformat(cleaned_data['image']._size)))

        #always return the cleaned_data dictionary
        return cleaned_data
        
    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "image",
        ]


class CommentForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea, label='Leave a comment: ')
	class Meta:
		model = Comment
		fields = [
			"text",
		]


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160