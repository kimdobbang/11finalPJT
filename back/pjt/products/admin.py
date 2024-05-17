from django.contrib import admin
from .models import Fixed, Installment, FixedOption, InstallmentOption

# Register your models here.
admin.site.register(Fixed)
admin.site.register(Installment)
admin.site.register(FixedOption)
admin.site.register(InstallmentOption)
