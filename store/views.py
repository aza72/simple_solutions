from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item


