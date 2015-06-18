from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.core import serializers
from testapp.models import las_parcel,las_application,Rivers,Roads,development,completed
from testapp.forms import *
from django.views.generic.base import TemplateView
import uuid
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views


# Create your views here.
def index(request):
    #return HttpResponse('Welcome. add application_portal after :8080/ to load application page')
    return render(request, 'application_portal/index.html')

def about(request):
    return render(request, 'application_portal/about.html')

def review(request):
    return render(request, 'application_portal/review.html')

def datas(request):
    return render(request, 'application_portal/data.html')

def services(request):
    return render(request, 'application_portal/services.html')

def plans(request):
    return render(request, 'application_portal/plans.html')


def applied(request):
    return render(request, 'application_portal/applied.html')

def register_success(request):
    return render(request, 'registration/registration_complete.html')

@login_required
def application_status(request):
    user = request.user.get_full_name()
    applications = development.objects.filter(user__user=request.user)
    #developments = development.objects.filter(user__user=request.user)
    #html = []
    #for k in applications:
        #html.append('<tr><td>%s - %s - %s - %s </td></tr>' % (k.first_name, k.id_number,k.date_applied,k.status))
    #return HttpResponse('Welcome %s. This is your home.<br/><table>%s</table>' % (user, '\n'.join(html)))
    return render_to_response("application_portal/status.html", {"applications": applications}, context_instance=RequestContext(request))


def search(request):
    datas = las_parcel.objects.all()
    return render_to_response("application_portal/mapfinal.html", {'datas': datas}, context_instance=RequestContext(request))

@api_view(['GET'])
def mapping(request):
    result = las_parcel.objects.all()
    data = serializers.serialize('json', result)
    return Response(data, status=status.HTTP_200_OK, content_type='application/json')
    #return render_to_response("application_portal/mapfinal.html", locals(), context_instance=RequestContext(request))

@api_view(['GET'])
def mapping_filter(request):
    request_data = request.QUERY_PARAMS
    filtered_fields = request_data['fields']

    kwargs = {}

    if "registration" in filtered_fields:
        kwargs['registration'] = request_data['registration']
    if "legal" in filtered_fields:
        kwargs['legal'] = request_data['legal']

    try:
        result = las_parcel.objects.filter(**kwargs)
        data = serializers.serialize('json', result)
        return Response(data, status=status.HTTP_200_OK, content_type='application/json')
        #return render_to_response("application_portal/mapfinal.html", locals(), context_instance=RequestContext(request))
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def maps(request):
    maps = las_parcel.objects.all()
    return render_to_response("application_portal/maps.html", {maps: 'maps'}, context_instance=RequestContext(request))

@login_required
def application_portal(request):
    form = applicationForm
    if request.method == 'POST':
        form = applicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            #return payment_portal(request)
            return HttpResponseRedirect(reverse("applied"))
        else:
            print form.errors
    else:
        form = applicationForm()
    images=las_application.objects.all()
    return render(request, 'application_portal/apply.html', {'form': form,'images':images})

def reader_portal(request):
    form = readerForm
    if request.method == 'POST':
        form = readerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #return index(request)
            return HttpResponseRedirect(reverse("/ladm/reader"))
        else:
            print form.errors
    else:
        form = readerForm()
    return render(request, 'application_portal/reader.html', {'form': form})

def dc_portal(request):
    form = dcForm
    if request.method == 'POST':
        form = dcForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #return index(request)
            return HttpResponseRedirect(reverse("reader"))
        else:
            print form.errors
    else:
        form = dcForm()
    return render(request, 'application_portal/dc.html', {'form': form})
# Create your views here.

def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid(): 
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
            activation_key = hashlib.sha1(salt+email).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user=User.objects.get(username=username)

            # Create and save user profile                                                                                                                                  
            new_profile = UserProfile(user=user, activation_key=activation_key, 
                key_expires=key_expires)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours http://3b50af7f.ngrok.com/ladm/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/ladm/register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('application_portal/register.html', args, context_instance=RequestContext(request))

def register_confirm(request, activation_key):
    if request.user.is_authenticated():
        HttpResponseRedirect('/ladm/')

    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    if user_profile.key_expires < timezone.now():
        return render_to_response('registration/confirm_expired.html')
    
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('registration/confirm.html')

def user_login(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            
            if user.is_active:

                if user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect('/admin/')
                else:

                    login(request, user)
                    return HttpResponseRedirect('/ladm/')
                
            else:
                return HttpResponseRedirect(reverse("login"))
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('application_portal/login.html', args, context_instance=RequestContext(request))

    
    else:
        
        return render(request, 'application_portal/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/ladm/')

def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response

class applicationsView(TemplateView):
    template_name = 'application_portal/reader.html'

    def get_context_data(self,**kwargs):
        context = super(applicationsView,self).get_context_data(**kwargs)
        context['object_list'] = applications.objects.all()
        return context

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@ke_ladm.com'),
                ['laskenya@dkut.ac.ke'], #email address where message is sent.
            )
            return HttpResponseRedirect('/ladm/thanks/')
    return render(request, 'application_portal/contact.html',
        {'errors': errors})
def thanks(request):
    return render_to_response('application_portal/thanks.html')
