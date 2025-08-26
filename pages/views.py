from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import redirect
from django import forms 
from django.shortcuts import render, redirect
from django.contrib import messages


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True, min_value=0)

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            messages.success(request, "Product has been created successfully!")
            return redirect("index")
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Santiago acevedo",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "email": "ouremail@email.com",
            "adress": "Medellin, Colombia",
            "phone": "35204165201",
        })
        return context
    
class Product:
 products = [
 {"id":"1", "name":"TV", "description":"Best TV", "price": 1000},
 {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 2500},
 {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 100},
 {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 2000}
 ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = next(p for p in Product.products if p["id"] == str(id))
        except StopIteration:
            return redirect('home')
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)