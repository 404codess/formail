from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'mailer/mailer.html'
    success_url = 'https://example.com'

    def form_valid(self, form):
        # Save the contact instance
        response = super().form_valid(form)
        # Any additional logic after saving (optional)
        return response
