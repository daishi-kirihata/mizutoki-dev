# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, FormView

from .forms import InquiryForm

class IndexView(TemplateView):
    template_name = "index.html"
    
class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm