
# from shortener.models import KirrURL
import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings , "SHORTCODE_MIN", 6)

def code_generator(size=6,chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def createShortcode(instance, size=SHORTCODE_MIN):
	new_code = code_generator (size=size)
	print instance
	print instance.__class__
	print instance.__class__.__name__
	IClass =instance.__class__
	qs=IClass.objects.filter(shortcode=new_code).exists()
	if qs:
		return createShortcode( instance ,size=size )
	else:
		return new_code