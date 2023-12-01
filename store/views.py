from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item

class HomePageView(TemplateView):
    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        products = Item.objects.all()
        context = super(HomePageView, self).get_context_data(**kwargs)
        #context = super().get_context_data(**kwargs)
        #context["items"] = products
        context.update({
             "items": products,
         })
        return context
class SuccessView(TemplateView):
    template_name = "store/success.html"


class CancelView(TemplateView):
    template_name = "store/cancel.html"


class ItemPageView(TemplateView):
    template_name = "store/item.html"










