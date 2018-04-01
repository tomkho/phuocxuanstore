from django.views.generic.edit import FormView

from .forms import ProfileForm
from .models import Profile

class ProfileView(FormView):
    template_name = 'store/profile.html'
    form_class = ProfileForm
    success_url = 'thanhtoan.html'

    def get_form(self, form_class):
        """
        Check if the user already saved contact details. If so, then show
        the form populated with those details, to let user change them.
        """
        try:
            profile = Profile.objects.get(user=self.request.user)
            return form_class(instance=profile, **self.get_form_kwargs())
        except Profile.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ProfileView, self).form_valid(form)
