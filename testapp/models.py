# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.gis.db import models
import datetime 
from django.utils import timezone
from django.db.models import signals
from django.contrib.gis.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MaxLengthValidator,MinLengthValidator
#from django_hstore import hstore

def upload_application(instance, filename):
   # return "title_images/%s" % (filename)
    return '/'.join(['application_docs', str(instance.id_number), filename])

def upload_report(instance, filename):
    return "report_images/%s" % (filename)

def upload_docs(instance, filename):
    return "documents/%s" % (filename)



restriction_types = (
    ('Morgage', 'Morgage'),
    ('Courtorder', 'Court Order'),
    ('Caveat', 'Caveat'),
    ('Landuse','LAnd Use Restriction')
)

landuse_zoning_types = (
    ('Agricultural', 'Agricultural'),
    ('Residential', 'Residential'),
    ('Commercial', 'Commercial'),
    ('Industry', 'Industry'),
    ('Public', 'Public'),
    ('Reserve', 'Reserve'),
)

landcover_types = (
    ('1', 'Agricultural'),
    ('2', 'Residential'),
    ('3', 'Commercial'),
    ('4', 'Industry'),
    ('5', 'Public'),
    ('6', 'Reserve'),
    ('7', 'Industry'),
    ('8', 'Public'),
    ('9', 'Reserve'),
)

transaction_types = (
    ('Transfer', 'Transfer'),
    ('Subdivision', 'Subdivision'),
    ('Change of user', 'Change of user'),
    ('Development application', 'Development application'),
    ('Registration', 'Registration'),
    ('Valuation', 'Valuation'),
)
status_types = (
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Registered', 'Registered'),
    ('Deleted', 'Deleted'),
    ('Pending', 'Pending'),
    ('Withdrawn', 'Withdrawn'),
    ('Superceeded', 'Superceeded'),
)
application_status = (
    ('Unverified','Unverified'),
    ('Verified','Verified'),
    ('Approved','Approved'),
    ('Completed','Completed'),
    ('Closed','Closed')
    )
party_types = (
    ('Individual', 'Individual'),
    ('Company', 'Company'),
    ('Community', 'Community'),
    ('Trust', 'Trust'),
    ('Family', 'Family'),
    ('Government', 'Government'),
)
agent_types=(
        ('Owner', 'Owner'),
        ('Buyer', 'Buyer'),
        ('Other','Other'),
)

actual_landuses=(
    ('Agricultural', 'Agricultural'),
    ('Residential', 'Residential'),
    ('Commercial', 'Commercial'),
    ('Industry', 'Industry'),
    ('Public', 'Public'),
    ('Reserve', 'Reserve'),
    )
transaction_status_types = (
        ('Lodge', 'Lodge'),
        ('Validate', 'Validate'),
        ('Start', 'Start'),
        ('Assign', 'Assign'),
        ('Un-Assign', 'Un-Assign'),
        ('Dispatch', 'Dispatch'),
        
    )
status_type=(
        ('Current','Current'), 
        ('Historic','Historic'), 
        ('Pending','Pending'), 
        ('Previous','Previous'),
    )

change_actions = (
        #to edit types
        ('Update', 'Update'),
        ('Delete', 'Delete'),
        ('Insert', 'Insert'),
    )
service_status_types=(
        ('Lodged', 'Lodged'),
        ('Validated', 'Validated'),
        ('Started', 'Started'),
        ('Assigned', 'Assigned'),
        ('Un-Assigned', 'Un-Assigned'),
        ('Dispatched', 'Dispatched'),
        ('Completed','Completed'),
        ('Archived','Archived'),
    )
lims_badminunit_type=(
        ('Free-hold title', 'Free-hold title'),
        ('Lease-hold title', 'Lease-hold title'),
        ('Mining contract', 'Mining contract'),
        ('Conservation', 'Conservation'),
        )

application_status_types = (
        ('Lodged', 'Lodged'),
        ('Validated', 'Validated'),
        ('Started', 'Started'),
        ('Assigned', 'Assigned'),
        ('Un-Assigned', 'Un-Assigned'),
        ('Dispatched', 'Dispatched'),
        ('Completed','Completed'),
        ('Archived','Archived'),  
    )
