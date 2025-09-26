from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, RegisterView, LoginView, ProfileView,
    DeleteUserView, StepViewSet, PricingViewSet, FAQViewSet,
    ContactViewSet, TokenomicsViewSet
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'steps', StepViewSet)
router.register(r'pricing', PricingViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'tokenomics', TokenomicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
]
