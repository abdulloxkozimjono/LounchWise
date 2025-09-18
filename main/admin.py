from django.contrib import admin
from .models import User, Service, Step, Pricing, FAQ, Contact, Tokenomics


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "full_name", "is_staff", "is_active")
    search_fields = ("email", "full_name")
    list_filter = ("is_staff", "is_active")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "icon")
    search_fields = ("title",)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "title")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "is_popular")
    list_editable = ("is_popular",)
    search_fields = ("name",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question")
    search_fields = ("question",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "telegram", "email", "created_at")
    search_fields = ("name", "telegram", "email")
    list_filter = ("created_at",)


@admin.register(Tokenomics)
class TokenomicsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "percentage")
    search_fields = ("title",)
