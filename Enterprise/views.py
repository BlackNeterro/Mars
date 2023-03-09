from rest_framework import generics
from .models import Instance, AppType, Enterprise, Work, Module, Repayment, EnterpriceAccess, RepaymentModule
from .serializers import InstanceSerializer, AppTypeSerializer, EnterpriseSerializer, WorkSerializer, ModuleSerializer, RepaymentSerializer, EnterpriceAccessSerializer, RepaymentModuleSerializer


#import coreapi
#from django.shortcuts import render
#from rest_framework.decorators import api_view, schema
#from rest_framework.response import Response
#from rest_framework.schemas import AutoSchema

# Create your views here.

#@api_view(['GET'])
#@schema(AutoSchema(manual_fields=[
#    coreapi.Field(name='my_field', required=True, location='query', description='A required field'),
#    coreapi.Field(name='another_field', required=False, location='query', description='An optional field'),
#]))
#def my_endpoint(request):
#    my_field = request.query_params.get('my_field')
#    another_field = request.query_params.get('another_field')
#    # Your code here
#    return Response({'my_field': my_field, 'another_field': another_field})

class InstanceListCreateView(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class InstanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


class AppTypeListCreateView(generics.ListCreateAPIView):
    queryset = AppType.objects.all()
    serializer_class = AppTypeSerializer

class AppTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppType.objects.all()
    serializer_class = AppTypeSerializer


class EnterpriseListCreateView(generics.ListCreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class EnterpriseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class RepaymentListCreateView(generics.ListCreateAPIView):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer

class RepaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer


class EnterpriceAccessListCreateView(generics.ListCreateAPIView):
    queryset = EnterpriceAccess.objects.all()
    serializer_class = EnterpriceAccessSerializer

class EnterpriceAccessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnterpriceAccess.objects.all()
    serializer_class = EnterpriceAccessSerializer


class RepaymentModuleAccessListCreateView(generics.ListCreateAPIView):
    queryset = RepaymentModule.objects.all()
    serializer_class = RepaymentModuleSerializer

class RepaymentModuleAccessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RepaymentModule.objects.all()
    serializer_class = RepaymentModuleSerializer

