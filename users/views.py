from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView


from .models import CustomUser
from braces.views import LoginRequiredMixin

class UpdateCustomUserView(LoginRequiredMixin, UpdateView):
    fields = ['first_name','last_name','department','position', 'phone', 'chief' ]
    model = CustomUser

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:update")

    def get_object(self):
        # Only get the User record for the user making the request
        return self.request.user

