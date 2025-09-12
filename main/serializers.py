from rest_framework import serializers
from .models import Service, Step, Pricing, FAQ, Contact, Tokenomics


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class TokenomicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokenomics
        fields = "__all__"