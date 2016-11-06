from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cp.pdns_models import Domains, Records
from api.serializers import DomainSerializer, RecordSerializer
from django.http import Http404

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    return HttpResponse("no")

@csrf_exempt
def dns_index(request):
    domains = Domains.objects.using('pdns').all()
    serializer = DomainSerializer(domains, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def dns_zone(request, zone_name):
    zone = Domains.objects.using('pdns').filter(name = zone_name).first()
    if zone is None:
        raise Http404

    records = Records.objects.using('pdns').filter(domain_id = zone.id)
    serializer = RecordSerializer(records, many=True)
    return JSONResponse(serializer.data)