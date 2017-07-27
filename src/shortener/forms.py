from django import forms
# from django.core.validators import URLValidator
from .validators import validate_url,validate_dot_com


class SubmitUrlForm(forms.Form):
	#first we used the validations in the methods of this class 
	#now we are using a separate file for validations
	#now we nee dto change the url to somethings like
	# url =forms.CharField(label='Submit URL')
	url =forms.CharField(
		label='',
		validators=[validate_url],
		widget = forms.TextInput(
			attrs= {
				"placeholder":"Long URL",
				"class" : "form-control"
				}
			)
	)#,validate_dot_com])

#here both the methds are used for cleaning the data we get into either valid
#or invalid data
#this validation is on the form
'''
This clean function runs auto matic when a form is submitted so as we are using external validators we need to comment it
'''
	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm,self).clean()
		# print (cleaned_data)
		#url =cleaned_data['url']
		#print url
#this validation is directly on the field
#as the validation is taking place from the validators file we can comment this function
	# def clean_url(self):
	# 	url =self.cleaned_data['url']
	# 	#print url
	# 	url_validator =URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL")
	# 	return url


#my own validator method
# def validate_url(value):
# 	#checking for the valid urls 
# 	url_validator=URLValidator()
# 	try:
# 		url_validator(value)
# 	except:
# 		raise ValidationError ("Invalid Url through user defined validator")
# 	return value	