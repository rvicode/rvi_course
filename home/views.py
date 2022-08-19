from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from blog.models import Course, Comment


class HomeCoursesView(generic.ListView):
    queryset = Course.objects.all().order_by('-created')[:6]
    template_name = 'home/home.html'
    context_object_name = 'course'


class AllVideoView(generic.ListView):
    model = Course
    template_name = 'home/all_videos.html'
    context_object_name = 'course'
    paginate_by = 12


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
