from django.contrib import admin
from .models import Essay, EssayCategory
from tinymce.widgets import TinyMCE
from django import forms

class EssayAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    blockquote = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Essay
        fields = '__all__'

class EssayAdmin(admin.ModelAdmin):
    form = EssayAdminForm

admin.site.register(Essay, EssayAdmin)
admin.site.register(EssayCategory)
