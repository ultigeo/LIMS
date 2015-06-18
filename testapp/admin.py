from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from testapp.models import *
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.models import User,Group
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
#from django.contrib import databrowse

# Register your models here.
class StaffAdmin(UserAdmin):

    def queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        qs = qs.filter(Q(is_staff=True) | Q(is_superuser=True))
        return qs

class CustomerAdmin(StaffAdmin):

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.exclude(Q(is_staff=True) | Q(is_superuser=True))
        return qs

class ladm_badminunitAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'type_code','parcel_id', 'party_id', 'admindocumenturi','creation_date','expiration_date')
    search_fields = ['id','parcel_id']
    ordering = ['id']

class AdministrationAreaAdmin(LeafletGeoAdmin):
    pass
    list_display = ('unitid', 'name', 'leng', 'area')
    search_fields = ['unitid']
    ordering = ['unitid']

class RegistrationSectionAdmin(LeafletGeoAdmin):
    pass
    list_display = ('sectionid', 'adminarea','name', 'leng', 'area')
    search_fields = ['sectionid']
    ordering = ['sectionid']

class RiversAdmin(LeafletGeoAdmin):
    pass
    list_display = ('id', 'name','reserve')
    search_fields = ['id']
    ordering = ['id']
    list_filter=('reserve',)

class RiperianAdmin(LeafletGeoAdmin):
    pass
    list_display = ('id', 'name','reserve')
    search_fields = ['id']
    ordering = ['id']
    list_filter=('reserve',)

class RoadsAdmin(LeafletGeoAdmin):
    pass
    list_display = ('id','name','road_type','road_class','reserve')
    search_fields = ['id']
    ordering = ['road_type']
    list_filter=('road_type','road_class',)

class RegistrationBlockAdmin(LeafletGeoAdmin):
    pass
    list_display = ('sectionid', 'blockid','name', 'leng', 'area')
    search_fields = ['sectionid']
    ordering = ['sectionid']

class las_parcelAdmin(LeafletGeoAdmin):
    pass
    list_display = ('id', 'blockid', 'parcel_no', 'sectcode', 'areacode')
    search_fields = ['id','parcel_no']
    ordering = ['id']

class las_applicationAdmin (admin.ModelAdmin):
    list_display = ('app_id','first_name','last_name','email','telephone', 'id_number', 'date_applied','application_type','applicant_type','status')
    search_fields = [ 'id_number'] 
    ordering = ['status']
    #readonly_fields = ['dc_comments ','upload_dcreport', 'final_comments']
    list_filter=('applicant_type','application_type','status',)
    actions = ['make_verify'] 

    def make_verify(self, request, queryset):
        rows_updated = queryset.update(status='Verified')
        if rows_updated == 1:
            message_bit = "1 application was"
        else:
            message_bit = "%s applications were" % rows_updated
        self.message_user(request, "%s successfully verified." % message_bit)
    make_verify.short_description = "Verify selected applications"
    
        

class developmentAdmin(las_applicationAdmin):
    readonly_fields = ['first_name','last_name', 'email', 'telephone', 'id_number','title','search','comment']
    #exclude = ('id', 'user',)

class completedAdmin(developmentAdmin):
    pass

class approvedAdmin(completedAdmin):
    pass

class transactionAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'assigned', 'assignee_id', 'status', 'approval_datatime','fee_paid','change_action')
    search_fields = ['id','status']
    ordering = ['id']

class dev_controlunitAdmin(admin.ModelAdmin):
    pass
    list_display = ('las_application', 'User', 'dc_verified', 'dc_comments', 'date_checked')
    search_fields = ['user']
    ordering = ['las_application']


class valuationAdmin (admin.ModelAdmin):
    pass
    list_display = ('valuation_id', 'badminunit', 'value_amount', 'valuationstartdate', 'valuationenddate')
    search_fields = ['valuation_id','badminunit']
    ordering = ['valuation_id']

    
class las_partyAdmin(admin.ModelAdmin):
    pass  
    list_display = ('id', 'partytype', 'name', 'gender_code', 'id_number','address_id','email','mobile','preffered_communication')
    search_fields = ['id','id_number']
    ordering = ['id']

  
class DocumentsAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'of_type', 'document_name', 'document_image', 'datetime_uploaded')
    search_fields = ['id','document_name']
    ordering = ['id']

class Landuse_RestrictionAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'adminunit', 'landuserestriction_type', 'registration_date', 'expiry_date')
    search_fields = ['id','adminunit']
    ordering = ['id']

class landuse_zoningAdmin(LeafletGeoAdmin):
    pass
    list_display = ('id', 'zone_code', 'zone_type', 'zone_Description', 'area')
    search_fields = ['id','zone_code']
    ordering = ['id']

class landcoverAdmin(LeafletGeoAdmin):
    pass
    list_display = ('gid', 'landcover_code', 'landcover_type','area')
    search_fields = ['gid','landcover_code']
    ordering = ['gid']

class RestrictionsAdmin(admin.ModelAdmin):
    pass
    list_display = ('restriction_id', 'adminunit', 'restriction_type', 'restriction_holder', 'amount')
    search_fields = ['restriction_id','adminunit']
    ordering = ['restriction_id']

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(AdministrationArea, AdministrationAreaAdmin)      
admin.site.register(RegistrationSection, RegistrationSectionAdmin)
admin.site.register(RegistrationBlock, RegistrationBlockAdmin)
admin.site.register(las_parcel, las_parcelAdmin)
admin.site.register(ladm_badminunit, ladm_badminunitAdmin)
admin.site.register(las_application, las_applicationAdmin)
admin.site.register(landuse_zoning, landuse_zoningAdmin)
admin.site.register(valuation, valuationAdmin)
admin.site.register(transaction, transactionAdmin)
admin.site.register(Landuse_Restriction, Landuse_RestrictionAdmin)
admin.site.register(Restrictions, RestrictionsAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(las_party, las_partyAdmin)
#admin.site.register(dev_controlunit, dev_controlunitAdmin)
admin.site.register(development, developmentAdmin)
admin.site.register(Approved_apps, approvedAdmin)
admin.site.register(completed, completedAdmin)
admin.site.register(Riperian,RiperianAdmin)
admin.site.register(Rivers,RiversAdmin)
admin.site.register(Roads,RoadsAdmin)
admin.site.register(UserProfile,UserAdmin)
admin.site.register(landcover,landcoverAdmin)
