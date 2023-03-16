from django.contrib import admin
from .models import (Enterprise,
                     Instance,
                     AppType,
                     MessageType,
                     WorkMessage,
                     Module,
                     Repayment,
                     EnterpriceAccess,
                     RepaymentModule)


# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('id', 'instance', 'bin', 'name_kz', 'name_ru', 'name_en', 'phoneNumber', 'email', 'website', 'dBeg', 'dEnd', 'cmt_kz', 'cmt_ru', 'cmt_en')
    list_display_links = ('id', 'instance', 'bin', 'name_kz', 'name_ru', 'name_en', 'phoneNumber', 'email', 'website', 'dBeg', 'dEnd', 'cmt_kz', 'cmt_ru', 'cmt_en')
    search_fields = ('bin', 'instance', 'phoneNumber', 'email')
    list_filter = ('dBeg', 'dEnd')

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'instanceNumber', 'dBeg', 'OS', 'extMemory', 'path', 'iin_superuser', 'fio_kz', 'fio_ru', 'fio_en', 'phoneNumber', 'cmt_kz', 'cmt_ru', 'cmt_en')
    list_display_links = ('id', 'instanceNumber', 'dBeg', 'OS', 'extMemory', 'path', 'iin_superuser', 'fio_kz', 'fio_ru', 'fio_en', 'phoneNumber', 'cmt_kz', 'cmt_ru', 'cmt_en')
    search_fields = ('iin_superuser', 'phoneNumber', 'email')
    list_filter = ('dBeg')

class AppTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_kz', 'name_ru', 'name_en')
    list_display_links = ('id', 'name_kz', 'name_ru', 'name_en')

class MessageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_kz', 'name_ru', 'name_en')
    list_display_links = ('id', 'name_kz', 'name_ru', 'name_en')

class WorkMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'instance', 'appType', 'dtBeg', 'dtEnd', 'response', 'cmt_kz', 'cmt_ru', 'cmt_en')
    list_display_links = ('id', 'instance', 'appType', 'dtBeg', 'dtEnd', 'response', 'cmt_kz', 'cmt_ru', 'cmt_en')
    list_filter = ('dBeg', 'dtEnd')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_kz', 'name_ru', 'name_en', 'moduleURL', 'cmt_kz', 'cmt_ru', 'cmt_en')
    list_display_links = ('id', 'name_kz', 'name_ru', 'name_en', 'moduleURL', 'cmt_kz', 'cmt_ru', 'cmt_en')
    search_fields = ('moduleURL')

class RepaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'enterprise', 'dtBeg', 'amount', 'paymentType')
    list_display_links = ('id', 'enterprise', 'dtBeg', 'amount', 'paymentType')
    list_filter = ('dBeg')

class EnterpriceAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'enterprise', 'module', 'dtEnd')
    list_display_links = ('id', 'enterprise', 'module', 'dtEnd')
    list_filter = ('module', 'dtEnd')

class EnterpriceAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'repayment', 'module', 'monthCount')
    list_display_links = ('id', 'repayment', 'module', 'monthCount')
    list_filter = ('module', 'dtEnd')

admin.site.register(Enterprise)
admin.site.register(Instance)
admin.site.register(AppType)
admin.site.register(MessageType)
admin.site.register(WorkMessage)
admin.site.register(Module)
admin.site.register(Repayment)
admin.site.register(EnterpriceAccess)
admin.site.register(RepaymentModule)

