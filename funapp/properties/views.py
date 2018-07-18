from django.shortcuts import get_object_or_404, render
from .models import Property


def index(request):
    latest_property_list = Property.objects.order_by('-pub_date')[:5]
    context = {'latest_property_list': latest_property_list}
    return render(request, 'properties/index.html', context)


def detail(request, property_id):
    p = get_object_or_404(Property, pk=property_id)
    return render(request, 'properties/detail.html', {'property': p})


def trade(request, property_id):   # will want to add a user id to track who is buying the shares
    p = get_object_or_404(Property, pk=property_id)
    return render(request, 'properties/trade.html', {'property': p})
