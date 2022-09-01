from django.contrib import admin

from .models import Category, Course, Comment, Field, Language, AboutUs, ContactUs


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'update', )
    search_fields = ['author', 'title', 'created', 'update', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title', ]


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'course', 'body', 'parent', )
    search_fields = ['username', 'course', 'body', 'parent', ]


@admin.register(Field)
class FieldsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title', ]


@admin.register(Language)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title', ]


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'our_products', )
    search_fields = ['title', 'description', 'our_products', ]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'subject', 'massage', )
    search_fields = ['user', 'email', 'subject', 'massage', ]
