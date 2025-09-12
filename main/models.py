from django.db import models

# Xizmatlar
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)  # frontend uchun

    def __str__(self):
        return self.title


# Bosqichlar (Step-by-step)
class Step(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


# Pricing paketlar
class Pricing(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()  # JSON yoki string qilib saqlash mumkin
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# FAQ
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# Contact forma (saytdan va botdan kelganlar)
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.telegram})"


class Tokenomics(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.FloatField(help_text="Ajratilgan foiz (%)")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.percentage}%"