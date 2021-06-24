from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import View
from rest_framework import mixins, viewsets
from rest_framework.views import Response
from rest_framework import permissions
from shortner.serializers import UrlSerializer
from .serializers import UrlSerializer

from .models import Url


class UrlViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def retrieve(self, request, pk):
        data_cache = cache.get(f"url-{pk}")
        if data_cache:
            return Response(data_cache)

        data = Url.objects.filter(pk=pk).first()
        _data = UrlSerializer(data)
        if data:
            cache.set(f"url-{pk}", _data.data, 60)
            return Response(_data.data)
        raise Http404

    def create(self, request, *args, **kwargs):
        result = UrlSerializer(data=request.data)
        result.is_valid(raise_exception=True)
        result.save()
        url = 'http://localhost:8000/'
        url += result.instance.url_hash
        return Response({"url":url})

class UrlResolver(View):
    def get(self, request, *args, **kwargs):
        cache_key = f"url-{kwargs.get('url')}"
        data_cache = cache.get(cache_key)
        if data_cache:
            return HttpResponseRedirect(data_cache.get("url_full"))

        data = Url.objects.filter(url_hash=kwargs.get("url")).first()
        _data = UrlSerializer(data)
        if data:
            cache.set(cache_key, _data.data, 60)
            return HttpResponseRedirect(data.url_full)

        raise Http404

def redirect_to_login(request):
    return redirect('/admin/login/?next=/panel/')