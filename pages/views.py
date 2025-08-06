from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    
class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 400},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 50},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 25}
    ]

class productIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        
        return render(request, self.template_name, viewData)
    
class productShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product_data = Product.products[int(id)-1]
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse("home"))

        viewData = {
            "title": product_data["name"] + " - Online Store",
            "subtitle": product_data["name"] + " - Product information",
            "product": product_data
        }
        return render(request, self.template_name, viewData)