application_types=(
            ('Registration','Registration'),
            ('Official Search','Official Search'),
            ('Change of User','Change of User'),
            )
    
landuse_restrictions_types = (
            ('Permitted Use', 'Permitted Use'),
            ('Non-permitted Use', 'Non-permitted Use'),
            ('Consented Use', 'Consented Use'),
            ('Actual Use', 'Actual Use'),
        )
id_types=(
               ('National ID','National ID'),
               ('Passport','Passport'),
               ('Company Registration Number','Company Registration Number'),
               )
######## LADM Objects#########
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today()) 
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='Userprofiles'

class Customer(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Customer account'
        verbose_name_plural = 'Customer accounts'

class Staff(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'Staff account'
        verbose_name_plural = 'Staff accounts'

class ladm_badminunit(models.Model):
    id=models.IntegerField(primary_key=True)
    type_code=models.CharField(choices=lims_badminunit_type, max_length=50)
    parcel_id=models.ForeignKey('las_parcel')
    party_id=models.ForeignKey('las_party')
    admindocumenturi=models.ForeignKey('Documents')
    creation_date=models.DateField()
    expiration_date=models.DateField()
    objects=models.Manager()
    
    def __unicode__(self):
        return "%s %s" %(self.id, self.type_code)
    
    class Meta:
        verbose_name_plural = "ADmin Units" 
        managed = True
        
class AdministrationArea(models.Model):
    unitid = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "AdministrationArea"
        managed = True
       
   

class RegistrationSection(models.Model):
    sectionid = models.IntegerField(primary_key=True)
    adminarea = models.ForeignKey(AdministrationArea)
    name= models.CharField(max_length=50)
    leng = models.FloatField()
    area = models.FloatField()
    geom = models.PolygonField(srid=21037)
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = "RegistrationSection"
        managed = True 
        
  
class RegistrationBlock (models.Model):
    blockid = models.IntegerField(primary_key=True)  # Field name made lowercase.
    sectionid = models.ForeignKey(RegistrationSection)  # Field name made lowercase.
    name= models.CharField(max_length=50)
    leng = models.FloatField()
    area = models.FloatField()
    geom = models.PolygonField(srid=21037)
    objects = models.GeoManager()
    class Meta:
        verbose_name_plural = "Registration Blocks"
        managed = True 
       


class las_parcel(models.Model):
    id=models.IntegerField(primary_key=True) 
    blockid=models.IntegerField(null=True,blank=True)
    areacode=models.IntegerField(null=True,blank=True)
    blockname=models.CharField(max_length=50,null=True,blank=True)
    parcel_no=models.CharField(max_length=50,null=True,blank=True)
    sectcode=models.IntegerField(null=True,blank=True)
    land_use=models.ForeignKey('landuse_zoning',null=True,blank=True)
    surveyornumber=models.CharField(max_length=50,null=True,blank=True)
    surveydocid=models.ForeignKey('Documents',null=True,blank=True)
    approval_datetime=models.DateTimeField(null=True,blank=True)
    historic_datetime=models.DateTimeField(null=True,blank=True)
    parent=models.CharField(max_length=15, null=True,default="null",blank=True)
    area=models.FloatField()
    length=models.FloatField()
    geom=models.MultiPolygonField(srid=21037)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s %s" %(self.id, self.blockid)
    
    class Meta:
        verbose_name_plural = "las_parcel" 
        managed = True
        


class Restrictions(models.Model):
    restriction_id = models.AutoField(max_length=1, primary_key=True)
    adminunit = models.ForeignKey(ladm_badminunit)
    restriction_type = models.CharField(max_length=50, choices= restriction_types)
    restriction_Description = models.CharField(max_length=50)
    restriction_holder = models.CharField(max_length=50)
    amount = models.IntegerField()
    objects=models.Manager()

    class Meta:
        verbose_name_plural = "Restrictions"
        managed = True        

class Landuse_Restriction(models.Model):
    id = models.IntegerField(primary_key=True)
    adminunit = models.ForeignKey(ladm_badminunit)
    landuserestriction_type = models.CharField(max_length=50, choices= landuse_restrictions_types)
    landuserestriction_desc = models.TextField(max_length=100)
    registration_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    objects=models.Manager()

    class Meta:
        verbose_name_plural = "Landuse Restriction"
        managed = True 

class unverifiedManager(models.Manager):
    def get_queryset(self):
        return super(unverifiedManager, self).get_queryset().filter(status='Unverified')

class verifiedManager(models.Manager):
    def get_queryset(self):
        return super(verifiedManager, self).get_queryset().filter(status='Verified')

class completedManager(models.Manager):
    def get_queryset(self):
        return super(completedManager, self).get_queryset().filter(status='Completed')

class approvedManager(models.Manager):
    def get_queryset(self):
        return super(approvedManager, self).get_queryset().filter(status='Approved')

class rejectedManager(models.Manager):
    def get_queryset(self):
        return super(rejectedManager, self).get_queryset().filter(status='Rejected')
   
        
class las_application(models.Model):
    app_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    id_type=models.CharField(max_length=20, null=True, choices=id_types, default=id_types[0][0])
    id_number=models.CharField(max_length=15,null=True)
    parcel_number=models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=50, default='user@user.com')
    telephone = models.CharField(max_length=50, help_text="Enter phone number")
    applicant_type=models.CharField(choices=agent_types,max_length=50)    
    date_applied = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True,blank=True)
    date_approved = models.DateTimeField(null=True,blank=True)
    application_type = models.CharField(max_length=50, choices=application_types)  
    title = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of Title")
    search = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of Search document")
    comment = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of comment form")
    add_comment = models.FileField(upload_to= upload_application, null=True, help_text="Upload other comment(if available)")
    scheme = models.FileField(upload_to=upload_application, null=True, help_text="Upload copy of Physical Scheme Plan")
    ppa = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of PPA2")
    receipt = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of Payment Receipt")
    planning = models.FileField(upload_to= upload_application, null=True, help_text="Upload copy of Planning document")
    status = models.CharField(max_length=15, null=True, choices=application_status, default=application_status[0][0])
    registry_comments = models.TextField(max_length = 256, help_text="Registry section comments Here", null=True)
    dc_comments = models.TextField(max_length = 256, help_text="Development control comments Here", null=True)
    upload_dcreport = models.FileField(upload_to= upload_report, null=True)
    final_comments = models.TextField(max_length = 256, help_text="Final comments Here", null=True)
    user = models.ForeignKey(User)
    #objects=unverifiedManager()

    def __unicode__(self):
        return u'%s' % (self.first_name)
    
    class Meta:
        verbose_name_plural = "las_applications" 
        managed = True

    class Meta:
        permissions = (
            ('view_application', 'Can verify applications'),
        )
