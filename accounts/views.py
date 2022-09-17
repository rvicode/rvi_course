from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm, EditCustomUserForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


class UserPanelView(generic.ListView):
    model = CustomUser
    template_name = 'account/user_panel.html'


def edit_user_panel_view(request):

    if not request.user.is_authenticated:
        return redirect('home:home')

    else:
        user = request.user

        if request.method == 'POST':
            form = EditCustomUserForm(request.POST, request.FILES, instance=user)
            if form is not None:
                if form.is_valid():
                    form.save()
                    return redirect('home:home')
                else:
                    return render(request, 'account/edit_user_panel.html', {'form': form})

        else:
            form = EditCustomUserForm(instance=user)
            return render(request, 'account/edit_user_panel.html', {'form': form})
