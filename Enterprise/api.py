from .models import (Enterprise,
                     Instance,
                     AppType,
                     Work,
                     Module,
                     Repayment,
                     EnterpriceAccess,
                     RepaymentModule)
from rest_framework import viewsets, permissions
from .serializers import (InstanceSerializer,
                          AppTypeSerializer,
                          EnterpriseSerializer,
                          WorkSerializer,
                          ModuleSerializer,
                          RepaymentSerializer,
                          EnterpriceAccessSerializer,
                          RepaymentModuleSerializer)


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = EnterpriseSerializer

class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = InstanceSerializer

class AppTypeViewSet(viewsets.ModelViewSet):
    queryset = AppType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = AppTypeSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = WorkSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = ModuleSerializer

class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = Repayment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = RepaymentSerializer

class EnterpriceAccessViewSet(viewsets.ModelViewSet):
    queryset = EnterpriceAccess.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = EnterpriceAccessSerializer

class RepaymentModuleAccessViewSet(viewsets.ModelViewSet):
    queryset = RepaymentModule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
serializer_class = RepaymentModuleSerializer