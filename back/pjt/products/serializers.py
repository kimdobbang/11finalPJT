from rest_framework import serializers
from .models import Fixed, FixedOption, Installment, InstallmentOption

class FixedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = '__all__'

class FixedOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedOption
        fields = '__all__'
        
class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = '__all__'
        
class InstallmentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentOption
        fields = '__all__'
