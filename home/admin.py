from django.contrib import admin

from .models import *
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['full_name','is_read']
    list_editable = ['is_read']
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    model = Home
    list_display = ('full_name','is_published')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['full_name','article','is_published']
    list_filter = ['is_published']
    list_editable = ['is_published']
    search_fields = ['full_name','article','is_published']

@admin.register(Contact_me)
class ContactMeAdmin(admin.ModelAdmin):
    model = Contact_me
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ('title','is_published')
admin.site.register(Article)
admin.site.register(Tags)
admin.site.register(Footer)
