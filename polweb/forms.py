from django import forms
from .models import contact_message 

# Create your models here.

class contact_form(forms.ModelForm):
	class Meta:
		model = contact_message
		fields=['name','message']
		text={'name':'','messsage':''}
	
