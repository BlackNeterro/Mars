from django.db import models
import uuid

# Create your models here.
class Instance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    instanceNumber = models.CharField('Инстант', max_length=50, null=True)
    dBeg = models.DateField('Дата установки', null=True)
    OS = models.CharField('Операционная система', max_length=50, null=True)
    extMemory = models.CharField('Номер HD', max_length=50, null=True)
    path = models.CharField('Путь установки', max_length=50, null=True)
    iin_superuser = models.CharField('', max_length=12, null=True)
    fio_kz = models.CharField('ФИО каз.', max_length=50, null=True)
    fio_ru = models.CharField('ФИО рус.', max_length=50, null=True)
    fio_en = models.CharField('ФИО англ.', max_length=50, null=True)
    phoneNumber = models.CharField('', max_length=12, null=False)
    cmt_kz = models.CharField('Коммент каз.', max_length=100, null=True)
    cmt_ru = models.CharField('Коммент рус.', max_length=100, null=True)
    cmt_en = models.CharField('Коммент англ', max_length=100, null=True)

class AppType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name_kz = models.CharField('Наименование организации каз', max_length=50, null=True)
    name_ru = models.CharField('Наименование организации рус', max_length=50, null=True)
    name_en = models.CharField('Наименование организации англ', max_length=50, null=True)

class Enterprise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, blank=True, null=True)
    bin = models.CharField('БИН/ИИН', max_length=12, null=False)
    name_kz = models.CharField('Названи каз', max_length=50, null=True)
    name_ru = models.CharField('Названи рус', max_length=50, null=True)
    name_en = models.CharField('Названи англ', max_length=50, null=True)
    phoneNumber = models.CharField('Номер телефона', max_length=12, null=False)
    email = models.EmailField('Емайл', null=True)
    website = models.URLField('Ссылка', null=True)
    dBeg = models.DateField('Дата открытие предприятия', null=False)
    dEnd = models.DateField('Дата закрытия предприятия', null=True)
    cmt_kz = models.CharField('Комментарии (каз)', max_length=50, null=True)
    cmt_ru = models.CharField('Комментарии (рус)', max_length=50, null=True)
    cmt_en = models.CharField('Комментарии (англ)', max_length=50, null=True)
    
class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, blank=True, null=True)
    appType = models.ForeignKey(AppType, on_delete=models.CASCADE, blank=True, null=True)
    dtBeg = models.DateField('Дата Начала', null=False)
    dtEnd = models.DateField('Дата окончания', null=True)
    response = models.CharField('Ответ от приложения', max_length=50, null=True)
    cmt_kz = models.CharField('Комментарии (каз)', max_length=50, null=True)
    cmt_ru = models.CharField('Комментарии (рус)', max_length=50, null=True)
    cmt_en = models.CharField('Комментарии (англ)', max_length=50, null=True)

    
class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name_kz = models.CharField('Названи каз', max_length=50, null=True)
    name_ru = models.CharField('Названи рус', max_length=50, null=True)
    name_en = models.CharField('Названи англ', max_length=50, null=True)
    moduleURL = models.URLField('Ссылка', null=True)
    cmt_kz = models.CharField('Коммент каз.', max_length=100, null=True)
    cmt_ru = models.CharField('Коммент рус.', max_length=100, null=True)
    cmt_en = models.CharField('Коммент англ', max_length=100, null=True)

    
class Repayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, blank=True, null=True)
    dtBeg = models.DateField('Дата оплаты', null=True)
    amount = models.CharField('Сумма оплаты', max_length=50, null=True)
    paymentType = models.CharField('Метод оплаты', max_length=50, null=True)

class EnterpriceAccess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    dtEnd = models.DateField('Дата окончания', null=True)

class RepaymentModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    repayment = models.ForeignKey(Repayment, on_delete=models.CASCADE, blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    monthCount = models.CharField('Не понятно', max_length=50, null=True)
