from django.shortcuts import render
from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name = "pages/home.html"
    
class aboutPageView(TemplateView):
 template_name = "pages/about.html"

 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Alberto Daniel Cervantes Forero",
    })
    return context

class contactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacto"
        context["subtitle"] = "Contáctanos"
        context["email"] = "fake-email@example.com"
        context["address"] = "123 Fake Street, Medellín, Colombia"
        context["phone"] = "+57 301 123 4567"
        return context