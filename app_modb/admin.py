from django.contrib import admin
from app_modb import models

# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)
admin.site.register(models.Topic,TopicAdminView)

class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name')
    list_editable=('name',)
    list_filter=('topic',)
admin.site.register(models.Webpage,WebpageAdminView)

class AccessdetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('webpage','datetime')
admin.site.register(models.AccessDetail,AccessdetailsAdminView)
