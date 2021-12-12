from django.shortcuts import render
from .models import post, contact_message, About, Proj_achievements, Legislative_activitie, Quotes, Empowerment, image
from django.views.generic import ListView, DetailView
from .forms import contact_form
from django.views import View
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.list import MultipleObjectMixin

# Create your views here.


        

class Home_detail(ListView):


	model=post

	
	template_name = 'polweb/home.html'
	



	
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['form']= contact_form()
		context['abut']= About.objects.all()
		context['quot']=Quotes.objects.order_by('-time')
		context['pix']=image.objects.all()
		return context
			
class contact_form_view(MultipleObjectMixin, FormView):
	template_name = 'polweb/home.html'
	form_class = contact_form
	model = contact_message
	
	def form_valid(self,form):
		form.save()
		return super().form_valid(form)
		
	def post(self, request, *args, **kwargs):
		queryset=self.get_queryset()
		return super().post(request, *args, **kwargs)
	def get_success_url(self):
		return reverse('home')
		
class HomeView(View):
	def get(self, request, *args, **kwargs):
		view = Home_detail.as_view()
		return view(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		view = contact_form_view.as_view()
		return view(request, *args, **kwargs)
		
		
		
	
	
	
	
class About_detail(ListView):
	model=About
	template_name='polweb/about.html'
	
	
	
class Proj_detail(ListView):
	model=Proj_achievements
	template_name='polweb/list_project.html'
	paginate_by=20
	context_object_name="project"
	ordering=['-time']

		

class Project_detail(DetailView):
	model=Proj_achievements
	template_name='polweb/project.html'
	context_object_name="project"
	
	
class Bill_list(ListView):
	model=Legislative_activitie
	template_name='polweb/bill.html'
	paginate_by=20
	ordering=['-time']
class Bill_detail(DetailView):
	model=Legislative_activitie
	template_name='polweb/bill-detail.html'
	context_object_name="bill"
	
	

class Quotes_detail(ListView):
	model=Quotes
	template_name='polweb/quotes.html'
	ordering=['-time']
	
class Emp_detail(ListView):
	model=Empowerment
	template_name='polweb/empowerment.html'
	context_object_name="kole"
	ordering=['-time']
	paginate_by= 20
class Empowerment_detail(DetailView):
	model=Empowerment
	template_name='polweb/detail_empowerment.html'
	context_object_name="kole"
	
	

