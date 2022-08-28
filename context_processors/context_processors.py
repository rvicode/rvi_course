from blog.models import Category, Language, Field


def context_processors(request):
    category = Category.objects.all()
    language = Language.objects.all()
    field = Field.objects.all()
    return {'category': category, 'language': language, 'field': field}
