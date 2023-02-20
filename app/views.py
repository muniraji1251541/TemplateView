from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class cbv_template(TemplateView):
	template_name='cbv_template.html'

class cbv_context(TemplateView):
	template_name='cbv_context.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['name']='Muniraji'
		context['course']='Django'
		return context

class cbv_forms(TemplateView):
	template_name='cbv_forms.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['form']=Profile()
		return context

	def post(self,request):
		data=Profile(request.POST)
		if data.is_valid():
			return HttpResponse(str(data.cleaned_data))