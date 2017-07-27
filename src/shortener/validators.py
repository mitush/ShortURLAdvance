from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


#my own validator method
def validate_url(value):
	#checking for the valid urls 
	print 'In validate function'
	url_validator=URLValidator() 
	enter=True
	enter2=True
	try:
		url_validator(value)
	except:
		url_new = "http://"+value
		try:
			url_validator(url_new)
		except:
			raise ValidationError ("Invalid Url through user defined validator")
		print "url_new is ",url_new	
		print "returned url is ",url_new
		return url_new	
	print ("returned url is ",value)
	return value	
''' 
	try:
		print "in try block1"
		url_validator(value)
	except:
		enter=False
		value_url="http://"+value
		print value_url
	if enter == False:	

		try:
			print "in try block2"
			url_validator(value_url)
		except:
			enter2=False
			#value_url_valid=False
		if enter2==True:
			return value_url

	if enter == False and enter2==False:
		raise ValidationError ("Invalid Url through user defined validator")
	#elif enter == True or enter2 ==False:
	return value
	'''

def validate_dot_com(value):
	#value=validate_url(value)
	if not "com" in value:
		raise ValidationError ("This is not valid because of .com")
	print ("final returned value is ",value)
	return value	