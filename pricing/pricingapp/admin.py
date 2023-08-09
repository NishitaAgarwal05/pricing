from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.DistanceAdditionalPrice)
class DAPAdmin(admin.ModelAdmin):
    list_display = ["id", "price", "distance"]
    list_editable = ["price", "distance"]
    list_per_page = 10

    # def save


@admin.register(models.DistanceBasePrice)
class DBPAdmin(admin.ModelAdmin):
    list_display = ["id", "price", "distance", "day"]
    list_editable = ["price", "distance", "day"]
    list_per_page = 10


@admin.register(models.TimeMultiplicationFactor)
class TMFAdmin(admin.ModelAdmin):
    list_display = ["id", "time", "multiplication_factor"]
    list_editable = ["time", "multiplication_factor"]
    list_per_page = 10

@admin.register(models.WaitingCharges)
class WCAdmin(admin.ModelAdmin):
    list_display = ["id", "buffer", "waiting_rate", "waiting_time"]
    list_editable = ["buffer", "waiting_rate", "waiting_time"]
    list_per_page = 10
