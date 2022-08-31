from django.contrib import admin

from .models import Category, Course, Comment, Field, Language, AboutUs


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'update',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'course', 'body', 'parent',)


@admin.register(Field)
class FieldsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Language)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'our_products']
