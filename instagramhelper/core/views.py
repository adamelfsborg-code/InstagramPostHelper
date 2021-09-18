from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views import View

class MainCoreView(View):
    def get(self, request, *args, **kwargs):
        return render('index.html')