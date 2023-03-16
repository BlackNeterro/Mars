from rest_framework import serializers

from .models import Instance, AppType, Enterprise, WorkMessage, MessageType, Module, Repayment, EnterpriceAccess, RepaymentModule


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

class WorkMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkMessage
        fields = '__all__'

class MassageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
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