from django.contrib import admin

# my models Modules,
from post.models import Post,Tag,Author

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","date_created","author","status")

class TagAdmin(admin.ModelAdmin):
    list_display = ("name","frequency")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("fullname","email")

admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Author,AuthorAdmin)