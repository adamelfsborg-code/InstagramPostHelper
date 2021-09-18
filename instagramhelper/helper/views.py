from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views import View
# Create your views here.
class HelperMainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'helper.html')