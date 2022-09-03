from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from blog.models import CustomUser
from blog.models import Course, Comment, Category, Language, Field
from blog.models import AboutUs

from .forms import ContactUsForm, ContactUsUserForm


class ListUpdateView(generic.ListView):  # show list update in home
    queryset = Course.objects.all().order_by('-created')[:3]
    template_name = 'home/home.html'
    context_object_name = 'course'


class AllVideoUpdateView(generic.ListView):  # show all video update
    queryset = Course.objects.all().order_by('-created')
    template_name = 'home/all_videos.html'
    context_object_name = 'course'
    paginate_by = 12


class AllVideoView(generic.ListView):  # show all video
    model = Course
    template_name = 'home/all_videos.html'
    context_object_name = 'course'
    paginate_by = 12


def category_list(request, pk):  # show category courses
    video = get_object_or_404(Category, id=pk)
    course = video.category.all()
    return render(request, 'home/all_videos.html', {'course': course})


def language_list(request, pk):  # show languages courses
    video = get_object_or_404(Language, id=pk)
    course = video.language.all()
    return render(request, 'home/all_videos.html', {'course': course})


def field_list(request, pk):  # show field courses
    video = get_object_or_404(Field, id=pk)
    course = video.field.all()
    return render(request, 'home/all_videos.html', {'course': course})


def video_detail_view(request, pk):  # show detail video
    course = get_object_or_404(Course, id=pk)

    if request.user.is_authenticated:
        if request.method == 'POST':  # if send comment
            parent_id = request.POST.get('parent_id')
            body = request.POST.get('body')

            Comment.objects.create(username=request.user, course=course, parent_id=parent_id, body=body)
            return render(request, 'home/video_detail.html', {'course': course})

    return render(request, 'home/video_detail.html', {'course': course})


def search_view(request):  # search video
    q = request.GET.get('q')
    list_course = Course.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    paginator = Paginator(list_course, 12)  # Show 12 contacts per page.
    page_number = request.GET.get('page')
    course = paginator.get_page(page_number)
    return render(request, 'home/all_videos.html', {'course': course})


def about_us_view(request):  # show about us page
    profile = CustomUser.objects.all()
    description = AboutUs.objects.all()
    return render(request, 'home/about_us.html', {'profile': profile, 'description': description})


def contact_us_view(request):  # show contact us page

    if request.user.is_authenticated:  # If user is authenticated
        if request.method == "POST":  # If request is post
            form = ContactUsForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                user.email = request.user.email
                user.save()
                form = ContactUsForm()
        else:
            form = ContactUsForm()  # call form

    else:  # If user isn't authenticated
        if request.method == "POST":
            form = ContactUsUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('home:contact_us')
        else:
            form = ContactUsUserForm()  # call form
    return render(request, 'home/contact_us.html', {'form': form})


class DeleteVideoView(generic.DeleteView):
    model = Course
    template_name = 'home/delete_video.html'
    success_url = reverse_lazy('home:home')