class development(las_application):
    approved = verifiedManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Development_apps"

class registry(las_application):
    approved = unverifiedManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Registry_apps"

class Approved_apps(las_application):
    approved = approvedManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Approved Apps"

class rejected(las_application):
    approved = rejectedManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Rejected_apps"

class completed(las_application):
    approved = completedManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Completed_Apps"

class dev_controlunit(models.Model):
    las_application=models.OneToOneField(las_application)
    User=models.ForeignKey(User)
    dc_verified = models.NullBooleanField(blank=True, null=True, default=None)
    dc_comments = models.TextField(max_length = 256, help_text="Development control comments Here", null=True)
    date_checked = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    class Meta:
        verbose_name_plural = "Development Section" 
        managed = True
        
class las_party (models.Model):
    
     GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'N/A'),
        )
     preffered_comm_methd=(
                ('Email','Email'),
                ('Mobile','Mobile'),
                ('Tel','Telephone')
        )
     
     id=models.IntegerField(primary_key=True)
     ext_id=models.CharField(max_length=50)
     partytype=models.CharField(choices=party_types,max_length=50)
     name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50, null=True, blank=True)
     gender_code=models.CharField(choices=GENDER_CHOICES,max_length=50)
     id_type_code=models.CharField(choices=id_types,max_length=50)
     id_number=models.CharField(max_length=50)
