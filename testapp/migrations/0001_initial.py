# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import testapp.models
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationArea',
            fields=[
                ('unitid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'AdministrationArea',
            },
        ),
        migrations.CreateModel(
            name='dev_controlunit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dc_verified', models.NullBooleanField(default=None)),
                ('dc_comments', models.TextField(help_text='Development control comments Here', max_length=256, null=True)),
                ('date_checked', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Development Section',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('of_type', models.CharField(max_length=10)),
                ('document_name', models.CharField(max_length=50)),
                ('document_image', models.FileField(null=True, upload_to=testapp.models.upload_docs)),
                ('datetime_uploaded', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Uploaded Documents',
            },
        ),
        migrations.CreateModel(
            name='ladm_badminunit',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type_code', models.CharField(max_length=50, choices=[('Free-hold title', 'Free-hold title'), ('Lease-hold title', 'Lease-hold title'), ('Mining contract', 'Mining contract'), ('Conservation', 'Conservation')])),
                ('creation_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('admindocumenturi', models.ForeignKey(to='testapp.Documents')),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'ADmin Units',
            },
        ),
        migrations.CreateModel(
            name='landcover',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('landcover_code', models.IntegerField(null=True)),
                ('landcover_type', models.CharField(max_length=50, null=True, blank=True)),
                ('landcover_desc', models.CharField(blank=True, max_length=50, null=True, choices=[('1', 'Agricultural'), ('2', 'Residential'), ('3', 'Commercial'), ('4', 'Industry'), ('5', 'Public'), ('6', 'Reserve'), ('7', 'Industry'), ('8', 'Public'), ('9', 'Reserve')])),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'landcover',
            },
        ),
        migrations.CreateModel(
            name='Landuse_Restriction',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('landuserestriction_type', models.CharField(max_length=50, choices=[('Permitted Use', 'Permitted Use'), ('Non-permitted Use', 'Non-permitted Use'), ('Consented Use', 'Consented Use'), ('Actual Use', 'Actual Use')])),
                ('landuserestriction_desc', models.TextField(max_length=100)),
                ('registration_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('adminunit', models.ForeignKey(to='testapp.ladm_badminunit')),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Landuse Restriction',
            },
        ),
        migrations.CreateModel(
            name='landuse_zoning',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('zone_code', models.IntegerField()),
                ('zone_type', models.CharField(max_length=50, null=True, choices=[('Agricultural', 'Agricultural'), ('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Industry', 'Industry'), ('Public', 'Public'), ('Reserve', 'Reserve')])),
                ('zone_Description', models.CharField(max_length=50)),
                ('area', models.FloatField()),
                ('length', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Landuse Zoning',
            },
        ),
        migrations.CreateModel(
            name='las_application',
            fields=[
                ('app_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('id_type', models.CharField(default='National ID', max_length=20, null=True, choices=[('National ID', 'National ID'), ('Passport', 'Passport'), ('Company Registration Number', 'Company Registration Number')])),
                ('id_number', models.CharField(max_length=15, null=True)),
                ('parcel_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(default='user@user.com', max_length=50)),
                ('telephone', models.CharField(help_text='Enter phone number', max_length=50)),
                ('applicant_type', models.CharField(max_length=50, choices=[('Owner', 'Owner'), ('Buyer', 'Buyer'), ('Other', 'Other')])),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('date_approved', models.DateTimeField(null=True, blank=True)),
                ('application_type', models.CharField(max_length=50, choices=[('Registration', 'Registration'), ('Official Search', 'Official Search'), ('Change of User', 'Change of User')])),
                ('title', models.FileField(help_text='Upload copy of Title', null=True, upload_to=testapp.models.upload_application)),
                ('search', models.FileField(help_text='Upload copy of Search document', null=True, upload_to=testapp.models.upload_application)),
                ('comment', models.FileField(help_text='Upload copy of comment form', null=True, upload_to=testapp.models.upload_application)),
                ('add_comment', models.FileField(help_text='Upload other comment(if available)', null=True, upload_to=testapp.models.upload_application)),
                ('scheme', models.FileField(help_text='Upload copy of Physical Scheme Plan', null=True, upload_to=testapp.models.upload_application)),
                ('ppa', models.FileField(help_text='Upload copy of PPA2', null=True, upload_to=testapp.models.upload_application)),
                ('receipt', models.FileField(help_text='Upload copy of Payment Receipt', null=True, upload_to=testapp.models.upload_application)),
                ('planning', models.FileField(help_text='Upload copy of Planning document', null=True, upload_to=testapp.models.upload_application)),
                ('status', models.CharField(default='Unverified', max_length=15, null=True, choices=[('Unverified', 'Unverified'), ('Verified', 'Verified'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('Closed', 'Closed')])),
                ('registry_comments', models.TextField(help_text='Registry section comments Here', max_length=256, null=True)),
                ('dc_comments', models.TextField(help_text='Development control comments Here', max_length=256, null=True)),
                ('upload_dcreport', models.FileField(null=True, upload_to=testapp.models.upload_report)),
                ('final_comments', models.TextField(help_text='Final comments Here', max_length=256, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_application', 'Can verify applications'),),
            },
        ),
        migrations.CreateModel(
            name='las_parcel',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('blockid', models.IntegerField(null=True, blank=True)),
                ('areacode', models.IntegerField(null=True, blank=True)),
                ('blockname', models.CharField(max_length=50, null=True, blank=True)),
                ('parcel_no', models.CharField(max_length=50, null=True, blank=True)),
                ('sectcode', models.IntegerField(null=True, blank=True)),
                ('surveyornumber', models.CharField(max_length=50, null=True, blank=True)),
                ('approval_datetime', models.DateTimeField(null=True, blank=True)),
                ('historic_datetime', models.DateTimeField(null=True, blank=True)),
                ('parent', models.CharField(default='null', max_length=15, null=True, blank=True)),
                ('area', models.FloatField()),
                ('length', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=21037)),
                ('land_use', models.ForeignKey(blank=True, to='testapp.landuse_zoning', null=True)),
                ('surveydocid', models.ForeignKey(blank=True, to='testapp.Documents', null=True)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'las_parcel',
            },
        ),
        migrations.CreateModel(
            name='las_party',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('ext_id', models.CharField(max_length=50)),
                ('partytype', models.CharField(max_length=50, choices=[('Individual', 'Individual'), ('Company', 'Company'), ('Community', 'Community'), ('Trust', 'Trust'), ('Family', 'Family'), ('Government', 'Government')])),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender_code', models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'N/A')])),
                ('id_type_code', models.CharField(max_length=50, choices=[('National ID', 'National ID'), ('Passport', 'Passport'), ('Company Registration Number', 'Company Registration Number')])),
                ('id_number', models.CharField(max_length=50)),
                ('address_id', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('preffered_communication', models.CharField(max_length=50, choices=[('Email', 'Email'), ('Mobile', 'Mobile'), ('Tel', 'Telephone')])),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'las_party',
            },
        ),
        migrations.CreateModel(
            name='RegistrationBlock',
            fields=[
                ('blockid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('leng', models.FloatField()),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Registration Blocks',
            },
        ),
        migrations.CreateModel(
            name='RegistrationSection',
            fields=[
                ('sectionid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('leng', models.FloatField()),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=21037)),
                ('adminarea', models.ForeignKey(to='testapp.AdministrationArea')),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'RegistrationSection',
            },
        ),
        migrations.CreateModel(
            name='Restrictions',
            fields=[
                ('restriction_id', models.AutoField(max_length=1, serialize=False, primary_key=True)),
                ('restriction_type', models.CharField(max_length=50, choices=[('Morgage', 'Morgage'), ('Courtorder', 'Court Order'), ('Caveat', 'Caveat'), ('Landuse', 'LAnd Use Restriction')])),
                ('restriction_Description', models.CharField(max_length=50)),
                ('restriction_holder', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('adminunit', models.ForeignKey(to='testapp.ladm_badminunit')),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Restrictions',
            },
        ),
        migrations.CreateModel(
            name='Riperian',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('reserve', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Riperian',
            },
        ),
        migrations.CreateModel(
            name='Rivers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('reserve', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Rivers',
            },
        ),
        migrations.CreateModel(
            name='Roads',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('road_type', models.CharField(max_length=50)),
                ('road_class', models.CharField(max_length=5)),
                ('reserve', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=21037)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Roads',
            },
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('assigned', models.BooleanField()),
                ('assigned_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50, choices=[('Lodge', 'Lodge'), ('Validate', 'Validate'), ('Start', 'Start'), ('Assign', 'Assign'), ('Un-Assign', 'Un-Assign'), ('Dispatch', 'Dispatch')])),
                ('approval_datatime', models.DateTimeField()),
                ('service_fee', models.IntegerField()),
                ('fee_paid', models.BooleanField()),
                ('change_action', models.CharField(max_length=50, choices=[('Update', 'Update'), ('Delete', 'Delete'), ('Insert', 'Insert')])),
                ('change_user', models.CharField(max_length=50)),
                ('change_time', models.DateTimeField()),
                ('notes', models.TextField()),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'transaction',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 7, 9))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Userprofiles',
            },
        ),
        migrations.CreateModel(
            name='valuation',
            fields=[
                ('valuation_id', models.IntegerField(serialize=False, primary_key=True)),
                ('value_amount', models.IntegerField()),
                ('valuationstartdate', models.DateTimeField()),
                ('valuationenddate', models.DateTimeField()),
                ('badminunit', models.ForeignKey(to='testapp.ladm_badminunit')),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Valuation',
            },
        ),
        migrations.AddField(
            model_name='transaction',
            name='assignee_id',
            field=models.ForeignKey(to='testapp.UserProfile'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='from_application_id',
            field=models.ForeignKey(to='testapp.las_application'),
        ),
        migrations.AddField(
            model_name='registrationblock',
            name='sectionid',
            field=models.ForeignKey(to='testapp.RegistrationSection'),
        ),
        migrations.AddField(
            model_name='ladm_badminunit',
            name='parcel_id',
            field=models.ForeignKey(to='testapp.las_parcel'),
        ),
        migrations.AddField(
            model_name='ladm_badminunit',
            name='party_id',
            field=models.ForeignKey(to='testapp.las_party'),
        ),
        migrations.AddField(
            model_name='dev_controlunit',
            name='las_application',
            field=models.OneToOneField(to='testapp.las_application'),
        ),
        migrations.CreateModel(
            name='Approved_apps',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Approved Apps',
            },
            bases=('testapp.las_application',),
        ),
        migrations.CreateModel(
            name='completed',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Completed_Apps',
            },
            bases=('testapp.las_application',),
        ),
        migrations.CreateModel(
            name='development',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Development_apps',
            },
            bases=('testapp.las_application',),
        ),
        migrations.CreateModel(
            name='registry',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Registry_apps',
            },
            bases=('testapp.las_application',),
        ),
        migrations.CreateModel(
            name='rejected',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Rejected_apps',
            },
            bases=('testapp.las_application',),
        ),
    ]
