from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import Q

from blog.models import CustomUser
from blog.models import Course, Comment, Category, Language, Field
from blog.models import AboutUs


class LastUpdateView(generic.ListView):
    queryset = Course.objects.all().order_by('-created')[:3]
    template_name = 'home/home.html'
    context_object_name = 'course'


class AllVideoUpdateView(generic.ListView):
    queryset = Course.objects.all().order_by('-created')
    template_name = 'home/all_videos.html'
    context_object_name = 'course'
    paginate_by = 12


class AllVideoView(generic.ListView):
    model = Course
    template_name = 'home/all_videos.html'
    context_object_name = 'course'
    paginate_by = 12


def category_list(request, pk):
    video = get_object_or_404(Category, id=pk)
    course = video.category.all()
    return render(request, 'home/all_videos.html', {'course': course})


def language_list(request, pk):
    video = get_object_or_404(Language, id=pk)
    course = video.language.all()
    return render(request, 'home/all_videos.html', {'course': course})


def field_list(request, pk):
    video = get_object_or_404(Field, id=pk)
    course = video.field.all()
    return render(request, 'home/all_videos.html', {'course': course})


def video_detail_view(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            parent_id = request.POST.get('parent_id')
            body = request.POST.get('body')
            print(parent_id)
            print(body)
            Comment.objects.create(username=request.user, course=course, parent_id=parent_id, body=body)

    return render(request, 'home/video_detail.html', {'course': course})


def search_view(request):
    q = request.GET.get('q')
    list_course = Course.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    paginator = Paginator(list_course, 12)  # Show 12 contacts per page.
    page_number = request.GET.get('page')
    course = paginator.get_page(page_number)
    return render(request, 'home/all_videos.html', {'course': course})


def about_us_view(request):
    profile = CustomUser.objects.all()
    description = AboutUs.objects.all()
    return render(request, 'home/about_us.html', {'profile': profile, 'description': description})
