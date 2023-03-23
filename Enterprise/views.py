from rest_framework import generics
from rest_framework.decorators import api_view,schema
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Instance, AppType, Enterprise, MessageType, WorkMessage, Module, Repayment, EnterpriceAccess, RepaymentModule
from .serializers import InstanceSerializer, AppTypeSerializer, EnterpriseSerializer, MassageTypeSerializer,WorkMessageSerializer, ModuleSerializer, RepaymentSerializer, EnterpriceAccessSerializer, RepaymentModuleSerializer

# @api_view(['POST'])
# @csrf_exempt
# def add_Instance(request):
#     instanceNumber = request.POST.get('instanceNumber')
#     dBeg = request.POST.get('dBeg')
#     OS = request.POST.get('OS')
#     extMemory = request.POST.get('extMemory')
#     path = request.POST.get('path')
#     iin_superuser = request.POST.get('iin_superuser')
#     fio_kz = request.POST.get('fio_kz')
#     fio_ru = request.POST.get('fio_ru')
#     email = request.POST.get('email')
#     fio_en = request.POST.get('fio_en')
#     phoneNumber = request.POST.get('phoneNumber')
#     cmt_kz = request.POST.get('cmt_kz')
#     cmt_ru = request.POST.get('cmt_ru')
#     cmt_en = request.POST.get('cmt_en')
#     Instance = Instance(instanceNumber =instanceNumber, dBeg =dBeg, OS = OS, extMemory = extMemory, path = path, iin_superuser =iin_superuser, fio_kz = fio_kz, fio_ru = fio_ru, email = email, fio_en = fio_en, phoneNumber = phoneNumber, cmt_kz = cmt_kz, cmt_ru = cmt_ru, cmt_en = cmt_en)
#     Instance.save()
#     return Response(status=201)

# @api_view(['GET'])
# @schema(None)
# def Instance(request):
#     ip = 
#     instanceNumber = request.POST.get('instanceNumber')
#     dBeg = request.POST.get('dBeg')
#     OS = request.POST.get('OS')
#     extMemory = request.POST.get('extMemory')
#     path = request.POST.get('path')
#     iin_superuser = request.POST.get('iin_superuser')
#     fio_kz = request.POST.get('fio_kz')
#     fio_ru = request.POST.get('fio_ru')
#     email = request.POST.get('email')
#     fio_en = request.POST.get('fio_en')
#     phoneNumber = request.POST.get('phoneNumber')
#     cmt_kz = request.POST.get('cmt_kz')
#     cmt_ru = request.POST.get('cmt_ru')
#     cmt_en = request.POST.get('cmt_en')
#     Instance = Instance(instanceNumber =instanceNumber, dBeg =dBeg, OS = OS, extMemory = extMemory, path = path, iin_superuser =iin_superuser, fio_kz = fio_kz, fio_ru = fio_ru, email = email, fio_en = fio_en, phoneNumber = phoneNumber, cmt_kz = cmt_kz, cmt_ru = cmt_ru, cmt_en = cmt_en)
#     Instance.save()
#     return Response(status=200)   

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

class MessageTypeListCreateView(generics.ListCreateAPIView):
    queryset = MessageType.objects.all()
    serializer_class = MassageTypeSerializer

class MessageTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageType.objects.all()
    serializer_class = MassageTypeSerializer


class WorkMessageListCreateView(generics.ListCreateAPIView):
    queryset = WorkMessage.objects.all()
    serializer_class = WorkMessageSerializer

class WorkMessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkMessage.objects.all()
    serializer_class = WorkMessageSerializer


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

