from django.contrib import admin
from base import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class AppointmentInline(admin.TabularInline):
    model = models.Appointment
    extra = 1

class MedicalRecordInline(admin.TabularInline):
    model = models.MedicalRecord
    extra = 1

class LabTestInline(admin.TabularInline):
    model = models.LabTest
    extra = 1

class PrescriptionInline(admin.TabularInline):
    model = models.Prescription
    extra = 1

class BillingInline(admin.TabularInline):
    model = models.Billing
    extra = 1

class ServiceAdmin(ImportExportModelAdmin):
    list_display = ['name', 'cost']
    search_fields = ['name', 'description']
    filter_horizontal = ['available_doctors']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'status']
    search_fields = ['patient__username', 'doctor__user__username']
    inlines = [MedicalRecordInline, LabTestInline, PrescriptionInline, BillingInline]

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'diagnosis']

class LabTestAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'test_name']

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'medications']

class BillingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'total', 'status', 'date']


admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.MedicalRecord, MedicalRecordAdmin)
admin.site.register(models.LabTest, LabTestAdmin)
admin.site.register(models.Prescription, PrescriptionAdmin)
admin.site.register(models.Billing, BillingAdmin)

