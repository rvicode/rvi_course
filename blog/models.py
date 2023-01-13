from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class Field(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("framework"))

    class Meta:
        verbose_name = _("framework")
        verbose_name_plural = _("frameworks")

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Language programming"))

    class Meta:
        verbose_name = _("Language programming")
        verbose_name_plural = _("Languages programming")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name=_("Category programming"))

    class Meta:
        verbose_name = _("Category programming")
        verbose_name_plural = _("Categorys programming")

    def __str__(self):
        return self.title


class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Teacher"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    category = models.ManyToManyField(Category, related_name='category',
                                      verbose_name=_("Category programming"), null=True, blank=True)
    field = models.ManyToManyField(Field, related_name='field', verbose_name=_("framework"), null=True, blank=True)
    language = models.ManyToManyField(Language, related_name='language',
                                      verbose_name=_("Language programming"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    image = models.ImageField(upload_to='Courses/image/', verbose_name=_("Image"), null=True, blank=True)
    file = models.FileField(upload_to='Courses/video/', verbose_name=_("File"), null=True, blank=True)
    time_video = models.CharField(max_length=20, verbose_name=_("Time_video"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created"))
    update = models.DateField(auto_now=True, verbose_name=_("Updated"))
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:detail_video', args=[self.id])


class Comment(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment', verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comment', verbose_name=_("Course"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replay',
                               verbose_name=_("Parent"))
    body = models.TextField(verbose_name=_("description"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f'{self.body}'


class AboutUs(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    our_products = models.TextField(verbose_name=_("Our_products"))

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    user = models.CharField(max_length=100, verbose_name=_("User"))
    email = models.CharField(max_length=100, verbose_name=_("Email"))
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    massage = models.TextField(verbose_name=_("Massage"))

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")

    def __str__(self):
        return f'{self.user}: {self.email}'


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes', verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='likes', verbose_name=_("Course"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.user.username}: {self.course.title}'
