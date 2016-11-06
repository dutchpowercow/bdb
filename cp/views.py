from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from cp.pdns_models import Domains, Records


def cp_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/cp")

    return redirect("/cp/login")

class Product:
    id = -1
    name = ""
    description = ""
    status = "unset"

    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status



@login_required
def cp_index(request):

    products = [
        Product(100341, "buckets", "a large bucket of buckets", "actief"),
        Product(100343, "Domein registratie", "bobisnietlui.nl", "actief"),
        Product(100344, "Website 1", "bobisnietlui.nl", "actief"),
        Product(100343, "Opname in nameservers", "bobisnietlui.nl", "actief"),
        Product(100533, "E-Mail", "23x", "actief"),
        Product(100673, "Domein registratie", "hans-olo.nl", "actief"),
        Product(100674, "Domein registratie", "hansduo.nl", "actief")
        ]

    context = { "products": products }
    template = loader.get_template('cp_index.html')
    return HttpResponse(template.render(context, request))


@login_required #funny, aint it
def cp_logout(request):
    logout(request)
    return redirect("/")


@login_required
def cp_dns_index(request, zone_name=None):

    def contains(list, filter):
        for x in list:
            if filter(x):
                return True
        return False
    
    def get_zone(list, filter):
        for x in list:
            if x.name == filter:
                return x
        return None


    def names(list):
        n = []
        for x in list:
            n.append(x.name)
        return n

    zonesList = Domains.objects.using('pdns').all()
    zones = names(zonesList)
    records = {}
    zone = get_zone(zonesList, zone_name)

    if zone_name not in zones and zone_name is not None:
        raise Http404

    records = {}
    if zone_name is not None:
        records = Records.objects.using('pdns').filter(domain_id = zone.id)

    context = {'message': "dns beheer yo", 'zone_name': zone_name, "zones": zones,  "records": records}
    template = loader.get_template('cp_dns_index.html')
    return HttpResponse(template.render(context, request))


@login_required
def cp_dns_details(request, zone_name):


    # todo: check if user has rights on accessing this resource
    #if not request.user.is_authenticated:
    #    raise PermissionDenied

    if zone_name not in records:
        raise Http404

    context = {'zone_name': zone_name, "records": records}
    template = loader.get_template('cp_dns_details.html')
    return HttpResponse(template.render(context, request))