#      contacts=hstore.DictionaryField()
     address_id=models.CharField(max_length=50)
     email=models.EmailField()
     mobile=models.CharField(max_length=50)
     phone=models.CharField(max_length=50)
     preffered_communication=models.CharField(choices=preffered_comm_methd,max_length=50)
     objects=models.Manager()
     #objects = hstore.HStoreManager()

     def __unicode__(self):
        return "%s %s" %(self.id, self.name)
    
     class Meta:
        verbose_name_plural = "las_party" 
        managed = True
    
        
class transaction(models.Model):
    id=models.IntegerField(primary_key=True)
    from_application_id=models.ForeignKey('las_application')
    assigned=models.BooleanField()
    assignee_id=models.ForeignKey('UserProfile')
    assigned_date=models.DateTimeField()
    status=models.CharField(choices=transaction_status_types,max_length=50)
    approval_datatime=models.DateTimeField()
    service_fee=models.IntegerField()
    fee_paid=models.BooleanField()
    change_action=models.CharField(choices=change_actions,max_length=50)
    change_user=models.CharField(max_length=50)
    change_time=models.DateTimeField()
    notes=models.TextField()
    objects=models.Manager()
    
    def __unicode__(self):
        return "%s" %(self.id)

    class Meta:
        verbose_name_plural = "transaction" 
        managed = True
           
                       
  #### KLADM Extensions#####

class landuse_zoning(models.Model):
    id = models.AutoField(primary_key=True)
    zone_code = models.IntegerField()
    zone_type = models.CharField(max_length=50, null=True, choices= landuse_zoning_types)
    zone_Description = models.CharField(max_length=50)
    area=models.FloatField()
    length=models.FloatField()
    geom = models.MultiPolygonField(srid=21037)
    objects = models.GeoManager()

    def __unicode__(self):              # __unicode__ on Python 2
        return 'Type: %s' % self.zone_type
 
    class Meta:
        verbose_name_plural = "Landuse Zoning" 
        managed = True

class landcover(models.Model):
    gid = models.AutoField(primary_key=True)
    landcover_code=models.IntegerField(null=True)
    landcover_type = models.CharField(max_length=50,null=True,blank=True)
    landcover_desc= models.CharField(max_length=50, blank=True, null=True, choices= landcover_types)
    area= models.FloatField()
    geom = models.MultiPolygonField(srid=21037)
    objects=models.GeoManager()

    class Meta:
        verbose_name_plural = "landcover" 
        managed = True
        
    
class valuation(models.Model):
    valuation_id = models.IntegerField(primary_key=True)
    badminunit = models.ForeignKey('ladm_badminunit')
    value_amount = models.IntegerField()
    valuationstartdate = models.DateTimeField()
    valuationenddate = models.DateTimeField()
    objects=models.Manager()

    class Meta:
        verbose_name_plural = "Valuation" 
        managed = True
       
        
class Documents (models.Model):
    id=models.IntegerField(primary_key=True)
    of_type=models.CharField(max_length=10)
    document_name=models.CharField(max_length=50, blank=False, null=False)
    document_image=models.FileField(upload_to= upload_docs, null=True)
    datetime_uploaded=models.DateTimeField()
    objects=models.GeoManager()

    
    class Meta:
        verbose_name_plural = "Uploaded Documents" 
        managed = True
        
class Rivers(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.CharField(max_length=255)
    reserve=models.IntegerField( null=True, blank= True)
    geom= models.MultiLineStringField(srid=21037)
    objects=models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rivers" 
        managed = True

class Riperian(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.CharField(max_length=255)
    reserve=models.IntegerField( null=True, blank= True)
    geom= models.MultiPolygonField(srid=21037)
    objects=models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Riperian" 
        managed = True

class Roads(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.CharField(max_length=255)
    road_type=models.CharField(max_length= 50)
    road_class=models.CharField(max_length=5)
    reserve=models.IntegerField( null=True, blank= True)
    geom= models.MultiLineStringField(srid=21037)
    objects=models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Roads" 
        managed = True

