from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from contact.forms import ContactForm
@csrf_protect
def contact(request):
	errors = []
	if request.method == 'POST':
#		if not request.POST.get('subject',''):
#			errors.append('Enter a subject.')
#		if not request.POST.get('message',''):
#			errors.append('Enter a message')
#		if request.POST.get('email') and '@' not in request.POST['email']:
#			errors.append('Enter a valid e-mail address.')
#		if not errors:
#			send_mail(request.POST['subject'],request.POST['message'], request.POST.get('email', 'likeshan168@sina.com'),['likeshan168@163.com'])
#		return HttpResponseRedirect('/contact/thanks/')
#	return render_to_response('contact_form.html',{'error':errors, 'subject':request.POST.get('subject',''),'message':request.POST.get('message',''),'email':request.POST.get('email','')},c)
		form = ContactForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			send_mail(cd['subject'],cd['message'],cd.get('email','likeshan168@sina.com'),['likeshan168@163.com'],auth_password='likeshannihao168')
			return HttpResponseRedirect('/contact/thanks')
	else:
		form=ContactForm(initial={'subject':'I love your site!'})
	return render_to_response('contact_form.html',{'form':form},context_instance=RequestContext(request))
