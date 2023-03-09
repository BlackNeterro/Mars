from rest_framework import serializers

from .models import Instance, AppType, Enterprise, Work, Module, Repayment, EnterpriceAccess, RepaymentModule


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'

class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = '__all__'

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'

class EnterpriceAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriceAccess
        fields = '__all__'

class RepaymentModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepaymentModule
        fields = '__all__'