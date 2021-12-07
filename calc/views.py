from django.shortcuts import render
from django.views import generic
from . import forms
from django.urls import reverse_lazy

def index(request):
    return render(request, 'calc/index.html')

def description(request):
    return render(request, 'calc/description.html')

class InquiryView(generic.FormView):
    template_name = "calc/inquiry.html"
    form_class = forms.InquiryForm
    success_url = reverse_lazy('calc:index')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)