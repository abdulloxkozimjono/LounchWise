from rest_framework import viewsets
from .models import Service, Step, Pricing, FAQ, Contact, Tokenomics
from .serializers import ServiceSerializer, StepSerializer, PricingSerializer, FAQSerializer, ContactSerializer, TokenomicsSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TokenomicsViewSet(viewsets.ModelViewSet):
    queryset = Tokenomics.objects.all()
    serializer_class = TokenomicsSerializer
