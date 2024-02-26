from django.contrib import admin

from main.models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("nama", "npm")


admin.site.register(Developer, DeveloperAdmin)
