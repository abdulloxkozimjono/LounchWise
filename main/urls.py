from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, StepViewSet, PricingViewSet, FAQViewSet, ContactViewSet, TokenomicsViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'steps', StepViewSet)
router.register(r'pricing', PricingViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'tokenomics', TokenomicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
