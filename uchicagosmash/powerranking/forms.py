from django import forms
from uchicagosmash.powerranking.models import *

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Smasher
		fields = ('tag', 'dorm', 'agree')

	agree = forms.BooleanField()

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['dorm'].widget.attrs['class'] = 'form-control'
		self.fields['dorm'].widget.attrs['required'] = 'required'
		self.fields['tag'].widget.attrs['required'] = 'required'
		self.fields['agree'].widget.attrs['required'] = 'required'



class MatchForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = ('winner', 'loser', 'game')

	def __init__(self, *args, **kwargs):
		super(MatchForm, self).__init__(*args, **kwargs)
		self.fields['winner'].widget.attrs['class'] = 'form-control'
		self.fields['winner'].widget.attrs['required'] = 'required'
		self.fields['loser'].widget.attrs['class'] = 'form-control'
		self.fields['loser'].widget.attrs['required'] = 'required'
		self.fields['game'].widget.attrs['class'] = 'form-control'
		self.fields['game'].widget.attrs['required'] = 'required'


class MatchVerificationForm(forms.Form):
	verify = forms.BooleanField()
